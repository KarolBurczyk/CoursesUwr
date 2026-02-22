from zad3 import *
from transformers import AutoModelForCausalLM, AutoTokenizer


K = 2

papuga_model_name = "flax-community/papuGaPT2"
papuga_tokenizer = AutoTokenizer.from_pretrained(papuga_model_name)
papuga_model = AutoModelForCausalLM.from_pretrained(papuga_model_name).to(device)

pos_prompts = [
    "Świetny produkt.", "Bardzo polecam.", "Jestem bardzo zadowolony.",
    "To była doskonała decyzja.", "Na pewno wrócę."
]
neg_prompts = [
    "Bardzo słaby produkt.", "Nie polecam.", "Jestem bardzo zawiedziony.",
    "To była zła decyzja.", "Nigdy więcej."
]

def papuga_augment(text, label, K=2):
    prompts = pos_prompts if label == 1 else neg_prompts
    aug_texts = []
    for _ in range(K):
        prompt = random.choice(prompts)
        input_text = f"{text} {prompt}"
        inputs = papuga_tokenizer(input_text, return_tensors='pt', truncation=True, max_length=128).to(device)
        with torch.no_grad():
            outputs = papuga_model.generate(
                **inputs,
                max_new_tokens=25,
                do_sample=True,
                temperature=0.8,
                top_p=0.9,
                pad_token_id=papuga_tokenizer.eos_token_id
            )
        gen = papuga_tokenizer.decode(outputs[0], skip_special_tokens=True)
        aug_texts.append(gen)
    return aug_texts

train_lines, test_lines = load_data('reviews.txt')

base_acc = train_test_baseline(train_lines, test_lines)

aug_lines = []
for line in train_lines:
    label, text = split_label_text(line)
    if label is None or not text:
        continue
    aug_lines.append(line)
    for t in papuga_augment(text, label, K=K):
        prefix = "GOOD" if label == 1 else "BAD"
        aug_lines.append(f"{prefix} {t}")

with open('reviews_aug_papuga.txt', 'w', encoding='utf-8') as f:
    for l in aug_lines:
        f.write(l + "\n")

X_train, y_train = features_and_labels_from_lines(aug_lines)
X_test, y_test = features_and_labels_from_lines(test_lines)

clf = LogisticRegression(random_state=42, max_iter=1000)
clf.fit(X_train, y_train)
acc = accuracy_score(y_test, clf.predict(X_test))

print(f"augmented test accuracy: {acc:.4f}")
print(f"gain vs baseline: {acc - base_acc:.4f}")
