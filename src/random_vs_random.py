from tictactoe import Board, GameManager, MarkManager
import random

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
    next_move = random.choice(board.get_possible_moves())
    board.make_mark(next_move)

    print(board)

