import random

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


model_name = "radlab/polish-gpt2-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

expected = []
reviews = []
with open("reviews.txt", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file if line.strip()]
    random.shuffle(lines)
    for line in lines:
        striped_line = line.strip().split(';')
        expected.append(striped_line[0])
        reviews.append(striped_line[1])

def sentence_logprob(text):
    inputs = tokenizer(text, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
    return -outputs.loss.item()

def classify_sentiment(review):
    patterns = [
        f"{review} To pozytywna opinia.",
        f"{review} To negatywna opinia.",
        f"Opinie takie jak: {review} są pozytywne.",
        f"Opinie takie jak: {review} są negatywne.",
        f"{review} jest pozytywną opinią.",
        f"{review} jest negatywną opinią.",
        f"{review} brzmi pozytywnie",
        f"{review} brzmi negatywnie"
    ]

    scores = [sentence_logprob(t) for t in patterns]
    positive_score = max(scores[0], scores[2], scores[4], scores[6])
    negative_score = max(scores[1], scores[3], scores[5], scores[7])

    label = "POSITIVE" if positive_score > negative_score else "NEGATIVE"
    return label

correct = 0
total = len(reviews)

for opinia, expected in zip(reviews, expected):
    label = classify_sentiment(opinia)
    result = "CORRECT" if label == expected else "WRONG"
    print(f"{opinia} → {label} (expected: {expected}) {result}")
    if label == expected:
        correct += 1

print(f"\nAccuracy: {correct/total*100:.1f}%")
