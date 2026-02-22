import torch
import numpy as np
from transformers import AutoTokenizer, AutoModel

with open('clusters.txt', 'r', encoding='utf-8') as f:
    clusters_txt = f.read()

model_name = 'allegro/herbert-base-cased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
model.eval()

emb_static = model.embeddings.word_embeddings.weight.detach().cpu().numpy()

def get_static_embedding(word):
    tokens = tokenizer.tokenize(word)
    if not tokens: return None
    token_ids = tokenizer.convert_tokens_to_ids(tokens)
    valid_ids = [tid for tid in token_ids if 0 <= tid < emb_static.shape[0]]
    if not valid_ids: return None
    vecs = emb_static[valid_ids]
    return vecs.mean(axis=0) / np.linalg.norm(vecs.mean(axis=0))

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
        vec = mean_vec.cpu().numpy()
        return vec / np.linalg.norm(vec)

alpha = 0.1
def get_combined_embedding(word):
    vec_static = get_static_embedding(word)
    vec_context = get_contextual_embedding(word)
    if vec_static is not None and vec_context is not None:
        combined = alpha * vec_static + (1 - alpha) * vec_context
        return combined / np.linalg.norm(combined)
    return vec_context or vec_static

words = set()
for line in clusters_txt.strip().split('\n'):
    if ':' in line and len(line.split(':')) > 1:
        _, word_list = line.split(':', 1)
        words.update(word_list.strip().split())

vectors = {}
for word in sorted(words):
    vec = get_combined_embedding(word)
    if vec is not None:
        vectors[word] = vec

with open('word_embeddings_file.txt', 'w', encoding='utf-8') as f:
    for word in sorted(vectors):
        vec_str = ' '.join(f'{x:.6f}' for x in vectors[word])
        f.write(f'{word} {vec_str}\n')
