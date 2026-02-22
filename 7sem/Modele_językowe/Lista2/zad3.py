from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import torch.nn.functional as F


MODEL_NAME = "radlab/polish-gpt2-small"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()


def sequence_log_prob(input_ids):
    input_ids = input_ids.to(device)
    with torch.no_grad():
        outputs = model(input_ids)
    logits = outputs.logits
    log_probs = F.log_softmax(logits, dim=-1)
    seq_log_prob = 0.0
    for i in range(log_probs.size(1) - 1):
        token_id = input_ids[0, i+1]
        seq_log_prob += log_probs[0, i, token_id].item()
    return seq_log_prob


def beam_search_disambiguation(variants_list, beam_size=3):
    beam = [([], 0.0)]

    for variants in variants_list:
        candidates = []
        for prefix_words, _ in beam:
            prefix_text = " ".join(prefix_words)
            for word in variants:
                new_text = (prefix_text + " " + word).strip()
                input_ids = tokenizer.encode(new_text, return_tensors="pt")
                logprob = sequence_log_prob(input_ids)
                candidates.append((prefix_words + [word], logprob))
        candidates = sorted(candidates, key=lambda x: x[1], reverse=True)[:beam_size]
        beam = candidates

    best_sequence, best_logprob = beam[0]
    return best_sequence, best_logprob


texts = [
    (
        "wprost|wyprosty|wyprostu|wyprost "
        "uwielbiała|wielbił|wielbiła|uwielbił|wielbiło|uwielbiał|uwielbiało|uwielbiały "
        "słuchać|osłuchać|słychać|usłuchać "
        "o|i|e|a|ó|ę|y|ą|u "
        "wartościach|wartość|warto|niewarto "
        "własnych|owłosionych|włos|właśnie "
        "macierzy|mocarz|macierzą|macierze|mocarza|mocarze|mocarzy|macierz"
        
    ),
    (
        "długo|bardzo|dawno|dalej|dalejże|dłoń|dłonią|dłonię|dłońmi|dłońmi "
        "pamiętał|pamiętała|pamiętali|pamiętały|pamiętałby|pamiętałbym "
        "człowieka|człowiekiem|człowieka|człowieka|człowieka|człowiekiem "
        "który|która|które|którego|któremu|której|którymi|któryż|któryś "
        "odszedł|odeszli|odeszło|przeszło|odchodzić"
    ),
    (
        "piękny|piękna|piękne|pięknego|pięknej|piękniejszy|piękniejsza|piękniejsze "
        "dom|domu|domem|domach|domy|domów|domami "
        "z|za|obok|przy|zza|nad|pod|stąd "
        "zielonym|zielona|zielone|zieloni|zielony|zielonych "
        "ogrodem|ogród|ogrodzie|ogrodu|ogrody|ogrodów|ogrodami"
    ),
]
splitted_texts = [[elem.split('|') for elem in text.split(' ')] for text in texts]

for text in splitted_texts:
    best_sequence, best_score = beam_search_disambiguation(text, beam_size=5)
    print("Najlepsza sekwencja wariantów:", best_sequence)
    print("Z log-probability:", best_score)
