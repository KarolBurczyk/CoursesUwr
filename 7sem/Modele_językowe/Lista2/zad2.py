import torch
import random
from collections import defaultdict
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "radlab/polish-gpt2-small"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

queries = [
    "Jestem królem szachownicy, ruszam się po przekątnej. Kim jestem?",
    "Mam cztery nogi, ale nie umiem chodzić. Co to jest?",
    "Co to jest: ma zęby, ale nie gryzie?",
    "Co jest zawsze przed tobą, ale nigdy nie możesz tego zobaczyć?",
    "Co to za rzecz, która ma wiele kluczy, ale nie może otworzyć żadnych drzwi?",
    "Co rośnie, gdy się je ścina?",
    "Co to jest: chodzi po niebie, ale nigdy nie spadnie?",
    "Co to jest: daje światło, ale nie jest słońcem?",
    "Jestem biały, ale nie śnieg, mam skrzydła, ale nie jestem ptakiem. Co to jest?",
    "Co to jest: ma ręce i nogi, ale nie żyje?"
]

answers = [
    "hetman",      # król szachownicy ruszający po przekątnej
    "stół",        # cztery nogi, ale nie chodzi
    "grzebień",    # ma zęby, nie gryzie
    "przyszłość",  # zawsze przed tobą, niewidzialna
    "fortepian",   # wiele kluczy, ale nie otwiera drzwi
    "włosy",       # rośnie, gdy się je ścina
    "chmura",      # chodzi po niebie, nie spada
    "latarnia",    # daje światło, nie słońce
    "ptak",        # biały, ma skrzydła
    "lalka",        # ma ręce i nogi, nie żyje
]

allowed_words = list(set(answers))

word2tok_ids = {}
for w in allowed_words:
    token_ids = tokenizer(w, add_special_tokens=False).input_ids
    if len(token_ids) > 0:
        word2tok_ids[w] = token_ids

prefix2words = defaultdict(set)
next_token_allowed = defaultdict(set)
for w, ids in word2tok_ids.items():
    for k in range(1, len(ids)+1):
        prefix = tuple(ids[:k])
        prefix2words[prefix].add(w)
    for k in range(len(ids)-1):
        prefix = tuple(ids[:k+1])
        next_token_allowed[prefix].add(ids[k+1])

start_allowed = set(ids[0] for ids in word2tok_ids.values())


def generate_one_word_from_set(prompt, max_new_tokens, num_samples):
    model.eval()
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)
    batch_size = num_samples
    input_ids = input_ids.repeat(batch_size, 1)
    finished = [None] * batch_size
    prefix_tokens = [tuple() for _ in range(batch_size)]

    with torch.no_grad():
        for step in range(max_new_tokens):
            outputs = model(input_ids=input_ids)
            logits = outputs.logits[:, -1, :]
            for i in range(batch_size):
                if finished[i] is not None:
                    logits[i, :] = -1e9
                    logits[i, tokenizer.eos_token_id] = 0
                    continue
                if len(prefix_tokens[i]) == 0:
                    allowed_next = start_allowed
                else:
                    allowed_next = next_token_allowed.get(prefix_tokens[i], set())
                if not allowed_next:
                    logits[i, :] = -1e9
                    logits[i, tokenizer.eos_token_id] = 0
                    continue
                mask = torch.full_like(logits[i], -1e9)
                mask[list(allowed_next)] = 0.0
                logits[i] = logits[i] + mask
            probs = torch.softmax(logits, dim=-1)
            next_tokens = torch.multinomial(probs, num_samples=1).squeeze(-1)
            input_ids = torch.cat([input_ids, next_tokens.unsqueeze(-1)], dim=-1)
            for i in range(batch_size):
                if finished[i] is not None:
                    continue
                t = int(next_tokens[i].item())
                prefix_tokens[i] = prefix_tokens[i] + (t,)
                words_for_prefix = prefix2words.get(prefix_tokens[i], set())
                if words_for_prefix:
                    finished[i] = next(iter(words_for_prefix))
    candidates = [w for w in finished if w is not None]
    seen = set()
    unique = []
    for w in candidates:
        if w not in seen:
            seen.add(w)
            unique.append(w)
    return unique


def mean_reciprocal_rank(real_answers, computed_answers, K=5):
    mrr = 0
    n = len(real_answers)
    for real, preds in zip(real_answers, computed_answers):
        rank = 0
        for i, p in enumerate(preds):
            if p == real:
                rank = i + 1
                break
        if rank > 0:
            mrr += 1 / rank
    return mrr / n if n > 0 else 0


def eval_model_on_riddles(K=5):
    computed = []
    qs = queries
    asw = answers
    for q in qs:
        prompt = f"Zagadka: {q}\nOdpowiedź:"
        words = generate_one_word_from_set(prompt, 6, K*2)
        computed.append(words[:K])
    acc = mean_reciprocal_rank(asw, computed, K=K)
    print(f"MRR@{K} na {len(computed)} zagadkach: {acc:.4f}")


eval_model_on_riddles(K=5)
