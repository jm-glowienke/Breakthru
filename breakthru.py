from transition import Board
from tools import initial_state

board_list = initial_state()

board = Board(board_list,'gold')

board.show_state()

print(board.get_number_pieces('gold'))
