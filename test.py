from transition import Board
from tools import initial_state

board_list = initial_state()


board = Board(board_list)

import signal

valid_signals = signal.valid_signals()

print(valid_signals)
