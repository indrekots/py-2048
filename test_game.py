import unittest
from game import Game

class TestGame(unittest.TestCase):

    def test_left_move(self):
        game = Game()
        initial = [[0, 2, 0, 4],
                   [0, 0, 2, 0],
                   [0, 0, 4, 4],
                   [2, 0, 0, 8]]
        next_step = [[2, 4, 0, 0],
                     [2, 0, 0, 0],
                     [4, 4, 0, 0],
                     [2, 8, 0, 0]]

        game.board = initial
        game.generate_next("LEFT")
        self.assertEqual(game.board, next_step, "States do not match")

if __name__ == '__main__':
    unittest.main()
