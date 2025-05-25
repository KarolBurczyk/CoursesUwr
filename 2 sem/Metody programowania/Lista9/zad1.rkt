#lang plait

E -> E + S | E - S | S
S -> S * F | S / F | F
F -> L | (E)
L -> S | CL
C -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

