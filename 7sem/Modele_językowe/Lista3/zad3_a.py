from zad3 import *
import random
import re

K = 3

def mechanical_augment(text, K=3):
    aug_texts = []
    for _ in range(K):
        words = text.split()
        new_words = []
        for w in words:
            r = random.random()
            if r < 0.15:
                new_words.append(w.upper())
            elif r < 0.25 and len(w) > 3:
                pos = random.randint(1, len(w)-2)
                new_char = random.choice('aąbcćdeęfghijklłmnńoóprsśtuwyzźż')
                new_words.append(w[:pos] + new_char + w[pos+1:])
            elif r < 0.33:
                repl = {'ą':'a','ę':'e','ó':'o','ś':'s','ł':'l','ż':'z','ź':'z','ć':'c','ń':'n'}
                new_w = ''.join(repl.get(ch, ch) for ch in w)
                new_words.append(new_w)
            else:
                new_words.append(w)
        aug_texts.append(' '.join(new_words))
    return aug_texts

train_lines, test_lines = load_data('reviews.txt')

base_acc = train_test_baseline(train_lines, test_lines)

aug_lines = []
for line in train_lines:
    label, text = split_label_text(line)
    if label is None or not text:
        continue
    aug_lines.append(line)
    new_texts = mechanical_augment(text, K=K)
    for t in new_texts:
        prefix = "GOOD" if label == 1 else "BAD"
        aug_lines.append(f"{prefix} {t}")

with open('reviews_aug_mech.txt', 'w', encoding='utf-8') as f:
    for l in aug_lines:
        f.write(l + "\n")

X_train, y_train = features_and_labels_from_lines(aug_lines)
X_test, y_test = features_and_labels_from_lines(test_lines)

clf = LogisticRegression(random_state=42, max_iter=1000)
clf.fit(X_train, y_train)
acc = accuracy_score(y_test, clf.predict(X_test))

print(f"augmented test accuracy: {acc:.4f}")
print(f"gain vs baseline: {acc - base_acc:.4f}")
