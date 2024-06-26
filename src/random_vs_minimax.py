from tictactoe import Board, GameManager, MarkManager
from minimax import minimax
import random
import math

board = Board()

#ゲーム終了まで無限ループ
while True:
    #ゲームの終了判定
    if board.state() == GameManager.DROW:
        print("Drow\n")
        break
    if board.state() == GameManager.OVER:
        print("winner:後手\n" if board.is_first_player else "winner:先手\n")
        break
    print("先手" if board.is_first_player else "後手")

    best_score = -math.inf
    best_move = None
    #最善手の選択
    if board.is_first_player:
        move_dict = {}
        for move in board.get_possible_moves():
            board.make_mark(move)
            score = -minimax(board)
            move_dict[move] = score
            board.rewind(move)
            if score > best_score:
                best_score = score
                best_move = move
        next_move = best_move
        print(move_dict)
    else:
        #後手の場合はランダムに選択
        next_move = random.choice(board.get_possible_moves())
    board.make_mark(next_move)

    print(board)

