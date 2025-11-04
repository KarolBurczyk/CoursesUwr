import torch
import re
from transformers import AutoModelForCausalLM, AutoTokenizer
import random


MODEL_NAME = "radlab/polish-gpt2-small"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


def get_prompt(problem):
    return f"""Zadanie: oblicz wynik działania.
        1 + 1 = 2
        2 + 3 = 5
        4 + 5 = 9
        6 + 9 = 15
        1 + 7 = 8
        9 + 3 = 12
        3 + 3 = 6
        4 + 4 = 8
        9 + 9 = 18
        {problem} = 
"""


def generate_problem():
    a, b = random.randint(1, 10), random.randint(1, 10)
    return f"{a} + {b}", a + b


def calculate_sequence_probability(full_text):
    """Oblicza prawdopodobieństwo sekwencji (log-probability)"""
    model.eval()
    inputs = tokenizer(full_text, return_tensors="pt").to(device)
    
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs.input_ids)
        # Niższa strata (loss) = wyższe prawdopodobieństwo
        neg_log_likelihood = outputs.loss.item()
    
    return -neg_log_likelihood  # Zwracamy ujemną stratę (wyższe = lepsze)


def extract_answer(decoded_text):
    """Wyciąga liczbę bezpośrednio po znaku ="""
    # Szukaj liczby po spacji lub bezpośrednio
    match = re.search(r'^\s*(\d+)', decoded_text)
    return int(match.group(1)) if match else None


def predict(problem):
    input_text = get_prompt(problem)
    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    
    # Generuj więcej sekwencji z beam search
    outputs = model.generate(
        **inputs,
        max_new_tokens=10,  # Zamiast max_length
        num_beams=5,  # Beam search zamiast sampling
        num_return_sequences=5,
        early_stopping=True,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )
    
    # Zbieramy wszystkie odpowiedzi i ich prawdopodobieństwa
    candidates = []
    
    for output in outputs:
        decoded = tokenizer.decode(output[inputs.input_ids.shape[1]:], skip_special_tokens=True)
        answer = extract_answer(decoded)
        
        if answer is not None:
            # Obliczamy prawdopodobieństwo pełnej sekwencji (prompt + odpowiedź)
            full_text = input_text + str(answer)
            prob = calculate_sequence_probability(full_text)
            
            candidates.append({
                'answer': answer,
                'probability': prob,
                'decoded': decoded
            })
    
    # Jeśli nie udało się wyciągnąć żadnej liczby, zwróć None
    if not candidates:
        return None
    
    # Wybieramy odpowiedź z najwyższym prawdopodobieństwem
    best_candidate = max(candidates, key=lambda x: x['probability'])
    
    return best_candidate['answer'], best_candidate['decoded']


def run_tests(num_tests=20):
    correct = 0
    
    for i in range(num_tests):
        problem, answer = generate_problem()
        pred, undecoded = predict(problem)
        print(f"Problem: {problem}, Result: {pred}, Expected:{answer}, Undecoded: {undecoded}")
        if pred == answer:
            correct += 1
    
    print(f"Dokładność modelu na {num_tests} próbach: {correct/num_tests:.2%}")


if __name__ == "__main__":
    run_tests()
