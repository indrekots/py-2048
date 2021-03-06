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

    def generate_next(self, direction):
        for row in self.board:
            self.__shift_elems_left(row)

    def __shift_elems_left(self, row):
        for i in range(len(row)):
            if i > 0 and row[i] != 0:
                best_spot = self.__find_best_pos(i, row)
                row[best_spot] = row[i]
                row[i] = 0

    def __find_best_pos(self, i, row):
        best_spot = i
        for j in range(i-1, -1, -1):
            if row[j] != 0:
                break
            else:
                best_spot = j
        return best_spot
