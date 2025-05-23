import numpy as np
from itertools import combinations, count

b_deck = [] # przechowujemy całą talię blotkarza
f_deck = [] # całą talię figuranta

def prepare_decks(): # przygotowanie talii
    for color in range(4):
        for number in range(2, 11): 
            b_deck.append((number, color))
        for number in range(11, 15):
            f_deck.append((number, color))
    b_deck.sort()
    f_deck.sort()

def is_straight_flush(cards): # poker
    for i in range(1, len(cards)):
        if (cards[i][0] !=  (cards[i-1][0] + 1)) or (cards[i][1] != cards[i-1][1]):
            return False
    return True

def is_flush(cards): # kolor
    colors = [0,0,0,0]
    for card in cards:
        colors[card[1]] += 1
    if 5 in colors:
        return True
    return False

def is_straight(cards): # strit
    for i in range(1, len(cards)):
        if cards[i][0] != (cards[i-1][0] + 1):
            return False
    return True

def count_occurences(cards): # liczy figury
    counts = [0] * 15
    for card in cards:
        counts[card[0]] += 1
    return counts

def check_score(cards):
    counts = count_occurences(cards)

    if is_straight_flush(cards): # poker
        return 9
    if 4 in counts: # kareta
        return 8
    if 3 in counts and 2 in counts: # full
        return 7
    if is_flush(cards): # kolor
        return 6
    if is_straight(cards): # strit
        return 5
    if 3 in counts: # trójka
        return 4
    if counts.count(2) == 2: # dwie pary
        return 3
    if 2 in counts: # para
        return 2
    return 1 # wysoka karta


def count_combinations(deck):
    counts = np.zeros(9) # tablica o długości 9 wypełniona zerami do liczenia ile układów mamy
    all_combinations = combinations(deck, 5) # combinations zwraca wszystki możliwe kombinacje układów
    for cards in list(all_combinations):
        counts[check_score(cards)-1] += 1
    return counts

prepare_decks()

blots = count_combinations(b_deck)
figs = count_combinations(f_deck)
suma = 0
for i in range(1,9):
    for j in range(i):
        suma += blots[i] * figs[j] # Wyliczmy iloczyny dokładnie tak jak w tabelce i sumujemy je 
print(str(suma/(sum(blots)*sum(figs)) * 100) + "%") # Na koniec dzielimy przez liczbę wszystkich kombinacji
