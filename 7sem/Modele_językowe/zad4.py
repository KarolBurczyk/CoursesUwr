import random
import re

import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "eryk-mazus/polka-1.1b-chat"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

def classify_1_or_2(question, odpowiedz1, odpowiedz2):
    patterns = [
        f"Pytanie: {question}, Odpowiedź: {odpowiedz1}",
        f"Pytanie: {question}, Odpowiedź: {odpowiedz2}"
    ]

    scores = [sentence_logprob(t) for t in patterns]
    first_score, second_score = scores

    if first_score > second_score:
        return odpowiedz1
    else:
        return odpowiedz2

def heuristic_yes_no_question(question):
    for i, elem in enumerate(question):
        if elem == "czy":
            if i + 1 < len(question):
                options = [re.sub(r'[^\w\s]', '', question[i - 1]), re.sub(r'[^\w\s]', '', question[i + 1])]
                return classify_1_or_2(question, options[0], options[1])
            else:
                return question[i - 1]
    return "Zielony"

def model_generate_answer(question, max_length=15):
    prompt = f"Pytanie: {question}\nOdpowiedź:"
    inputs = tokenizer(prompt, return_tensors="pt", padding=True).to(device)

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    with torch.no_grad():
        outputs = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=inputs["input_ids"].shape[1] + max_length,
            num_beams=1,
            no_repeat_ngram_size=2,
            do_sample=False,
            pad_token_id=tokenizer.pad_token_id,
        )
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    answer = generated_text[len(prompt):].strip()
    answer = answer.split('\n')[0].split('.')[0].strip()
    return answer

def sentence_logprob(text):
    inputs = tokenizer(text, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
    return -outputs.loss.item()


def main():
    questions = [q.strip() for q in open("small_questions.txt", encoding="utf-8")]
    found_answers = []

    for q in tqdm(questions, "Questions processing"):
        split_question = q.lower().split(' ')
        if split_question[0] == "czy":
            if "czy" in split_question[1:]:
                found_answers.append(heuristic_yes_no_question(split_question[1:]))
            else:
                found_answers.append(classify_1_or_2(q, "tak", "nie"))
        elif "czy" in split_question[1:]:
            found_answers.append(heuristic_yes_no_question(split_question))
        else:
            pred = model_generate_answer(q)
            found_answers.append(pred)

    with open("found_answers_2.txt", "w", encoding="utf-8") as f:
        for answer in found_answers:
            f.write(answer + "\n")

if __name__ == "__main__":
    main()
