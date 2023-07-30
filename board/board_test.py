import unittest

from board import Board


class BoardTestCase(unittest.TestCase):
    def test_can_get_dimensions_from_board(self):
        board = Board([[True, True, True]])
        self.assertEqual(board.get_rows_number, 1)
        self.assertEqual(board.get_columns_number, 3)

    def test_can_resize_board(self):
        board = Board([[True]])
        board.resize_by(3)

        self.assertEqual(
            [
                [False, False, False],
                [False, True, False],
                [False, False, False]
            ],
            board.get_cells()
        )
