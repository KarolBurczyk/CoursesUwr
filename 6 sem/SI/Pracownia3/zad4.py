def B(i: int, j: int) -> str:
    return f'B_{i}_{j}'

def radar_constraint(rows: list[int], cols: list[int]) -> None:
    R, C = len(rows), len(cols)
    for r in range(R):
        vars = [B(r, c) for c in range(C)]
        writeln(f'    sum([{", ".join(vars)}], #=, {rows[r]}),')
    for c in range(C):
        vars = [B(r, c) for r in range(R)]
        writeln(f'    sum([{", ".join(vars)}], #=, {cols[c]}),')

def forbidden_three(R: int, C: int) -> None:
    for r in range(R):
        for c in range(1, C - 1):
            writeln(f'    {B(r, c - 1)} + 2*{B(r, c)} + 3*{B(r, c + 1)} #\\= 2,')
    for r in range(1, R - 1):
        for c in range(C):
            writeln(f'    {B(r - 1, c)} + 2*{B(r, c)} + 3*{B(r + 1, c)} #\\= 2,')

def forbidden_square(R: int, C: int) -> None:
    bad = [6, 7, 9, 11, 13, 14]
    for i in range(R - 1):
        for j in range(C - 1):
            for f in bad:
                expr = f'{B(i, j)} + 2*{B(i, j + 1)} + 4*{B(i + 1, j)} + 8*{B(i + 1, j + 1)}'
                writeln(f'    {expr} #\\= {f},')

def storms(rows: list[int], cols: list[int], triples: list[tuple[int, int, int]]) -> None:
    writeln(':- use_module(library(clpfd)).')
    R, C = len(rows), len(cols)
    vars = [B(i, j) for i in range(R) for j in range(C)]
    writeln(f'solve([{", ".join(vars)}]) :-')
    for i in range(R):
        for j in range(C):
            writeln(f'    {B(i, j)} in 0..1,')
    radar_constraint(rows, cols)
    forbidden_three(R, C)
    forbidden_square(R, C)
    for x, y, v in triples:
        writeln(f'    {B(x, y)} #= {v},')
    writeln(f'    labeling([ff], [{", ".join(vars)}]).')
    writeln('')
    writeln(":- tell('prolog_result.txt'), solve(X), write(X), nl, told.")

def writeln(s: str) -> None:
    output.write(s + '\n')

txt = open('zad_input.txt').readlines()
output = open('zad_output.txt', 'w')
rows = list(map(int, txt[0].split()))
cols = list(map(int, txt[1].split()))
triples = [list(map(int, line.split())) for line in txt[2:] if line.strip()]
storms(rows, cols, triples)
