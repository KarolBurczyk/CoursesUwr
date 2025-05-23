import numpy as np
from itertools import combinations

class NanoSolver:
    def __init__(self):
        self.R, self.C, self.row_val, self.col_val = self.readfile()
        self.row_correct = [False]*self.R
        self.col_correct = [False]*self.C
        self.picture = np.array([[False]*self.C]*self.R)

    def readfile(self):
        with open("zad_input.txt", "r") as input:
            s = input.readline().split()
            R = (int)(s[0])
            C = (int)(s[1])

            row_val = []
            col_val = []

            for i in range(R): row_val.append(list(map(int, input.readline().strip('\n').split())))
            for i in range(C): col_val.append(list(map(int, input.readline().strip('\n').split())))
        return R, C, row_val, col_val

    def print_picture(self):
        with open("zad_output.txt", "w") as output:
            for i in range(self.R):
                for j in range(self.C):
                    if self.picture[i][j]: output.write('#')
                    else: output.write('.')
                output.write("\n")

    def get_picture_col(self, col):
        res = []
        for row in range(0, self.R):
            res.append(self.picture[row][col])
        return res

    def is_correct(self, domain_row, domain_col):
        i = 0
        for row in self.picture:
            if tuple(row) not in domain_row[i]:
                return False
            i += 1
        for col in range(0, self.C):
            if tuple(self.get_picture_col(col)) not in domain_col[col]:
                return False
        return True

    def get_possible_domains(self):
        res = [[],[]]
        for row in self.row_val:
            act_res = []
            maxx = self.C - row[-1]
            for combination in combinations(range(maxx+1), len(row)):
                blocks_dont_overlap = True
                for cell in range(1, len(combination)):
                    if combination[cell-1] + row[cell-1] >= combination[cell]:
                        blocks_dont_overlap = False
                        break

                if blocks_dont_overlap:
                    new = [0] * self.C
                    row_ptr = 0
                    for cell in combination:
                        for j in range(cell, cell + row[row_ptr]):
                            new[j] = 1
                        row_ptr += 1
                    act_res.append(new)
            res[0].append({tuple(i) for i in act_res})

        for col in self.col_val:
            act_res = []
            maxx = self.R - col[-1]
            for combination in combinations(range(maxx+1), len(col)):
                blocks_dont_overlap = True
                for cell in range(1, len(combination)):
                    if combination[cell-1] + col[cell-1] >= combination[cell]:
                        blocks_dont_overlap = False
                        break

                if blocks_dont_overlap:
                    new = [0] * self.R
                    col_ptr = 0
                    for cell in combination:
                        for j in range(cell, cell + col[col_ptr]):
                            new[j] = 1
                        col_ptr += 1
                    act_res.append(new)
            res[1].append({tuple(i) for i in act_res})
        return (res[0], res[1])

    def domain_intersection(self, domain):
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

    def clear_domain(self, cells, domain, color, is_row):
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

    def solve_ac3(self):
        domain_row, domain_col = self.get_possible_domains()

        while not self.is_correct(domain_row, domain_col):
            # --- row ---
            colored_cells = set()
            blank_cells = set()

            r = 0
            for row in domain_row:  # select row
                c = 0
                
                intersection = self.domain_intersection(row)
                for cell in range(0, len(intersection[0])):   # intersection of all possibilities in that row
                    if intersection[0][cell] == 1:
                        self.picture[r][c] = True
                        colored_cells.add((r, c))
                        
                    if intersection[1][cell] == 0:
                        self.picture[r][c] = False
                        blank_cells.add((r, c))
                    c += 1

                r += 1

            domain_col = self.clear_domain(colored_cells, domain_col, 1, True)
            domain_col = self.clear_domain(blank_cells, domain_col, 0, True)

            # --- col ---
            colored_cells = set()
            blank_cells = set()

            c = 0
            for col in domain_col:  # select col
                r = 0

                intersection = self.domain_intersection(col)
                for cell in range(0, len(intersection[0])):   # intersection of all possibilities in that col
                    if intersection[0][cell] == 1:
                        self.picture[r][c] = True
                        colored_cells.add((r, c))

                    if intersection[1][cell] == 0:
                        self.picture[r][c] = False
                        blank_cells.add((r, c))
                    r += 1

                c += 1

            domain_row = self.clear_domain(colored_cells, domain_row, 1, False)
            domain_row = self.clear_domain(blank_cells, domain_row, 0, False)
        
def main():
    solver = NanoSolver()
    solver.solve_ac3()
    solver.print_picture()

if __name__ == "__main__":
    main()