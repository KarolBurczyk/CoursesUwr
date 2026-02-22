import torch
import numpy as np
from transformers import AutoTokenizer, AutoModel

with open('clusters.txt', 'r', encoding='utf-8') as f:
    clusters_txt = f.read()

model_name = 'allegro/herbert-base-cased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def get_contextual_embedding(word):
    inputs = tokenizer(f"[CLS] {word} [SEP]", return_tensors='pt', truncation=True, max_length=512)
    
    with torch.no_grad():
        outputs = model(**inputs)
        
        layer_outputs = outputs.hidden_states
        if layer_outputs is not None:
            word_tokens = layer_outputs[7][0, 1:-1]
        else:
            word_tokens = outputs.last_hidden_state[0, 1:-1]
        
        attention_mask = inputs['attention_mask'][0, 1:-1].unsqueeze(-1).float()
        masked_tokens = word_tokens * attention_mask
        sum_tokens = masked_tokens.sum(dim=0)
        count_tokens = attention_mask.sum(dim=0)
        mean_vec = sum_tokens / count_tokens.clamp(min=1e-8)
        
        vec = mean_vec.numpy()
        norm = np.linalg.norm(vec)
        return vec / norm if norm > 0 else None

words = set()
for line in clusters_txt.strip().split('\n'):
    if ':' in line and len(line.split(':')) > 1:
        _, word_list = line.split(':', 1)
        words.update(word_list.strip().split())

vectors = {}
missing = []
for word in sorted(words):
    vec = get_contextual_embedding(word)
    if vec is not None:
        vectors[word] = vec
    else:
        missing.append(word)

with open('word_embeddings_file.txt', 'w', encoding='utf-8') as f:
    for word in sorted(vectors):
        vec_str = ' '.join(f'{x:.6f}' for x in vectors[word])
        f.write(f'{word} {vec_str}\n')

torch.cuda.empty_cache() if torch.cuda.is_available() else None
