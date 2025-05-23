import numpy as np
from itertools import combinations

def read_input():
    with open("zad_input.txt", "r") as f:
        R, C = map(int, f.readline().split())
        row_val = [list(map(int, f.readline().split())) for _ in range(R)]
        col_val = [list(map(int, f.readline().split())) for _ in range(C)]
    return R, C, row_val, col_val

def print_picture(picture):
    with open("zad_output.txt", "w") as f:
        for row in picture:
            f.write(''.join('#' if cell else '.' for cell in row) + '\n')

def generate_line_possibilities(length, clues):
    """Generuj wszystkie możliwe układy 0/1 spełniające ograniczenia."""
    if not clues:
        return {tuple([0]*length)}

    positions = []
    total_blocks = sum(clues)
    min_required = total_blocks + len(clues) - 1
    if min_required > length:
        return set()

    first, *rest = clues
    possibilities = set()

    for start in range(length - min_required + 1):
        prefix = [0]*start + [1]*first
        if rest:
            prefix += [0]
            for suffix in generate_line_possibilities(length - len(prefix), rest):
                possibilities.add(tuple(prefix + list(suffix)))
        else:
            suffix = [0]*(length - len(prefix))
            possibilities.add(tuple(prefix + suffix))
    return possibilities

def intersection_of_possibilities(possibilities):
    """Dla listy możliwych układów znajdź pewne pola (0 lub 1)."""
    possibilities = list(possibilities)
    if not possibilities:
        return []

    n = len(possibilities[0])
    result = []
    for i in range(n):
        values = {p[i] for p in possibilities}
        if len(values) == 1:
            result.append(values.pop())
        else:
            result.append(None)
    return result

def solve(R, C, row_val, col_val):
    picture = np.full((R, C), False)
    row_domains = [generate_line_possibilities(C, clues) for clues in row_val]
    col_domains = [generate_line_possibilities(R, clues) for clues in col_val]

    changed = True
    while changed:
        changed = False

        # Wiersze
        for r in range(R):
            known = [int(picture[r, c]) if picture[r, c] in [True, False] else None for c in range(C)]
            # Odfiltruj niemożliwe możliwości
            valid = {p for p in row_domains[r] if all(known[i] is None or known[i] == p[i] for i in range(C))}
            if row_domains[r] != valid:
                row_domains[r] = valid
                changed = True

            # Zrób przecięcie
            intersection = intersection_of_possibilities(valid)
            for c in range(C):
                if intersection[c] is not None and picture[r, c] != bool(intersection[c]):
                    picture[r, c] = bool(intersection[c])
                    changed = True

        # Kolumny
        for c in range(C):
            known = [int(picture[r, c]) if picture[r, c] in [True, False] else None for r in range(R)]
            valid = {p for p in col_domains[c] if all(known[i] is None or known[i] == p[i] for i in range(R))}
            if col_domains[c] != valid:
                col_domains[c] = valid
                changed = True

            intersection = intersection_of_possibilities(valid)
            for r in range(R):
                if intersection[r] is not None and picture[r, c] != bool(intersection[r]):
                    picture[r, c] = bool(intersection[r])
                    changed = True

    return picture

# --- główne wykonanie ---
R, C, row_val, col_val = read_input()
picture = solve(R, C, row_val, col_val)
print_picture(picture)
