from board.board import Board
from ui.board_ui import BoardUI


class Game:
    def __init__(self, board: Board):
        self.__board = board
        self.__boardUI = BoardUI()

    def go_to_next_generation(self):
        self.__board = self.__board.compute_next_generation()

    def get_board(self):
        return self.__board.get_cells()

    def display_board(self):
        self.__boardUI.display_board(self.__board)

