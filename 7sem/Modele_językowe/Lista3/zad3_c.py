import random
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from gensim.models import KeyedVectors

from zad3 import *

K = 2

def load_w2v_gensim(path="vectors-pl.txt", binary=False):
    w2v = KeyedVectors.load_word2vec_format(path, binary=binary)
    return w2v

def w2v_augment_one(text, w2v, K=2):
    words = text.split()
    aug_texts = []

    for _ in range(K):
        new_words = []
        for w in words:
            lw = w.lower()
            if random.random() < 0.2 and lw in w2v:
                try:
                    sims = w2v.most_similar(lw, topn=10)
                    cands = [cw for cw, s in sims if abs(len(cw) - len(lw)) <= 3]
                    if cands:
                        repl = random.choice(cands)
                        if w[0].isupper():
                            repl = repl.capitalize()
                        new_words.append(repl)
                    else:
                        new_words.append(w)
                except KeyError:
                    new_words.append(w)
            else:
                new_words.append(w)
        aug_texts.append(" ".join(new_words))

    return aug_texts

w2v = load_w2v_gensim()

train_lines, test_lines = load_data("reviews.txt")

base_acc = train_test_baseline(train_lines, test_lines)

aug_lines = []
for line in train_lines:
    label, text = split_label_text(line)
    if label is None or not text:
        continue
    aug_lines.append(line)
    for t in w2v_augment_one(text, w2v, K=K):
        prefix = "GOOD" if label == 1 else "BAD"
        aug_lines.append(f"{prefix} {t}")

with open("reviews_aug_w2v.txt", "w", encoding="utf-8") as f:
    for l in aug_lines:
        f.write(l + "\n")

X_train, y_train = features_and_labels_from_lines(aug_lines)
X_test, y_test = features_and_labels_from_lines(test_lines)

clf = LogisticRegression(random_state=42, max_iter=1000)
clf.fit(X_train, y_train)
acc = accuracy_score(y_test, clf.predict(X_test))

print(f"augmented test accuracy: {acc:.4f}")
print(f"gain vs baseline: {acc - base_acc:.4f}")
