import sys

def V(i, j):
    return 'V%d_%d' % (i, j)

def domains(Vs):
    return [q + ' in 1..9' for q in Vs]

def all_different(Qs):
    return 'all_distinct([' + ', '.join(Qs) + '])'

def get_column(j):
    return [V(i, j) for i in range(9)]

def get_raw(i):
    return [V(i, j) for j in range(9)]

def horizontal():
    return [all_different(get_raw(i)) for i in range(9)]

def vertical():
    return [all_different(get_column(j)) for j in range(9)]

def square():
    result = []
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [V(i + di, j + dj) for di in range(3) for dj in range(3)]
            result.append(all_different(square))
    return result

def print_constraints(Cs, indent, d, f):
    position = indent
    f.write(' ' * indent)
    for c in Cs:
        f.write(c + ', ')
        position += len(c)
        if position > d:
            position = indent
            f.write('\n' + ' ' * indent)

def sudoku(assignments, f):
    variables = [V(i, j) for i in range(9) for j in range(9)]

    f.write(':- use_module(library(clpfd)).\n')
    f.write('solve([' + ', '.join(variables) + ']) :-\n')

    cs = domains(variables) + vertical() + horizontal() + square()
    for i, j, val in assignments:
        cs.append('%s #= %d' % (V(i, j), val))

    print_constraints(cs, 4, 70, f)
    f.write('\n')
    f.write('    labeling([ff], [' + ', '.join(variables) + ']).\n\n')
    f.write(':- solve(X), write(X), nl.\n')

if __name__ == "__main__":
    input_file = 'zad_input.txt'
    output_file = 'zad_output.txt'

    raw = 0
    triples = []

    with open(input_file, 'r') as fin:
        for x in fin:
            x = x.strip()
            if len(x) == 9:
                for i in range(9):
                    if x[i] != '.':
                        triples.append((raw, i, int(x[i])))
                raw += 1

    with open(output_file, 'w') as fout:
        sudoku(triples, fout)
