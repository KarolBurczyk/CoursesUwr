import numpy as np
from itertools import combinations

R = 7      # picture row size
C = 7      # picture col size
row_val = [[]]    # how many how long blocks per row
col_val = [[]]    # how many how long blocks per col
row_correct = [False]*R
col_correct = [False]*C
picture = np.array([[False]*C]*R)

def print_picture(picture = picture):
    with open("zad_output.txt", "w") as output:
        for i in range(R):
            for j in range(C):
                if picture[i][j]: output.write('#')
                else: output.write('.')
            output.write("\n")

def get_picture_col(col):
    res = []
    for row in range(0, R):
        res.append(picture[row][col])
    return res


def is_correct(domain_row, domain_col):   # if picture is correct <=> its rows and cols are in domain
    i = 0
    for row in picture:
        if tuple(row) not in domain_row[i]:
            return False
        i += 1
    for col in range(0, C):
        if tuple(get_picture_col(col)) not in domain_col[col]:
            return False
        
    return True


def get_possible_domains():    # generate all possibilities/domains for each row and column
    res = [[],[]]
    for row in row_val:
        act_res = []
        maxx = C - row[-1]
        for combination in combinations(range(maxx+1), len(row)):   # combination of block starts
            blocks_dont_overlap = True
            for cell in range(1, len(combination)):
                # generate all possible combinations (block placements)
                # and choose only those, which are correct
                if combination[cell-1] + row[cell-1] >= combination[cell]:
                    blocks_dont_overlap = False
                    break
            if blocks_dont_overlap: # color blocks in row
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
                # generate all possible combinations (block placements)
                # and choose only those, which are correct
                if combination[cell-1] + col[cell-1] >= combination[cell]:
                    blocks_dont_overlap = False
                    break

            if blocks_dont_overlap: # color blocks in col
                new = [0] * R
                col_ptr = 0
                for cell in combination:
                    for j in range(cell, cell + col[col_ptr]):
                        new[j] = 1
                    col_ptr += 1
                act_res.append(new)
        res[1].append({tuple(i) for i in act_res})
    return (res[0], res[1])

def domain_intersection(domain):    # calculate intersection of given domain for row/col
    intersetion1 = list(domain)[0]
    intersetion0 = list(domain)[0]

    for poss in domain:
        intersetion1 = [1 if intersetion1[i] == poss[i] and poss[i] == 1 
                          else 0 
                            for i in range(0, len(poss))]
        intersetion0 = [0 if intersetion0[i] == poss[i] and poss[i] == 0 
                          else 1 
                            for i in range(0, len(poss))]
            
    return (intersetion1, intersetion0)

def clear_domain(cells, domain, color, is_row):   # remove not fitting possibilities from domain
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


def solve_ac3(max_iterations=10):
    domain_row, domain_col = get_possible_domains()
    iteration = 0

    while not is_correct(domain_row, domain_col) and iteration < max_iterations:
        iteration += 1
        # --- row ---
        colored_cells = set()
        blank_cells = set()

        for r, row in enumerate(domain_row):
            intersection = domain_intersection(row)
            for c in range(C):
                if intersection[0][c] == 1:
                    picture[r][c] = True
                    colored_cells.add((r, c))
                if intersection[1][c] == 0:
                    picture[r][c] = False
                    blank_cells.add((r, c))

        domain_col = clear_domain(colored_cells, domain_col, 1, True)
        domain_col = clear_domain(blank_cells, domain_col, 0, True)

        # --- col ---
        colored_cells = set()
        blank_cells = set()

        for c, col in enumerate(domain_col):
            intersection = domain_intersection(col)
            for r in range(R):
                if intersection[0][r] == 1:
                    picture[r][c] = True
                    colored_cells.add((r, c))
                if intersection[1][r] == 0:
                    picture[r][c] = False
                    blank_cells.add((r, c))

        domain_row = clear_domain(colored_cells, domain_row, 1, False)
        domain_row = clear_domain(blank_cells, domain_row, 0, False)

    return domain_row, domain_col


def is_partial_valid_line(line, clues):
    groups = []
    count = 0
    for val in line:
        if val == True:
            count += 1
        elif count > 0:
            groups.append(count)
            count = 0
    if count > 0:
        groups.append(count)

    # Allow prefix match during backtracking (partial)
    return all(groups[i] == clues[i] for i in range(min(len(groups), len(clues))))


def is_partial_solution_valid():
    for r in range(R):
        if not is_partial_valid_line(picture[r], row_val[r]):
            return False
    for c in range(C):
        col = [picture[r][c] for r in range(R)]
        if not is_partial_valid_line(col, col_val[c]):
            return False
    return True


def is_complete():
    for r in range(R):
        if not is_partial_valid_line(picture[r], row_val[r]):
            return False
    for c in range(C):
        col = [picture[r][c] for r in range(R)]
        if not is_partial_valid_line(col, col_val[c]):
            return False
    return True


def backtrack(r=0, c=0):
    if r == R:
        return is_complete()
    next_r, next_c = (r, c+1) if c + 1 < C else (r+1, 0)
    for val in [True, False]:
        picture[r][c] = val
        if is_partial_solution_valid() and backtrack(next_r, next_c):
            return True
    picture[r][c] = False  # backtrack
    return False


def read_input():
    with open("zad_input.txt", "r") as input:
        s = input.readline().split()
        R = (int)(s[0])
        C = (int)(s[1])

        row_val = []
        col_val = []
        for i in range(R): row_val.append(list(map(int, input.readline().strip('\n').split())))
        for i in range(C): col_val.append(list(map(int, input.readline().strip('\n').split())))
        return R, C, row_val, col_val


R, C, row_val, col_val = read_input()
row_correct = [False]*R
col_correct = [False]*C
picture = np.array([[False]*C for _ in range(R)])

domain_row, domain_col = solve_ac3(max_iterations=10)
backtrack()
print_picture(picture)
