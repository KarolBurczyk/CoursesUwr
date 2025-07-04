#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import copy
import random

M = 8
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

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

class Board:
    def __init__(self):
        self.board = [[None] * M for _ in range(M)]
        self.board[3][3] = 1
        self.board[4][4] = 1
        self.board[3][4] = 0
        self.board[4][3] = 0
        self.fields = {(x, y) for y in range(M) for x in range(M) if self.board[y][x] is None}
        self.move_list = []

    def get(self, x, y):
        if 0 <= x < M and 0 <= y < M:
            return self.board[y][x]
        return None

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

    def moves(self, player):
        res = []
        for x, y in self.fields:
            if any(self.can_beat(x, y, direction, player) for direction in dirs):
                res.append((x, y))
        if not res:
            return [None]
        return res

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


class Player:
    def __init__(self):
        self.reset()

    def say(self, msg):
        sys.stdout.write(msg + "\n")
        sys.stdout.flush()

    def hear(self):
        line = sys.stdin.readline().split()
        return line[0], line[1:]

    def reset(self):
        self.game = Board()
        self.my_player = 1
        self.say("RDY")

    def loop(self):
        while True:
            cmd, args = self.hear()
            if cmd == "HEDID":
                _, _ = args[0], args[1]  # timeouts
                move = tuple(map(int, args[2:]))
                if move == (-1, -1):
                    move = None
                self.game.do_move(move, 1 - self.my_player)
            elif cmd == "UGO":
                self.my_player = 0
            elif cmd == "ONEMORE":
                self.reset()
                continue
            elif cmd == "BYE":
                break

            # Make a move using minimax
            _, move = self.game.minimax(depth=4, player=self.my_player, alpha=-float("inf"), beta=float("inf"))
            if move is None:
                self.game.do_move(None, self.my_player)
                self.say("IDO -1 -1")
            else:
                self.game.do_move(move, self.my_player)
                self.say(f"IDO {move[0]} {move[1]}")


if __name__ == "__main__":
    Player().loop()
