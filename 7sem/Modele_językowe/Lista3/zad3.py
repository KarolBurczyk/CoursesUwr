import torch
import numpy as np
from transformers import AutoTokenizer, AutoModel
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import random
import re
import os

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model_name = "allegro/herbert-base-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name).to(device)

def load_data(filename='reviews.txt'):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('GOOD') or line.startswith('BAD'):
                lines.append(line)
    random.shuffle(lines)
    N = len(lines)
    test_size = N // 4
    return lines[:N-test_size], lines[N-test_size:]

def split_label_text(line):
    if line.startswith('GOOD'):
        return 1, line[4:].strip()
    elif line.startswith('BAD'):
        return 0, line[3:].strip()
    else:
        return None, None

def herbert_features(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, max_length=256).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[0, 0, :].cpu().numpy()

def features_and_labels_from_lines(lines):
    X, y = [], []
    for line in lines:
        label, text = split_label_text(line)
        if label is None or not text:
            continue
        X.append(herbert_features(text))
        y.append(label)
    return np.array(X), np.array(y)

def train_test_baseline(train_lines, test_lines):
    X_train, y_train = features_and_labels_from_lines(train_lines)
    X_test, y_test = features_and_labels_from_lines(test_lines)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    clf = LogisticRegression(random_state=42, max_iter=1000)
    clf.fit(X_train_scaled, y_train)
    acc = accuracy_score(y_test, clf.predict(X_test_scaled))

    print(f"baseline test accuracy: {acc:.4f}")
    return acc
