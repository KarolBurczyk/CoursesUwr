# W rozwiązaniu zastosowałem tabelę dp, która na i-tej pozycji zawira najepszy możliwy podział pod względem wyniku.
# Za pomocą dwóch pętli for sprawdzam czy słowo złożone z liter od j do i istnieje, jeżeli tak to sprawdzam czy 
# istnieje podział od 0 do j, jeżeli tak to porównuję ewentualną sumę wyników (od 0 do j + od j do i) z wartością 
# zawartą w i-tej komórce. Jeżeli jest większa to następuje zamiana.

import gzip

def load_word_list():
    words = set()
    with gzip.open('zad2_words.txt.gz', 'rb') as gf:
        for line in gf:
            line = line.strip().decode('utf-8')
            if line:
                words.add(line)
    return words

def best_split(text, word_list):
    n = len(text)
    dp = [None] * (n + 1)
    dp[0] = (0, [])

    for i in range(1, n + 1):
        for j in range(i):
            word = text[j:i]
            if word in word_list:
                score = len(word) ** 2
                if dp[j] is not None:
                    current_score = dp[j][0] + score
                    if dp[i] is None or current_score > dp[i][0]:
                        dp[i] = (current_score, dp[j][1] + [word])

    if dp[n] is not None:
        return ' '.join(dp[n][1])
    else:
        return ""

def process_input_file(input_file, output_file, word_list):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            line = line.strip()
            if line:
                result = best_split(line, word_list)
                outfile.write(result + "\n")

if __name__ == '__main__':
    word_list = load_word_list()
    process_input_file('zad2_input.txt', 'zad2_output.txt', word_list)
