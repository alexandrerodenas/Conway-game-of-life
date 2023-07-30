import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

from board.board import Board


class BoardUI:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.grid(True)

    def display_board(self, board: Board):
        self.ax.clear()
        self.__color_board(board)
        self.__set_axis(board)
        plt.draw()

    def __color_board(self, board):
        np_matrix = np.array(board.get_cells())
        custom_cmap = ListedColormap(['white', 'black'])
        self.ax.imshow(
            np_matrix,
            cmap=custom_cmap,
            origin='lower',
            extent=[0, board.get_columns_number, 0, board.get_rows_number]
        )

    def __set_axis(self, board):
        self.ax.set_yticks(range(board.get_rows_number + 1))
        self.ax.set_xticks(range(board.get_columns_number + 1))
        self.ax.tick_params(
            which='both',
            bottom=False,
            left=False,
            labelbottom=False,
            labelleft=False,
            direction='inout'
        )
