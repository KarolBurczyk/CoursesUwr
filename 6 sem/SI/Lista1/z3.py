# W moim rozwiązaniu dla obydwu graczy z tablic, które są globalnymi zmiennymi losuję po 5 kart, a następnie 
# wyliczam wartość ręki. Liczby przypisane do konkretnych układów są zgodne z ich wartościami po kolei. 
# Blotkarz musi mieć większą wartość ręki, bo jeżeli mają taki sam układ, to figurarz zawsze wygra, bo ma 
# karty o wyższych wagach. Na koniec wyliczam procent wygranych blotkarza.

import random
from collections import Counter

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
                   '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

f_deck = [
    ("A", "♥"), ("A", "♦"), ("A", "♣"), ("A", "♠"),
    ("K", "♥"), ("K", "♦"), ("K", "♣"), ("K", "♠"),
    ("Q", "♥"), ("Q", "♦"), ("Q", "♣"), ("Q", "♠"),
    ("J", "♥"), ("J", "♦"), ("J", "♣"), ("J", "♠")
]

b_deck = [
    ("10", "♥"), ("10", "♦"), ("10", "♣"), ("10", "♠"),
    ("9", "♥"), ("9", "♦"), ("9", "♣"), ("9", "♠"),
    ("8", "♥"), ("8", "♦"), ("8", "♣"), ("8", "♠"),
    ("7", "♥"), ("7", "♦"), ("7", "♣"), ("7", "♠"),
    ("6", "♥"), ("6", "♦"), ("6", "♣"), ("6", "♠"),
    ("5", "♥"), ("5", "♦"), ("5", "♣"), ("5", "♠"),
    ("4", "♥"), ("4", "♦"), ("4", "♣"), ("4", "♠"),
    ("3", "♥"), ("3", "♦"), ("3", "♣"), ("3", "♠"),
    ("2", "♥"), ("2", "♦"), ("2", "♣"), ("2", "♠")
]

# b_deck = [
#     ("10", "♥"), ("10", "♦"),
#     ("9", "♥"), ("9", "♦"),
#     ("8", "♥"), ("8", "♦"),
#     ("7", "♥"), ("7", "♦"),
#     ("6", "♥"), ("6", "♦"),
#     ("5", "♥"), ("5", "♦"),
#     ("4", "♥"), ("4", "♦"),
#     ("3", "♥"), ("3", "♦"),
#     ("2", "♥"), ("2", "♦")
# ]

# b_deck = [
#     ("10", "♥"), ("10", "♦"), ("10", "♣"), ("10", "♠"),
#     ("9", "♥"), ("9", "♦"), ("9", "♣"), ("9", "♠"),
#     ("8", "♥"), ("8", "♦"), ("8", "♣"), ("8", "♠"),
# ]

def is_flush(hand):
    suits = [suit for _, suit in hand]
    return len(set(suits)) == 1


def is_straight(hand):
    values = sorted([card_values[value] for value, _ in hand])
    return values == list(range(values[0], values[0] + 5))

def evaluate_hand(hand):
    values = [card_values[value] for value, _ in hand]
    count_values = Counter(values)

    if is_flush(hand) and is_straight(hand): return 8
    if sorted(count_values.values()) == [1, 4]: return 7
    if sorted(count_values.values()) == [2, 3]: return 6
    if is_flush(hand): return 5
    if is_straight(hand): return 4
    if sorted(count_values.values()) == [1, 1, 3]: return 3
    if sorted(count_values.values()) == [1, 2, 2]: return 2
    if sorted(count_values.values()) == [1, 1, 1, 2]: return 1
    else: return 0

def generate_games(n):
    win_counter = 0
    for i in range(n):
        b_hand = random.sample(b_deck, 5)
        f_hand = random.sample(f_deck, 5)
        if evaluate_hand(b_hand) > evaluate_hand(f_hand):
            win_counter += 1
    return str(round(win_counter/n*100, 2)) + "% wygranych blotkarza"

if __name__ == '__main__':
    print(generate_games(10000))
