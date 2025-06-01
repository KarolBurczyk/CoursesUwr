import random
import copy

M = 8

position_weights = [
    [100, -20, 10, 5, 5, 10, -20, 100],
    [-20, -50, -2, -2, -2, -2, -50, -20],
    [10, -2, -1, -1, -1, -1, -2, 10],
    [5, -2, -1, 0, 0, -1, -2, 5],
    [5, -2, -1, 0, 0, -1, -2, 5],
    [10, -2, -1, -1, -1, -1, -2, 10],
    [-20, -50, -2, -2, -2, -2, -50, -20],
    [100, -20, 10, 5, 5, 10, -20, 100],
]

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

start_board = [[None] * M for i in range(M)]
start_board[3][3] = 1
start_board[4][4] = 1
start_board[3][4] = 0
start_board[4][3] = 0

start_fields = set()
for i in range(M):
    for j in range(M):
        if (i,j) != (3,4) and (i,j) != (4,4) and (i,j) != (4,3) and (i,j) != (3,3):
            start_fields.add((j, i))



class Board:
    def __init__(self):
        self.board = copy.deepcopy(start_board)
        self.fields = start_fields.copy()
        self.move_list = []

    def clear(self):
        self.board = copy.deepcopy(start_board)
        self.fields = start_fields.copy()
        self.move_list = []

    def moves(self, player):
        res = []
        for x, y in self.fields:
            if any(self.can_beat(x, y, direction, player) for direction in dirs):
                res.append((x, y))
        if not res:
            return [None]
        return res

    def can_beat(self, x, y, d, player):
        dx, dy = d
        x += dx
        y += dy
        cnt = 0
        while self.get(x, y) == 1 - player:
            x += dx
            y += dy
            cnt += 1
        return cnt > 0 and self.get(x, y) == player

    def get(self, x, y):
        if 0 <= x < M and 0 <= y < M:
            return self.board[y][x]
        return None

    def do_move(self, move, player):
        self.move_list.append(move)
        flipped = []
        if move is None:
            return flipped
        x0, y0 = move
        self.board[y0][x0] = player
        self.fields.discard(move)
        for dx, dy in dirs:
            x, y = x0 + dx, y0 + dy
            to_beat = []
            while self.get(x, y) == 1 - player:
                to_beat.append((x, y))
                x += dx
                y += dy
            if self.get(x, y) == player:
                for nx, ny in to_beat:
                    self.board[ny][nx] = player
                    flipped.append((nx, ny))
        return flipped


    def undo_move(self, move, player, flipped):
        if move is not None:
            x, y = move
            self.board[y][x] = None
            self.fields.add(move)
        for fx, fy in flipped:
            self.board[fy][fx] = 1 - player

    def result(self):
        res = 0
        for y in range(M):
            for x in range(M):
                b = self.board[y][x]
                if b == 0:
                    res -= 1
                elif b == 1:
                    res += 1
        return res

    def terminal(self):
        if not self.fields:
            return True
        if len(self.move_list) < 2:
            return False
        return self.move_list[-1] == self.move_list[-2] == None

    def evaluate(self, player):
        score = 0
        for y in range(M):
            for x in range(M):
                cell = self.board[y][x]
                if cell is not None:
                    multiplier = 1 if cell == player else -1
                    score += position_weights[y][x] * multiplier
        
        return score

    def minimax(self, depth, player, alpha, beta):
        if self.terminal() or depth == 0:
            return self.evaluate(player), None

        best_move = None
        if player == 1:
            max_eval = -float('inf')
            for move in self.moves(player):
                flipped = self.do_move(move, player)
                eval, _ = self.minimax(depth - 1, 1 - player, alpha, beta)
                self.undo_move(move, player, flipped)
                if move is not None:
                    self.fields.add(move)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in self.moves(player):
                flipped = self.do_move(move, player)
                eval, _ = self.minimax(depth - 1, 1 - player, alpha, beta)
                self.undo_move(move, player, flipped)
                if move is not None:
                    self.fields.add(move)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def ai_move(self, player):
        _, move = self.minimax(depth=2, player=player, alpha=-float('inf'), beta=float('inf'))
        return move
    
    def random_move(self, player):
        ms = self.moves(player)
        if ms:
            return random.choice(ms)
        return None

counter = 0
B = Board()

for i in range(1000):
    player = 1
    while True:
        if player == 1:
            m = B.ai_move(player)  
            B.do_move(m, player)
        else:
            m = B.random_move(player)  
            B.do_move(m, player)
        if B.terminal():
            break
        player = 1 - player
    if B.result() > 0:
        counter += 1
    B.clear()

print(counter)
