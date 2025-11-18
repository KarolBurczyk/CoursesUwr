from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import torch.nn.functional as F
import re

MODEL_NAME = "radlab/polish-gpt2-small"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

def filter_logits(logits, top_k=0, top_p=0.0):
    """Modyfikacja rozkładu logits: top-k i top-p"""
    logits = logits.squeeze(0)
    sorted_logits, sorted_indices = torch.sort(logits, descending=True)
    cumulative_probs = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)
    
    # top-p filter
    if top_p > 0.0:
        sorted_indices_to_remove = cumulative_probs > top_p
        if sorted_indices_to_remove[0]:
            sorted_indices_to_remove[0] = False
        indices_to_remove = sorted_indices[sorted_indices_to_remove]
        logits[indices_to_remove] = -float('Inf')
    
    # top-k filter
    if top_k > 0:
        indices_to_remove = sorted_indices[top_k:]
        logits[indices_to_remove] = -float('Inf')
    
    return logits.unsqueeze(0)

def generate_sentence_with_letter(prefix, letter, max_length=50, top_k=50, top_p=0.9, num_return_sequences=5):
    """
    Generuje zdania zaczynające się od liter z prefixu oraz słowa zaczynające się na `letter`.
    Generuje kilk wariantów, wybiera najlepszy wg średniej log-wiarygodności.
    """
    def clean_text(text):
        # Poprawna spacja i interpunkcja
        text = re.sub(r'\s+([,.!?])', r'\1', text)
        return text.strip()
    
    best_sentence = None
    best_score = -float('inf')
    
    prefix_ids = tokenizer.encode(prefix, return_tensors='pt').to(device)

    for _ in range(num_return_sequences):
        generated = prefix_ids
        past_words = set(prefix.lower().split())
        generated_sentence = prefix
        total_log_prob = 0.0
        word_count = 0
        
        while word_count < max_length:
            outputs = model(generated)
            next_token_logits = outputs.logits[:, -1, :]

            # Ograniczenie tokenów do tych, które zaczynają się na literę `letter` lub są interpunkcją / spacją
            filtered_logits = next_token_logits.clone()
            allowed_token_ids = []
            
            for token_id in range(filtered_logits.size(-1)):
                token_str = tokenizer.decode([token_id]).strip()
                if token_str == '':
                    continue
                # Dozwolone interpunkcje, spacje itp.
                if re.match(r'^[ ,.!?]$', token_str):
                    allowed_token_ids.append(token_id)
                # Słowa zaczynające się od litery letter (uwzględniając wielkość i małe litery)
                # lub tokeny rozpoczynające nowy wordpiece z literą letter
                elif token_str[0].lower() == letter.lower():
                    allowed_token_ids.append(token_id)
            # Ustaw maskę dla pozostałych tokenów na -inf
            mask = torch.full_like(filtered_logits, -float('Inf'))
            mask[:, allowed_token_ids] = filtered_logits[:, allowed_token_ids]
            filtered_logits = mask
            
            # Zastosuj top-k i top-p
            filtered_logits = filter_logits(filtered_logits, top_k=top_k, top_p=top_p)
            probs = F.softmax(filtered_logits, dim=-1)
            next_token = torch.multinomial(probs, num_samples=1)

            # Dodaj token i aktualizuj tekst
            generated = torch.cat((generated, next_token), dim=1)
            next_token_str = tokenizer.decode(next_token[0]).replace('Ġ', ' ').strip()
            
            # Unikaj powtórzeń słów
            normalized_word = next_token_str.lower()
            if normalized_word in past_words:
                break
            if next_token_str in ['.', '?', '!']:
                generated_sentence += next_token_str
                break
            if next_token_str != '':
                generated_sentence += ' ' + next_token_str
                past_words.add(normalized_word)
                word_count += 1
            
            # Sumuj log-prawdopodobieństwo
            token_log_prob = torch.log(probs[0, next_token])
            total_log_prob += token_log_prob.item()

        # Ocena jakości: średnie log-prawdopodobieństwo
        avg_log_prob = total_log_prob / (word_count if word_count>0 else 1)
        cleaned = clean_text(generated_sentence)
        print(cleaned)
        if avg_log_prob > best_score:
            best_score = avg_log_prob
            best_sentence = cleaned

    return best_sentence, best_score

# Przykład użycia dla prefiksu i litery
prefix = "Prawdziwy piekarz przyprawia pieczywo pieprzem"
letter = 'p'

sentence, score = generate_sentence_with_letter(prefix, letter)
print(f"Najlepsze zdanie: {sentence}")
print(f"Z oceną (średnie log-prawdopodobieństwo): {score}")
