from tictactoe import *
import math

#mini-max法を再帰的に実行するための関数
def minimax(board):
    #評価関数の値
    #引き分け:0
    #負け:-1
    #勝ち:1

    if board.state() == GameManager.DROW:
        return 0
    #1がないのは，次の手の評価関数を計算する時に符号を反転させるため
    elif board.state() == GameManager.OVER:
        return -1
    
    #評価関数の最適値の初期値は-無限大
    best_score = -math.inf

    #全ての可能な手について評価関数を計算
    for move in board.get_possible_moves():
        board.make_mark(move)
        #自分が勝つ:1 相手が勝つ:-1
        score = -minimax(board)
        #次のループのために，手を戻す
        board.rewind(move)
        if score > best_score:
            best_score = score
    
    return best_score