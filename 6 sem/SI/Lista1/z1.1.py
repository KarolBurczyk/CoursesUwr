# W tym programie zastosowałem BFS (zgodnie z podpowiedzią). Głównym elementem jest tutaj funkcja loop, która pobiera kolejne stany gry ze stosu
# i na ich podstawie dokłada na stos wszystkie możliwe ruchy w danym momencie. Zadbałem też o to, żeby stany gry się nie powtarzały. Funkcje
# odpowiadające za wylistowanie wszystkich możliwych ruchów dla króli i wieży sprawdzają czy król nie będzie wchodził w szacha albo czy nie 
# będzie kolidował z królem przeciwnym. Co ruch jest również sprawdzana opcja mata. Pat następuje w momencie, gdy na stosie nie ma już żadnych nowych stanów.

from collections import deque

def parse_position(pos):
    return ord(pos[0]) - ord('a'), int(pos[1]) - 1

def format_position(x, y):
    return f"{chr(x + ord('a'))}{y + 1}"

def figures_colliding(wk, bk):
    return abs(wk[0] - bk[0]) <= 1 and abs(wk[1] - bk[1]) <= 1

def get_moves_king(color, wk, wr, bk):
    x, y = wk if color == "white" else bk
    moves = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if color == "white" and not figures_colliding((nx, ny), bk) and (nx, ny)!=wr:
                    moves.append((nx, ny))
                elif not figures_colliding((nx, ny), wk) and (nx, ny)!=wr and not is_check(wk, wr, (nx, ny)):
                    moves.append((nx, ny))
    return moves

def can_king_take_rook(wk, wr, bk):
    return abs(wr[0] - bk[0]) <= 1 and abs(wr[1] - bk[1]) <= 1 and not figures_colliding(wk, wr)

def get_moves_rook(wk, wr, bk):
    moves = []
    for i in range(8):
        if i != wr[1] and (i, wr[1]) != wk and (i, wr[1]) != bk:
            moves.append((i, wr[1]))
        if i != wr[0] and (wr[0], i) != wk and (wr[0], i) != bk:
            moves.append((wr[0], i))
    return moves

def is_checkmate(wk, wr, bk):
    if is_check(wk, wr, bk) and get_moves_king("black", wk, wr, bk) == [] and not can_king_take_rook(wk, wr, bk):
        return True
    return False

def is_check(wk, wr, bk):
    if bk[0] == wr[0]:
        if wk[0] != bk[0] or (wk[1] < min(wr[1], wk[1]) or wk[1] > max(wr[1], wk[1])):
            return True
    if bk[1] == wr[1]:
        if wk[1] != bk[1] or (wk[0] < min(wr[0], wk[0]) or wk[0] > max(wr[0], wk[0])):
            return True
    return False

def make_turn(turn):
    if turn == "black":
        return "white"
    else:
        return "black"

def loop(turn, wk, wr, bk):
    queue = deque([(wk, wr, bk, 0, turn, [(wk, wr, bk)])])
    visited = set()
    
    while queue:
        wk, wr, bk, moves, t, states = queue.popleft()
        if is_checkmate(wk, wr, bk):
            return moves, states
        
        state = (wk, wr, bk, t)
        if state in visited:
            continue
        visited.add(state)
        
        if t == "black":
            possible_moves = get_moves_king("black", wk, wr, bk)
            if possible_moves == []:
                continue
            else:
                for nbk in possible_moves:
                    tmp = states.copy()
                    tmp.append((wk, wr, nbk))
                    queue.append((wk, wr, nbk, moves + 1, "white", tmp))
        else:
            possible_moves = get_moves_king("white", wk, wr, bk)
            for nwk in possible_moves:
                tmp = states.copy()
                tmp.append((nwk, wr, bk))
                queue.append((nwk, wr, bk, moves + 1, "black",tmp))
            possible_moves = get_moves_rook(wk, wr, bk)
            for nwr in possible_moves:
                tmp = states.copy()
                tmp.append((wk, nwr, bk))
                queue.append((wk, nwr, bk, moves + 1, "black", tmp))
    return "INF"

def process_states(states):
    boards = []
    i = 0
    for state in states:
        wk, wr, bk = state
        board = [[".." for _ in range(8)] for _ in range(8)]
        
        board[wk[1]][wk[0]] = "WK"
        board[wr[1]][wr[0]] = "WR"
        board[bk[1]][bk[0]] = "BK"
        
        board_str = "\n".join(" ".join(row) for row in board)
        boards.append(str(i))
        boards.append(board_str)
        i += 1
    
    return "\n".join(boards)


def main(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    results = []
    for line in lines:
        parts = line.strip().split()
        turn, wk, wr, bk = parts[0], parse_position(parts[1]), parse_position(parts[2]), parse_position(parts[3])
        result, states = loop(turn, wk, wr, bk)
        results.append(str(result) + " moves minimum\n")
        results.append(process_states(states))
    
    with open(output_file, 'w') as f:
        f.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main("zad1_input.txt", "zad1_output.txt")
