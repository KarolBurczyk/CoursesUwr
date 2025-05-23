import numpy as np
import copy
from itertools import combinations

R = 7
C = 7
row_val = [[]]
col_val = [[]]
picture = np.full((R, C), None)

def print_picture(picture = picture):
    with open("zad_output.txt", "w") as output:
        for i in range(R):
            for j in range(C):
                if picture[i][j]:
                    output.write('#')
                else:
                    output.write('.')
            output.write("\n")

def get_picture_col(pic, col):
    return [pic[row][col] for row in range(R)]

def is_correct(pic, domain_row, domain_col):
    i = 0
    for row in pic:
        if tuple(row) not in domain_row[i]:
            return False
        i += 1
    for col in range(0, C):
        if tuple(get_picture_col(pic, col)) not in domain_col[col]:
            return False
        
    return True

def partially_correct(pic, domain_row, domain_col):
    for r in range(R):
        valid = False
        current_row = pic[r]
        for possibility in domain_row[r]:
            if all(current_row[i] is None or current_row[i] == possibility[i] for i in range(C)):
                valid = True
                break
        if not valid:
            return False

    for c in range(C):
        current_col = get_picture_col(pic, c)
        valid = False
        for possibility in domain_col[c]:
            if all(current_col[i] is None or current_col[i] == possibility[i] for i in range(R)):
                valid = True
                break
        if not valid:
            return False

    return True

def select_unassigned_cell(pic, domain_row, domain_col):
    best_cell = None
    min_possibilities = float('inf')

    for r in range(R):
        for c in range(C):
            if pic[r][c] is None:
                row_poss = sum(1 for p in domain_row[r] if p[c] == 1 or p[c] == 0)
                col_poss = sum(1 for p in domain_col[c] if p[r] == 1 or p[r] == 0)
                possibilities = min(row_poss, col_poss)
                if possibilities < min_possibilities:
                    min_possibilities = possibilities
                    best_cell = (r, c)
    return best_cell

def get_possible_domains():
    res = [[], []]
    for row in row_val:
        act_res = []
        maxx = C - row[-1]
        for combination in combinations(range(maxx+1), len(row)):
            blocks_dont_overlap = True
            for cell in range(1, len(combination)):
                if combination[cell-1] + row[cell-1] >= combination[cell]:
                    blocks_dont_overlap = False
                    break
            if blocks_dont_overlap:
                new = [0] * C
                row_ptr = 0
                for cell in combination:
                    for j in range(cell, cell + row[row_ptr]):
                        new[j] = 1
                    row_ptr += 1
                act_res.append(new)
        res[0].append({tuple(i) for i in act_res})

    for col in col_val:
        act_res = []
        maxx = R - col[-1]
        for combination in combinations(range(maxx+1), len(col)):
            blocks_dont_overlap = True
            for cell in range(1, len(combination)):
                if combination[cell-1] + col[cell-1] >= combination[cell]:
                    blocks_dont_overlap = False
                    break
            if blocks_dont_overlap:
                new = [0] * R
                col_ptr = 0
                for cell in combination:
                    for j in range(cell, cell + col[col_ptr]):
                        new[j] = 1
                    col_ptr += 1
                act_res.append(new)
        res[1].append({tuple(i) for i in act_res})

    return (res[0], res[1])

def domain_intersection(domain):
    intersetion1 = list(domain)[0]
    intersetion0 = list(domain)[0]

    for poss in domain:
        intersetion1 = [1 if intersetion1[i] == poss[i] and poss[i] == 1 else 0 for i in range(len(poss))]
        intersetion0 = [0 if intersetion0[i] == poss[i] and poss[i] == 0 else 1 for i in range(len(poss))]
    
    return (intersetion1, intersetion0)

def clear_domain(cells, domain, color, is_row):
    if is_row:
        for r, c in cells:
            to_clear = []
            for poss in domain[c]:
                if poss[r] != color:
                    to_clear.append(poss)
            for rm in to_clear:
                domain[c] -= {rm}
    else:
        for r, c in cells:
            to_clear = []
            for poss in domain[r]:
                if poss[c] != color:
                    to_clear.append(poss)
            for rm in to_clear:
                domain[r] -= {rm}
    return domain

def solve_ac3():
    domain_row, domain_col = get_possible_domains()
    is_changed = True
    while(is_changed):
        is_changed = False
        colored_cells = set()
        blank_cells = set()

        r = 0
        for row in domain_row:
            c = 0
            intersection = domain_intersection(row)
            for cell in range(len(intersection[0])):
                if intersection[0][cell] == 1:
                    if picture[r][c] is None:
                        is_changed = True
                    picture[r][c] = True
                    colored_cells.add((r, c))
                if intersection[1][cell] == 0:
                    if picture[r][c] is None:
                        is_changed = True
                    picture[r][c] = False
                    blank_cells.add((r, c))
                c += 1
            r += 1

        domain_col = clear_domain(colored_cells, domain_col, 1, True)
        domain_col = clear_domain(blank_cells, domain_col, 0, True)

        colored_cells = set()
        blank_cells = set()

        c = 0
        for col in domain_col:
            r = 0
            intersection = domain_intersection(col)
            for cell in range(len(intersection[0])):
                if intersection[0][cell] == 1:
                    if picture[r][c] is None:
                        is_changed = True
                    picture[r][c] = True
                    colored_cells.add((r, c))
                if intersection[1][cell] == 0:
                    if picture[r][c] is None:
                        is_changed = True
                    picture[r][c] = False
                    blank_cells.add((r, c))
                r += 1
            c += 1

        domain_row = clear_domain(colored_cells, domain_row, 1, False)
        domain_row = clear_domain(blank_cells, domain_row, 0, False)

    return domain_row, domain_col

def solve_bt(pic, domain_row, domain_col):
    if not partially_correct(pic, domain_row, domain_col):
        return None
    next_cell = select_unassigned_cell(pic, domain_row, domain_col)
    if next_cell is None:
        if is_correct(pic, domain_row, domain_col):
            return pic
        else:
            return None
    r, c = next_cell

    new_pic = copy.deepcopy(pic)
    new_pic[r][c] = True
    res = solve_bt(new_pic, domain_row, domain_col)
    if res is not None:
        return res

    new_pic = copy.deepcopy(pic)
    new_pic[r][c] = False
    res = solve_bt(new_pic, domain_row, domain_col)
    if res is not None:
        return res

    return None

def read_input():
    with open("zad_input.txt", "r") as input:
        s = input.readline().split()
        R = int(s[0])
        C = int(s[1])

        row_val = []
        col_val = []
        for _ in range(R):
            row_val.append(list(map(int, input.readline().strip('\n').split())))
        for _ in range(C):
            col_val.append(list(map(int, input.readline().strip('\n').split())))
        return R, C, row_val, col_val

R, C, row_val, col_val = read_input()
picture = np.full((R, C), None)

domain_row, domain_col = solve_ac3()
picture = solve_bt(copy.deepcopy(picture), domain_row, domain_col)

if picture is not None:
    print_picture(picture)
else:
    print("Brak rozwiązania")