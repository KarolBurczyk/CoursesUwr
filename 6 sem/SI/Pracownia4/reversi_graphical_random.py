import random
import sys
from collections import defaultdict as dd
from turtle import *

#####################################################
# turtle graphic
#####################################################
tracer(0, 1)

BOK = 50
SX = 0
SY = 0
M = 8


def kwadrat(x, y, kolor):
    fillcolor(kolor)
    pu()
    goto(SX + x * BOK, SY + y * BOK)
    pd()
    begin_fill()
    for i in range(4):
        fd(BOK)
        rt(90)
    end_fill()


def kolko(x, y, kolor):
    fillcolor(kolor)

    pu()
    goto(SX + x * BOK + BOK / 2, SY + y * BOK - BOK)
    pd()
    begin_fill()
    circle(BOK / 2)
    end_fill()


#####################################################


def initial_board():
    B = [[None] * M for i in range(M)]
    B[3][3] = 1
    B[4][4] = 1
    B[3][4] = 0
    B[4][3] = 0
    return B


class Board:
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def __init__(self):
        self.board = initial_board()
        self.fields = set()
        self.move_list = []
        self.history = []
        for i in range(M):
            for j in range(M):
                if self.board[i][j] == None:
                    self.fields.add((j, i))

    def draw(self):
        for i in range(M):
            res = []
            for j in range(M):
                b = self.board[i][j]
                if b == None:
                    res.append(".")
                elif b == 1:
                    res.append("#")
                else:
                    res.append("o")
            print("".join(res))
        print

    def show(self):
        for i in range(M):
            for j in range(M):
                kwadrat(j, i, "green")

        for i in range(M):
            for j in range(M):
                if self.board[i][j] == 1:
                    kolko(j, i, "black")
                if self.board[i][j] == 0:
                    kolko(j, i, "white")

    def moves(self, player):
        res = []
        for x, y in self.fields:
            if any(self.can_beat(x, y, direction, player) for direction in Board.dirs):
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
        self.history.append([x[:] for x in self.board])
        self.move_list.append(move)

        if move == None:
            return
        x, y = move
        x0, y0 = move
        self.board[y][x] = player
        self.fields -= set([move])
        for dx, dy in self.dirs:
            x, y = x0, y0
            to_beat = []
            x += dx
            y += dy
            while self.get(x, y) == 1 - player:
                to_beat.append((x, y))
                x += dx
                y += dy
            if self.get(x, y) == player:
                for nx, ny in to_beat:
                    self.board[ny][nx] = player

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
                if self.board[y][x] == player:
                    score += 1
                elif self.board[y][x] == 1 - player:
                    score -= 1
        return score

    def minimax(self, depth, player, alpha, beta):
        if self.terminal() or depth == 0:
            return self.evaluate(player), None

        best_move = None
        if player == 1:  # maximizing player
            max_eval = -float('inf')
            for move in self.moves(player):
                saved = [row[:] for row in self.board]
                saved_fields = self.fields.copy()
                self.do_move(move, player)
                eval, _ = self.minimax(depth - 1, 1 - player, alpha, beta)
                self.board = saved
                self.fields = saved_fields
                if move is not None:
                    self.fields.add(move)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:  # minimizing player
            min_eval = float('inf')
            for move in self.moves(player):
                saved = [row[:] for row in self.board]
                saved_fields = self.fields.copy()
                self.do_move(move, player)
                eval, _ = self.minimax(depth - 1, 1 - player, alpha, beta)
                self.board = saved
                self.fields = saved_fields
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
        _, move = self.minimax(depth=3, player=player, alpha=-float('inf'), beta=float('inf'))
        return move


player = 0
B = Board()

def click_handler(x_click, y_click):
    global player
    x = int((x_click - SX) // BOK)
    y = int((y_click - SY) // BOK) + 1
    if 0 <= x < M and 0 <= y < M:
        if (x, y) in B.moves(player):
            B.do_move((x, y), player)
            player = 1 - player
            update_game()
    if B.moves(player) is None:
        B.do_move(None, player)

def ai_move():
    global player
    m = B.ai_move(player)  
    B.do_move(m, player)
    player = 1 - player
    update_game()

def update_game():
    global player
    B.draw()
    B.show()
    if B.terminal():
        print("Koniec gry. Wynik:", B.result())
        return
    if player == 1:
        ontimer(ai_move, 500)  # 500ms opóźnienia

    else:
        print(f"Teraz ruch gracza: {'biały (o)' if player == 0 else 'czarny (#)'}")


# Start gry
update_game()
onscreenclick(click_handler)
done()

