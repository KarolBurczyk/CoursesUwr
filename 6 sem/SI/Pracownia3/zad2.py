def generate_patterns_for_line(length, groups):
    results = []

    def backtrack(group_idx, start, pattern):
        if group_idx == len(groups):
            for i in range(start, length):
                pattern[i] = '.'
            results.append("".join(pattern))
            return

        group_size = groups[group_idx]
        max_start = length - (sum(groups[group_idx:]) + len(groups) - group_idx - 1)
        for pos in range(start, max_start + 1):
            for i in range(start, pos):
                pattern[i] = '.'
            for i in range(pos, pos + group_size):
                pattern[i] = '#'
            next_start = pos + group_size
            if group_idx < len(groups) - 1:
                pattern[next_start] = '.'
                next_start += 1
            backtrack(group_idx + 1, next_start, pattern)

    if not groups or (len(groups) == 1 and groups[0] == 0):
        return ['.' * length]

    backtrack(0, 0, ['.'] * length)
    return results


def solve_nonogram(n, m, row_specs, col_specs):
    row_patterns = [generate_patterns_for_line(m, spec) for spec in row_specs]
    col_patterns = [generate_patterns_for_line(n, spec) for spec in col_specs]

    board = [[None] * m for _ in range(n)]
    row_candidates = [set(pats) for pats in row_patterns]
    col_candidates = [set(pats) for pats in col_patterns]

    def match_row(r, pattern):
        return all(board[r][c] in (None, pattern[c]) for c in range(m))

    def match_col(c, pattern):
        return all(board[r][c] in (None, pattern[r]) for r in range(n))

    def filter_candidates():
        changed = False

        for r in range(n):
            before = len(row_candidates[r])
            row_candidates[r] = {p for p in row_candidates[r] if match_row(r, p)}
            if not row_candidates[r]:
                return False, False
            changed |= (len(row_candidates[r]) < before)

        for c in range(m):
            before = len(col_candidates[c])
            col_candidates[c] = {p for p in col_candidates[c] if match_col(c, p)}
            if not col_candidates[c]:
                return False, False
            changed |= (len(col_candidates[c]) < before)

        return True, changed

    def deduce_cells():
        updated = False
        for r in range(n):
            if not row_candidates[r]:
                continue
            candidates = list(row_candidates[r])
            for c in range(m):
                if board[r][c] is not None:
                    continue
                cell_value = candidates[0][c]
                if all(pattern[c] == cell_value for pattern in candidates):
                    board[r][c] = cell_value
                    updated = True

        for c in range(m):
            if not col_candidates[c]:
                continue
            candidates = list(col_candidates[c])
            for r in range(n):
                if board[r][c] is not None:
                    continue
                cell_value = candidates[0][r]
                if all(pattern[r] == cell_value for pattern in candidates):
                    board[r][c] = cell_value
                    updated = True

        return updated

    def is_completed():
        return all(cell is not None for row in board for cell in row)

    def solve_recursive():
        while True:
            valid, changed = filter_candidates()
            if not valid:
                return False

            if deduce_cells():
                changed = True

            if is_completed():
                return True

            if not changed:
                break

        best_line, is_row, min_options = None, True, float('inf')

        for r in range(n):
            options = len(row_candidates[r])
            if 1 < options < min_options:
                best_line, is_row, min_options = r, True, options

        for c in range(m):
            options = len(col_candidates[c])
            if 1 < options < min_options:
                best_line, is_row, min_options = c, False, options

        if best_line is None:
            return False

        saved_board = [row[:] for row in board]
        saved_row_candidates = [set(rc) for rc in row_candidates]
        saved_col_candidates = [set(cc) for cc in col_candidates]

        if is_row:
            r = best_line
            for pattern in list(row_candidates[r]):
                for c in range(m):
                    board[r][c] = pattern[c]
                row_candidates[r] = {pattern}
                if solve_recursive():
                    return True
                
                board[:] = [row[:] for row in saved_board]
                row_candidates[:] = [set(rc) for rc in saved_row_candidates]
                col_candidates[:] = [set(cc) for cc in saved_col_candidates]
        else:
            c = best_line
            for pattern in list(col_candidates[c]):
                for r in range(n):
                    board[r][c] = pattern[r]
                col_candidates[c] = {pattern}
                if solve_recursive():
                    return True
                
                board[:] = [row[:] for row in saved_board]
                row_candidates[:] = [set(rc) for rc in saved_row_candidates]
                col_candidates[:] = [set(cc) for cc in saved_col_candidates]

        return False

    if not solve_recursive():
        return ['.' * m for _ in range(n)]

    return ["".join(cell or '.' for cell in row) for row in board]


def main():
    with open("zad_input.txt", encoding="utf-8") as fin:
        lines = [line.rstrip() for line in fin]

    idx = 0
    output_lines = []

    while idx < len(lines):
        if not lines[idx].strip():
            idx += 1
            continue

        n, m = map(int, lines[idx].split())
        idx += 1

        row_specs = [list(map(int, lines[idx + i].split())) if lines[idx + i].strip() else [] for i in range(n)]
        idx += n

        col_specs = [list(map(int, lines[idx + i].split())) if lines[idx + i].strip() else [] for i in range(m)]
        idx += m

        solution = solve_nonogram(n, m, row_specs, col_specs)
        output_lines.extend(solution)

    with open("zad_output.txt", "w", encoding="utf-8") as fout:
        fout.write("\n".join(output_lines))


if __name__ == "__main__":
    main()
