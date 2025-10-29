import math
import random
import chess
import chess.polyglot  # Do księgi otwarć .bin
import chess.syzygy  # Do bazy końcówek .rtbw/.rtbz

# Wartości figur
PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3.1,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
}

def evaluate_board(board: chess.Board) -> float:
    if board.is_checkmate():
        return -9999 if board.turn else 9999
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    material = 0

    for piece_type in PIECE_VALUES:
        material += len(board.pieces(piece_type, chess.WHITE)) * PIECE_VALUES[piece_type]
        material -= len(board.pieces(piece_type, chess.BLACK)) * PIECE_VALUES[piece_type]

    def mobility_score():
        original_turn = board.turn

        board.turn = chess.WHITE
        white_moves = len(list(board.legal_moves))

        board.turn = chess.BLACK
        black_moves = len(list(board.legal_moves))

        board.turn = original_turn

        return 0.1 * (white_moves - black_moves)


    mobility = mobility_score()

    def pawn_structure_penalty(color):
        pawns = board.pieces(chess.PAWN, color)
        files = [chess.square_file(sq) for sq in pawns]
        return sum(files.count(f) == 1 for f in set(files)) * 0.2

    structure = -pawn_structure_penalty(chess.WHITE)
    structure += pawn_structure_penalty(chess.BLACK)

    def king_safety(color):
        king_square = board.king(color)
        if king_square is None:
            return -10

        danger_zone = chess.SquareSet(chess.BB_KING_ATTACKS[king_square])
        attackers = sum(1 for sq in danger_zone if board.is_attacked_by(not color, sq))

        return -0.5 * attackers if color == chess.WHITE else 0.5 * attackers


    king_safety_score = king_safety(chess.WHITE) + king_safety(chess.BLACK)

    score = material + mobility + structure + king_safety_score
    if board.is_repetition(3):
        return -1000 if board.turn else 1000

    score -= board.halfmove_clock * 0.05

    return score


def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_move = None

    if maximizing_player:
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def get_best_move(board, depth=3):
    if board.fullmove_number <= 10:
        try:
            with chess.polyglot.open_reader("Perfect2023.bin") as reader:
                entry = reader.find(board)
                return entry.move
        except:
            pass
    if len(board.piece_map()) <= 5:
        try:
            with chess.syzygy.open_tablebase("syzygy/") as tablebase:
                if board.is_insufficient_material():
                    return None
                dtz = tablebase.probe_dtz(board)
                if dtz is not None:
                    best = tablebase.probe_wdl(board)
                    return best
        except:
            pass

    _, best_move = minimax(board, depth, -math.inf, math.inf, board.turn)
    return best_move

def get_random_move(board: chess.Board):
    move = random.choice(list(board.legal_moves))
    return move

N = 10
won = 0
for i in range(N):
    board = chess.Board()
    player = 0
    while not board.is_game_over():
        # print(board)
        # print()
        if player == 0:
            move = get_best_move(board, depth=3)
        else:
            move = get_random_move(board)
        if move is None:
            break
        board.push(move)
        player = abs(player - 1)
    print(board)
    result = board.result()
    if result == '1-0': # SHIFT is player 0 (AI)
        won += 1
        print(f'Won {won} / {i + 1}')

print(f"Agent won {won}/{N} games")

