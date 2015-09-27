from arrows import Arrow

class Game:

    def __init__(self):
        self.board = []
        for i in range(4):
            self.board.append([])
            for j in range(4):
                self.board[i].append(0)

    def play(self):
        key = Arrow.input()
        while key != Arrow.NONE:
            print(key)
            self.__print_board()
            key = Arrow.input()

        print("None of the arrow keys was pressed")

    def __print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])
