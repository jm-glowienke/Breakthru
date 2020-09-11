from transition import Board
from tools import initial_state

board_list = initial_state()
print("This is how the board looks like:")

board = Board(board_list,'gold')

board.show_state()
