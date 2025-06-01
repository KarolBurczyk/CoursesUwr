#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import math

M = 8
INF = int(1e9)
DEPTH = 2

DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1),
              (1, 0), (1, -1), (0, -1), (-1, -1)]

CORNERS = [(0, 0), (0, 7), (7, 0), (7, 7)]

CELL_SCORE = [
    [20, -3, 11,  8,  8, 11, -3, 20],
    [-3, -7, -4,  1,  1, -4, -7, -3],
    [11, -4,  2,  2,  2,  2, -4, 11],
    [8,   1,  2, -3, -3,  2,  1,  8],
    [8,   1,  2, -3, -3,  2,  1,  8],
    [11, -4,  2,  2,  2,  2, -4, 11],
    [-3, -7, -4,  1,  1, -4, -7, -3],
    [20, -3, 11,  8,  8, 11, -3, 20],
]

class State:
    def __init__(self, starting=False):
        self.player = [[False] * M for _ in range(M)]
        self.opponent = [[False] * M for _ in range(M)]
        self.reset(starting)

    def reset(self, starting):
        for i in range(M):
            for j in range(M):
                self.player[i][j] = False
                self.opponent[i][j] = False
        self.player[3][4] = self.player[4][3] = True
        self.opponent[3][3] = self.opponent[4][4] = True
        if not starting:
            self.swap_players()

    def swap_players(self):
        self.player, self.opponent = self.opponent, self.player

    def good_position(self, row, col):
        return 0 <= row < M and 0 <= col < M

    def get_player_cell(self, row, col):
        return self.good_position(row, col) and self.player[row][col]

    def get_opponent_cell(self, row, col):
        return self.good_position(row, col) and self.opponent[row][col]

    def set_player_cell(self, row, col, value):
        if self.good_position(row, col):
            self.player[row][col] = value

    def set_opponent_cell(self, row, col, value):
        if self.good_position(row, col):
            self.opponent[row][col] = value

    def possible_move(self, row, col, d):
        dr, dc = DIRECTIONS[d]
        row += dr
        col += dc
        if not self.good_position(row, col) or not self.get_opponent_cell(row, col):
            return False
        while self.good_position(row, col) and self.get_opponent_cell(row, col):
            row += dr
            col += dc
        return self.good_position(row, col) and self.get_player_cell(row, col)

    def get_actions(self):
        res = []
        for row in range(M):
            for col in range(M):
                if self.get_player_cell(row, col) or self.get_opponent_cell(row, col):
                    continue
                for d in range(8):
                    if self.possible_move(row, col, d):
                        res.append((row, col))
                        break
        return res

    def make_move(self, row, col):
        self.set_player_cell(row, col, True)
        for d in range(8):
            if not self.possible_move(row, col, d):
                continue
            dr, dc = DIRECTIONS[d]
            new_row = row + dr
            new_col = col + dc
            while self.get_opponent_cell(new_row, new_col):
                self.set_player_cell(new_row, new_col, True)
                self.set_opponent_cell(new_row, new_col, False)
                new_row += dr
                new_col += dc

    def make_action(self, row, col):
        if row != -1 and col != -1:
            self.make_move(row, col)
        self.swap_players()

    def make_new_state(self, row, col):
        new_state = State()
        new_state.player = [row.copy() for row in self.player]
        new_state.opponent = [row.copy() for row in self.opponent]
        new_state.make_action(row, col)
        return new_state

    def utility(self):
        score = 0
        for i in range(M):
            for j in range(M):
                if self.get_player_cell(i, j):
                    score += 1
                elif self.get_opponent_cell(i, j):
                    score -= 1
        return score

    def calculate_ratio(self, player, opponent):
        total = player + opponent
        return 0 if total == 0 else int(100 * (player - opponent) / total)

    def heuristic_value(self):
        board_bilans = 0
        player_cells = 0
        opponent_cells = 0
        for i in range(M):
            for j in range(M):
                if self.get_player_cell(i, j):
                    board_bilans += CELL_SCORE[i][j]
                    player_cells += 1
                elif self.get_opponent_cell(i, j):
                    board_bilans -= CELL_SCORE[i][j]
                    opponent_cells += 1

        ratio = self.calculate_ratio(player_cells, opponent_cells)

        player_corners = sum(self.get_player_cell(r, c) for r, c in CORNERS)
        opponent_corners = sum(self.get_opponent_cell(r, c) for r, c in CORNERS)
        corner_ratio = self.calculate_ratio(player_corners, opponent_corners) if (player_corners + opponent_corners) else 0

        player_close_corners = 0
        opponent_close_corners = 0
        for row, col in CORNERS:
            if self.get_player_cell(row, col) or self.get_opponent_cell(row, col):
                continue
            for dr, dc in DIRECTIONS:
                r, c = row + dr, col + dc
                if self.good_position(r, c):
                    if self.get_player_cell(r, c):
                        player_close_corners += 1
                    elif self.get_opponent_cell(r, c):
                        opponent_close_corners += 1

        close_corner_value = player_close_corners - opponent_close_corners

        return ((10 * ratio) +
                (800 * corner_ratio) +
                (-12 * 380 * close_corner_value) +
                (80 * board_bilans))

    def terminal(self, actions=None):
        return len(self.get_actions() if actions is None else actions) == 0


class AI:
    def __init__(self):
        self.MAX_DEPTH = DEPTH

    def best_action(self, state):
        best_value = -INF
        best_move = (-1, -1)
        actions = state.get_actions()
        for row, col in actions:
            value = self.alpha_beta(state.make_new_state(row, col), self.MAX_DEPTH, False, -INF, INF)
            if value > best_value:
                best_value = value
                best_move = (row, col)
        return best_move

    def alpha_beta(self, state, depth, maximizing, alpha, beta):
        actions = state.get_actions()
        if state.terminal(actions):
            next_state = state.make_new_state(-1, -1)
            if next_state.terminal():
                return state.utility() * (1 if maximizing else -1)
            return self.alpha_beta(next_state, depth, not maximizing, alpha, beta)

        if depth == 0:
            return state.heuristic_value() * (1 if maximizing else -1)

        if maximizing:
            max_eval = -INF
            for row, col in actions:
                eval = self.alpha_beta(state.make_new_state(row, col), depth - 1, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = INF
            for row, col in actions:
                eval = self.alpha_beta(state.make_new_state(row, col), depth - 1, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval


class Player:
    def __init__(self):
        self.reset()

    def say(self, *args):
        print(*args, flush=True)

    def reset(self):
        self.game = State(True)
        self.ai = AI()
        self.say("RDY")

    def loop(self):
        while True:
            parts = input().split()
            if parts[0] == "BYE":
                break
            elif parts[0] == "UGO":
                _ = float(parts[1]), float(parts[2])
                row, col = self.ai.best_action(self.game)
                self.say("IDO", col, row)
                self.game.make_action(row, col)
            elif parts[0] == "HEDID":
                _ = float(parts[1]), float(parts[2])
                col, row = int(parts[3]), int(parts[4])
                self.game.make_action(row, col)
                row, col = self.ai.best_action(self.game)
                self.say("IDO", col, row)
                self.game.make_action(row, col)
            elif parts[0] == "ONEMORE":
                self.game.reset(True)
                self.say("RDY")


if __name__ == "__main__":
    Player().loop()