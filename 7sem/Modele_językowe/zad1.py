import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "flax-community/papuGaPT2"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

max_length = 50
num_return_sequences = 3

default_prompt = """
    Jesteś mechanikiem samochodowym w małym warsztacie w polsce
    Klient: Dzień dobry, mój samochód zaczął dziwnie stukać podczas jazdy.
    Mechanik: Może Pan pokazać, kiedy pojawia się ten dźwięk?
    Klient: Najczęściej przy skręcaniu w lewo.
    Mechanik: Sprawdzimy przeguby i zawieszenie. Proszę zostawić auto na godzinę.
    Klient: Słyszałem, że coś szumi z tylnego koła, co to może być?
    Mechanik: To może być uszkodzone łożysko. Zdejmę koło i zobaczę, czy rzeczywiście wymaga wymiany.
    Klient: Ile potrwa naprawa?
    Mechanik: Jeśli to tylko łożysko, powinno nam wystarczyć dwie godziny.
    Klient: Dzień dobry, samochód nie chce odpalić od wczoraj.
    Mechanik: Czy słychać, że kręci rozrusznik?
    Klient: Tak, ale nie łapie.
    Mechanik: Może to być akumulator albo problem z układem paliwowym. Zmierzę napięcie, potem sprawdzimy dalej.
    Klient: Proszę pana, ile będzie kosztować wymiana rozrządu?
    Mechanik: W tym modelu rozrząd kosztuje około 800 złotych z robocizną.
    Klient: Czy muszę też wymienić pompę wody?
    Mechanik: Zalecam wymianę razem z rozrządem, wtedy oszczędzi Pan na dodatkowej pracy w przyszłości.
    Klient: Czy mogę liczyć na naprawę dziś do wieczora?
    Mechanik: Postaram się, ale najpierw sprawdzę, czy mamy części na miejscu. Jeśli tak, naprawa powinna być gotowa około godziny 17:00.
"""

dialog_history = []

def make_prompt(history, user_input):
    prompt = default_prompt
    for i, (user_turn, bot_turn) in enumerate(history[-3:]):
        prompt += f"Użytkownik: {user_turn}\nBot: {bot_turn}\n"
    prompt += f"Użytkownik: {user_input}\nBot:"
    return prompt

def log_probs_from_logits(logits, labels):
    log_probs = torch.nn.functional.log_softmax(logits, dim=-1)
    selected_log_probs = torch.gather(log_probs, index=labels.unsqueeze(-1), dim=-1).squeeze(-1)
    return selected_log_probs

def sentence_prob(sentence_txt):
    model.eval()
    input_ids = tokenizer(sentence_txt, return_tensors='pt')['input_ids'].to(device)
    with torch.no_grad():
        output = model(input_ids=input_ids)
        log_probs = log_probs_from_logits(output.logits[:, :-1, :], input_ids[:, 1:])
        seq_log_probs = torch.sum(log_probs)
    return seq_log_probs.cpu().item()

def select_best_response(responses, prompt_prefix):

    scored = []

    for r in responses:
        full_text = prompt_prefix + r
        score = sentence_prob(full_text)
        scored.append((r, score))

    best_response = max(scored, key=lambda x: x[1])[0]
    return best_response

def chatbot_respond(user_input):
    global dialog_history

    prompt = make_prompt(dialog_history, user_input)
    input_encoding = tokenizer(prompt, return_tensors="pt", return_attention_mask=True)
    input_ids = input_encoding["input_ids"].to(device)
    attention_mask = input_encoding["attention_mask"].to(device)

    outputs = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_length=input_ids.shape[1] + max_length,
        do_sample=True,
        top_p=0.9,
        num_return_sequences=num_return_sequences,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

    responses = []
    for output in outputs:
        decoded = tokenizer.decode(output[input_ids.shape[1]:], skip_special_tokens=True)
        cutoff_pos = len(decoded)
        for sep in ['\n', '.']:
            pos = decoded.find(sep)
            if pos != -1 and pos < cutoff_pos:
                cutoff_pos = pos + 1 if sep == '.' else pos
        short_response = decoded[:cutoff_pos].strip()
        responses.append(short_response)

    best_response = select_best_response(responses, prompt)

    dialog_history.append((user_input, best_response))
    return best_response

if __name__ == "__main__":
    while True:
        user_text = input("You: ")
        reply = chatbot_respond(user_text)
        print(f"Bot: {reply}")
