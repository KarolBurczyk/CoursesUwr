import torch
import numpy as np
from transformers import AutoTokenizer, AutoModel, AutoModelForCausalLM
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import random

def load_data(filename='reviews.txt'):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and ('GOOD' in line or 'BAD' in line):
                lines.append(line)
    
    random.shuffle(lines)
    N = len(lines)
    test_size = N // 4
    train_size = N - test_size
    
    train_lines = lines[:train_size]
    test_lines = lines[train_size:]
    return train_lines, test_lines

train_lines, test_lines = load_data()

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model_herbert_name = "allegro/herbert-base-cased"
tokenizer_herbert = AutoTokenizer.from_pretrained(model_herbert_name)
model_herbert = AutoModel.from_pretrained(model_herbert_name).to(device)

model_papuga_name = "flax-community/papuGaPT2"
tokenizer_papuga = AutoTokenizer.from_pretrained(model_papuga_name)
model_papuga = AutoModelForCausalLM.from_pretrained(model_papuga_name).to(device)

def herbert_representation(text):
    inputs = tokenizer_herbert(text, return_tensors='pt', truncation=True, max_length=512).to(device)
    with torch.no_grad():
        outputs = model_herbert(**inputs)
    return outputs.last_hidden_state[0, 0, :].detach().cpu().numpy()

def papuga_score(text):
    pos_prompt = f"{text} Świetny produkt!"
    neg_prompt = f"{text} Bardzo słaby produkt."
    
    pos_inputs = tokenizer_papuga(pos_prompt, return_tensors='pt', truncation=True).to(device)
    neg_inputs = tokenizer_papuga(neg_prompt, return_tensors='pt', truncation=True).to(device)
    
    with torch.no_grad():
        pos_logits = model_papuga(**pos_inputs).logits[0, -2:, :]
        neg_logits = model_papuga(**neg_inputs).logits[0, -2:, :]
    
    pos_prob = torch.softmax(pos_logits, dim=-1).mean().cpu().numpy()
    neg_prob = torch.softmax(neg_logits, dim=-1).mean().cpu().numpy()
    
    return float(pos_prob - neg_prob)

def augment(text, p=0.15):
    words = text.split()
    augmented_words = []
    for word in words:
        if random.random() < p:
            augmented_words.append(word.upper())
        else:
            augmented_words.append(word)
    return ' '.join(augmented_words)

def extract_features(lines):
    X, y = [], []
    for line in lines:
        if line.startswith('GOOD'):
            label, text = 'GOOD', line[4:].strip()
            y_val = 1
        elif line.startswith('BAD'):
            label, text = 'BAD', line[3:].strip()
            y_val = 0
        else:
            continue
        
        if not text:
            continue

        herbert_feat = herbert_representation(text)
        papuga_feat = papuga_score(text)
        features = np.concatenate([herbert_feat, [papuga_feat]])
        X.append(features)
        y.append(y_val)

        for _ in range(3):
            augmented_text = text
            herbert_augmented = herbert_representation(augmented_text)
            papuga_augmented = papuga_score(augmented_text)
            features_augmented = np.concatenate([herbert_augmented, [papuga_augmented]])
            X.append(features_augmented)
            y.append(y_val)
    
    return np.array(X), np.array(y)

X_train, y_train = extract_features(train_lines)
X_test, y_test = extract_features(test_lines)


clf_lr = LogisticRegression(random_state=42, max_iter=2000, C=0.5)
clf_lr.fit(X_train, y_train)
lr_train_acc = accuracy_score(y_train, clf_lr.predict(X_train))
lr_test_acc = accuracy_score(y_test, clf_lr.predict(X_test))

clf_rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=15,
    min_samples_split=10,
    random_state=42,
    n_jobs=-1
)
clf_rf.fit(X_train, y_train)
rf_train_acc = accuracy_score(y_train, clf_rf.predict(X_train))
rf_test_acc = accuracy_score(y_test, clf_rf.predict(X_test))

print("Score:")
print(f"LogisticRegression: train={lr_train_acc:.4f}, test={lr_test_acc:.4f}")
print(f"RandomForest:      train={rf_train_acc:.4f}, test={rf_test_acc:.4f}")

best_acc = max(lr_test_acc, rf_test_acc)
print(f"Best: {best_acc:.4f}")
