import torch
import numpy as np
from transformers import AutoTokenizer, AutoModel


with open('clusters.txt', 'r', encoding='utf-8') as f:
    clusters_txt = f.read()

model_name = 'allegro/herbert-base-cased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

emb = model.embeddings.word_embeddings.weight.detach().cpu().numpy()


def get_word_embedding(word):
    tokens = tokenizer.tokenize(word)
    if not tokens:
        return None
    
    token_ids = tokenizer.convert_tokens_to_ids(tokens)
    valid_ids = [tid for tid in token_ids if 0 <= tid < emb.shape[0]]
    
    if not valid_ids:
        return None
    
    vecs = emb[valid_ids]
    mean_vec = vecs.mean(axis=0)
    norm = np.linalg.norm(mean_vec)
    return mean_vec / norm if norm > 0 else None


words = set()
for line in clusters_txt.strip().split('\n'):
    if ':' in line and len(line.split(':')) > 1:
        _, word_list = line.split(':', 1)
        words.update(word_list.strip().split())

vectors = {}
missing = []
for word in sorted(words):
    vec = get_word_embedding(word)
    if vec is not None:
        vectors[word] = vec
    else:
        missing.append(word)

with open('word_embeddings_file.txt', 'w', encoding='utf-8') as f:
    for word in sorted(vectors):
        vec_str = ' '.join(f'{x:.6f}' for x in vectors[word])
        f.write(f'{word} {vec_str}\n')
