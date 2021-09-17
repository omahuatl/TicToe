
class TicToe():
    def __init__(self):
        self.board =[
            ["_", "|", "_", "|", "_"],
            ["_", "|", "_", "|", "_"],
            ["_", "|", "_", "|", "_"],
        ]
        self.turn = "X"
        self. X =0
        self. Y =0
        self.status = "_"

    def validate_coordinates(self ,x ,y):
        # validate coordinates , now assign to the correct ones for the 3x5 matrix
        if 0 < x < 4 and 0 < y < 4:
            if x == 1:
                x = 0
            elif x == 2:
                x = 1
            elif x == 3:
                x = 2
            self. X =x
            if y == 1:
                y = 0
            elif y == 2:
                y = 2
            elif y == 3:
                y = 4
            self.Y = y
            if self.empty_space(x ,y):
                print(f"coordenadas validas {self.X},{self.Y}")
                return True
            else:
                print(f"coordenadas ya usadas {self.X},{self.Y}")
                return False
        else:
            print(f"coordenadas Invalidas {x},{y}")
            return False

    def empty_space(self ,x ,y):
        if self.board[x][y] == "_":
            return True
        else:
            return False

    def play_turn(self,x,y):
        if self.validate_coordinates(x,y) and self.status == "_":
            self.board[self.X][self.Y] = self.turn
            self.define_turn()
            self.game_status()
            return True
        else:
            return False

    def define_turn(self):
        if self.turn == "X":
            self.turn = "Y"
        else:
            self.turn = "X"

    def print_board(self):
        for x in range(0 ,3):
            row = ""
            for y in range(0 ,5):
                row = row + self.board[x][y]
            print(row)

    def game_status(self):
        if self.board[0][0] == "X" and self.board[0][2] == "X" and self.board[0][4] == "X":
            self.status = "X"
        elif self.board[1][0] == "X" and self.board[1][2] == "X" and self.board[1][4] == "X":
            self.status = "X"
        elif self.board[2][0] == "X" and self.board[2][2] == "X" and self.board[2][4] == "X":
            self.status = "X"
        elif self.board[0][0] == "X" and self.board[1][0] == "X" and self.board[2][0] == "X":
            self.status = "X"
        elif self.board[0][2] == "X" and self.board[1][2] == "X" and self.board[2][2] == "X":
            self.status = "X"
        elif self.board[0][4] == "X" and self.board[1][4] == "X" and self.board[2][4] == "X":
            self.status = "X"
        elif self.board[0][0] == "X" and self.board[1][2] == "X" and self.board[2][4] == "X":
            self.status = "X"
        elif self.board[2][0] == "X" and self.board[1][2] == "X" and self.board[0][4] == "X":
            self.status = "X"
        if self.board[0][0] == "Y" and self.board[0][2] == "Y" and self.board[0][4] == "Y":
            self.status = "Y"
        elif self.board[1][0] == "Y" and self.board[1][2] == "Y" and self.board[1][4] == "Y":
            self.status = "Y"
        elif self.board[2][0] == "Y" and self.board[2][2] == "Y" and self.board[2][4] == "Y":
            self.status = "Y"
        elif self.board[0][0] == "Y" and self.board[1][0] == "Y" and self.board[2][0] == "Y":
            self.status = "Y"
        elif self.board[0][2] == "Y" and self.board[1][2] == "Y" and self.board[2][2] == "Y":
            self.status = "Y"
        elif self.board[0][4] == "Y" and self.board[1][4] == "Y" and self.board[2][4] == "Y":
            self.status = "Y"
        elif self.board[0][0] == "Y" and self.board[1][2] == "Y" and self.board[2][4] == "Y":
            self.status = "Y"
        elif self.board[2][0] == "Y" and self.board[1][2] == "Y" and self.board[0][4] == "Y":
            self.status = "Y"
