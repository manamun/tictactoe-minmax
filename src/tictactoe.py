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
        self.is_first_player = True

    #ゲーム状況の判定メソッド
    def state(self):
        if self.won():
            return GameManager.OVER
        elif len(self.get_possible_moves()) == 0:
            return GameManager.DROW
        else:
            return GameManager.ON
        
    #現在置くことのできる場所を取得するメソッド
    def get_possible_moves(self):
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if self.cell[i][j] == MarkManager.EMPTY:
                    possible_moves.append((i,j))
        return possible_moves
    
    #指定された場所に印をつけるメソッド
    def make_mark(self, move):

        if self.cell[move[0]][move[1]] == MarkManager.EMPTY:
            if self.is_first_player:
                self.cell[move[0]][move[1]] = MarkManager.X
            else:
                self.cell[move[0]][move[1]] = MarkManager.O
            self.is_first_player = not self.is_first_player

    #勝利判定メソッド
    def won(self):
        def check_cells(x,y,dx,dy):
            if self.cell[x][y] == MarkManager.EMPTY:
                return False
            for i in range(3):
                if self.cell[x][y] != self.cell[x + i * dx][y + i * dy]:
                    return False
            return True
        
        for i in range(3):
            #垂直方向に判定
            if check_cells(i, 0, 0, 1):
                return True
            #水平方向に判定
            if check_cells(0, i, 1, 0):
                return True
        
        #対角方向に判定
        if check_cells(0,0,1,1):
            return True
        if check_cells(0,2,1,-1):
            return True
        
    #指定されたマスの場所の印を空欄(EMPTY)にするメソッド
    def rewind(self, move):
        #rewind the board
        self.cell[move[0]][move[1]] = MarkManager.EMPTY
        self.is_first_player = not self.is_first_player
    
    #盤面を表示するメソッド
    def __str__(self):
        board_str = ""
        for i in range(3):
            for j in range(3):
                if self.cell[i][j] == MarkManager.X:
                    board_str += "X"
                elif self.cell[i][j] == MarkManager.O:
                    board_str += "O"
                else:
                    board_str += "/"
            board_str += "\n"

        return board_str


