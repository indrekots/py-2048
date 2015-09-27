from arrows import Arrow

class Game:
    def play(self):
        key = Arrow.input()
        while key != Arrow.NONE:
            print(key)
            key = Arrow.input()

        print("None of the arrow keys was pressed")
