import unittest

from board.board import Board
from game import Game


class GameTestCase(unittest.TestCase):

    def test_live_cell_with_less_than_two_live_neighbours_dies(self):
        board = Board(
            [
                [True, True, True]
            ]
        )
        self.game = Game(board)

        self.game.go_to_next_generation()

        self.assertEqual(
            [
                [False, True, False]
            ],
            self.game.get_board()
        )

    def test_live_cell_with_more_than_three_live_neighbours_dies(self):
        board = Board(
            [
                [True, True, True],
                [True, True, True]
            ]
        )
        self.game = Game(board)

        self.game.go_to_next_generation()

        self.assertEqual(
            [
                [True, False, True],
                [True, False, True]
            ],
            self.game.get_board()
        )

    def test_a_dead_cell_having_three_live_neighbours_becomes_a_live_cell(self):
        board = Board(
            [
                [True, True],
                [True, False]
            ]
        )
        self.game = Game(board)

        self.game.go_to_next_generation()

        self.assertEqual(
            [
                [True, True],
                [True, True]
            ],
            self.game.get_board()
        )
