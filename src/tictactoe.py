from enum import Enum, auto

#ゲームの勝敗を管理するクラス
class GameManager(Enum):
    DROW = auto()
    ON = auto()
    OVER = auto()

#盤面の印を管理するクラス
class MarkManager(Enum):
    X = auto()
    O = auto()
    EMPTY = auto()

#盤面の状態全体を管理するクラス
class Board:
    #盤面の初期化
    def __init__(self):
        #3*3の盤面を作成
        self.cell = [[MarkManager.EMPTY for i in range(3)] for j in range(3)]
        self.if_first_player = True

    #ゲーム状況の判定メソッド
    def state(self):
        if self.won():
            return GameManager.OVER
        elif len(self.possible_moves()) == 0:
            return GameManager.DROW
        else:
            return GameManager.ON