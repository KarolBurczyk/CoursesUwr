from itertools import permutations
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


model_name = "radlab/polish-gpt2-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def score_sentence(sentence):
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
    loss = outputs.loss.item()
    return -loss

def capitalize_first_word(sentence):
    words = sentence.split()
    if words:
        words[0] = words[0].capitalize()
    return " ".join(words)

def generate_sentences(words):
    results = []
    for perm in permutations(words):
        sentence = " ".join(perm) + "."
        sentence = capitalize_first_word(sentence)
        score = score_sentence(sentence)
        results.append((sentence, score))

    results = list(set(results))
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:5]

sentences = [
    ["babuleńka", "miała", "dwa", "rogate", "koziołki"],
    ["wiewiórki", "w", "parku", "zaczepiają", "przechodniów"],
    ["chrząszcz", "brzmi", "w", "trzcinie", "w", "Szczebrzeszynie"]
]

for sentence in sentences:
    best_sentences = generate_sentences(sentence)
    for sent, score in best_sentences:
        print(f"{sent} (score: {score:.4f})")
