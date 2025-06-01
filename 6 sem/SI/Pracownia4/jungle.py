import random
import copy

ROWS, COLS = 9, 7

PIECE_STRENGTH = {
    'r': 1, 'c': 2, 'd': 3, 'w': 4, 'j': 5, 't': 6, 'l': 7, 'e': 8,
    'R': 1, 'C': 2, 'D': 3, 'W': 4, 'J': 5, 'T': 6, 'L': 7, 'E': 8
}

TRAPS = {(0,2), (0,4), (1,3), (8,2), (8,4), (7,3)}
DENS = {(0,3): 0, (8,3): 1}
WATER = {(3,1),(3,2),(3,4),(3,5),(4,1),(4,2),(4,4),(4,5),(5,1),(5,2),(5,4),(5,5)}

DIRS = [(-1,0), (1,0), (0,-1), (0,1)]

class Jungle:

    def __init__(self, board=None, player_turn=0):
        self.player_turn = player_turn
        self.board = board or [
            list("L.....T"),
            list(".D...C."),
            list("R.J.W.E"),
            list("......."),
            list("......."),
            list("......."),
            list("e.w.j.r"),
            list(".c...d."),
            list("t.....l")
        ]


    def clone(self):
        board_copy = [list(row) for row in self.board]
        return Jungle(board_copy, self.player_turn)


    def show(self):
        for row in self.board:
            print(''.join(row))
        print()
                

    def is_enemy(self, piece, target):
        if not piece or not target:
            return False
        return ('A' <= piece <= 'Z') != ('A' <= piece <= 'Z')
    

    def is_friend(self, piece, target):
        if not piece or not target:
            return False
        return ('A' <= piece <= 'Z') == ('A' <= piece <= 'Z')


    def piece_strength(self, piece):
        return PIECE_STRENGTH[piece]


    def get_legal_moves(self):
        moves = []
        for r in range(ROWS):
            for c in range(COLS):
                piece = self.board[r][c]
                if piece == '.':
                    continue
                if (self.player_turn == 0 and 'A' <= piece <= 'Z') or (self.player_turn == 1 and 'a' <= piece <= 'z'):
                    moves.extend(self.get_piece_moves(r, c, piece))
        return moves


    def get_piece_moves(self, r, c, piece):
        moves = []
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < ROWS and 0 <= nc < COLS):
                continue
            target = self.board[nr][nc]

            if (self.player_turn == 1 and (nr, nc) == (8,3)) or (self.player_turn == 0 and (nr, nc) == (0,3)):
                continue

            if (r, c) in WATER or (nr, nc) in WATER:
                if piece.lower() != 'r':
                    if piece.lower() in ('l', 't'):
                        sr, sc = r, c
                        while True:
                            sr += dr
                            sc += dc
                            if not (0 <= sr < ROWS and 0 <= sc < COLS):
                                break
                            if (sr, sc) not in WATER:
                                if self.board[sr][sc] and self.is_friend(piece, self.board[sr][sc]):
                                    break
                                if self.board[sr - dr][sc - dc].lower() == 'r':
                                    break
                                if self.can_capture(piece, self.board[sr][sc], (sr, sc)):
                                    moves.append(((r, c), (sr, sc)))
                                break
                    continue

            if target == '.':
                moves.append(((r, c), (nr, nc)))
                continue
            if self.is_friend(piece, target):
                continue
            if self.can_capture(piece, target, (nr, nc)):
                moves.append(((r, c), (nr, nc)))
        return moves


    def can_capture(self, piece, target, pos):
        if target == '.':
            return True
        if pos in TRAPS:
            return True
        if piece.lower() == 'r' and self.board[pos[0]][pos[1]] and target.lower() == 'e':
            return True
        if piece.lower() == 'e' and target.lower() == 'r':
            return False
        return PIECE_STRENGTH[piece] >= PIECE_STRENGTH[target]


    def make_move(self, move):
        if move is not None:
            (r1, c1), (r2, c2) = move
            piece = self.board[r1][c1]
            self.board[r1][c1] = '.'
            self.board[r2][c2] = piece
            self.player_turn = 1 - self.player_turn


    def is_game_over(self):
        return self.board[0][3] != '.' or self.board[8][3] != '.'


    def winner(self):
        if self.board[0][3] != '.':
            return 1
        if self.board[8][3] != '.':
            return 0
        return None


    def heuristic_score(self, player):
        score = 0
        for r in range(ROWS):
            for c in range(COLS):
                piece = self.board[r][c]
                if piece == '.':
                    continue
                strength = PIECE_STRENGTH[piece]
                sign = 1 if ('A' <= piece <= 'Z' and player == 0) or  ('a' <= piece <= 'z' and player == 1) else -1
                
                score += sign * (10 * strength)

                enemy_den = (8, 3) if self.player_turn == 0 else (0, 3)
                dist = abs(enemy_den[0] - r) + abs(enemy_den[1] - c)
                score += sign * (20 - dist)

                if (r, c) in TRAPS:
                    score += sign * 15

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in TRAPS:
                        score += sign * 2

                if (r, c) in DENS and DENS[(r, c)] != self.player_turn:
                    score += sign * 1000

        return score



class JungleAgent:

    def __init__(self, simulations_budget=200):
        self.N = simulations_budget


    def simulate_random_game(self, state, max_moves=30):
        for _ in range(max_moves):
            if state.is_game_over():
                return state.winner()
            legal_moves = state.get_legal_moves()
            if not legal_moves:
                return None
            move = random.choice(legal_moves)
            state.make_move(move)
        
        # if state.winner() is not None:
        return state.winner()
        # else:
        #     return 0 if state.heuristic_score(0) > state.heuristic_score(1) else 1




    def evaluate_state(self, state, move, simulations_per_move):
        wins = 0
        for _ in range(simulations_per_move):
            sim_state = state.clone()
            sim_state.make_move(move)
            sim_result = self.simulate_random_game(sim_state)
            if sim_result == 0:
                wins += 1
        return wins


    def choose_best_move(self, state):
        moves = state.get_legal_moves()
        random.shuffle(moves)

        if not moves:
            return None
        simulations_per_move = max(1, self.N // len(moves))
        best_move = None
        best_score = -1

        for move in moves:
            score = self.evaluate_state(state, move, simulations_per_move)
            if score > best_score:
                best_score = score
                best_move = move

        return best_move
    

    def choose_random_move(self, state):
        moves = state.get_legal_moves()
        if not moves:
            return None
        move = random.choice(moves)
        return move

# player 0 - MCS - A - Z
# player 1 - random - a - z

def loop():
    state = Jungle()
    agent = JungleAgent()
    player = 0

    while not state.is_game_over():
        # state.show()
        if player == 0:
            move = agent.choose_best_move(state.clone())
        else:
            move = agent.choose_random_move(state.clone())

        if state.get_legal_moves() == []:
            print("Player", player, "lost")
            break

        state.make_move(move)
        player = 1 - player

    print("Won player", state.winner())
    return state.winner()

n = 50
score = 0
for i in range(n):
    if loop() == 0:
        score += 1
print("Won", score, "out of", n)