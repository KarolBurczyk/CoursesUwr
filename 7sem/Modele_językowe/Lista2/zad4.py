from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import re

MODEL_NAME = "radlab/polish-gpt2-small"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

def generate_sentence_with_letter(prefix, letter, max_words=5, block_tokens=5, top_k=50, top_p=0.9, num_return_sequences=5):
    def clean_text(text):
        text = re.sub(r'\s+([,.!?])', r'\1', text)
        return text.strip()
    
    best_sentence = None
    best_score = -float('inf')
    past_words = set(prefix.lower().split())
    
    for _ in range(num_return_sequences):
        current_text = prefix
        generated = tokenizer.encode(current_text, return_tensors='pt').to(device)
        words_generated = 0

        while words_generated < max_words:
            outputs = model.generate(
                generated,
                max_new_tokens=block_tokens,
                do_sample=True,
                top_k=top_k,
                top_p=top_p,
                pad_token_id=tokenizer.eos_token_id,
                eos_token_id=tokenizer.eos_token_id
            )
            new_text = tokenizer.decode(outputs[0][generated.shape[-1]:])
            for match in re.finditer(r'\b\w+\b', new_text):
                word = match.group()
                if word.lower().startswith(letter.lower()) and word.lower() not in past_words:
                    current_text += ' ' + word.lower()
                    past_words.add(word.lower())
                    words_generated += 1
                    if words_generated >= max_words:
                        break
            if re.search(r'[.!?]', new_text):
                current_text += re.search(r'[.!?]', new_text).group()
                break
            generated = tokenizer.encode(current_text, return_tensors='pt').to(device)

        cleaned = clean_text(current_text)
        print(cleaned)
        if words_generated > best_score:
            best_score = words_generated
            best_sentence = cleaned

    if not best_sentence.endswith('.'):
        best_sentence = best_sentence + '.'
    return best_sentence, best_score

prefix = "Prawdziwy piekarz przyprawia pieczywo"
letter = 'p'

sentence, score = generate_sentence_with_letter(prefix, letter)
print(f"Najlepsze zdanie: {sentence}")
print(f"Z oceną (średnie log-probability): {score}")
