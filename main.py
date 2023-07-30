import time

from matplotlib import pyplot as plt

from board.board import Board
from board.predefined_patterns.predefined_pattern import *
from game.game import Game

if __name__ == '__main__':
    board = Board(gosper_glider_gun)
    board.resize_by(100)
    game = Game(board)

    generation = 0
    pause_time = 0.01
    try:
        while generation < 100:
            game.go_to_next_generation()
            game.display_board()
            plt.title(f'Generation: {generation}')
            plt.pause(pause_time)
            generation += 1
    except KeyboardInterrupt:
        pass
