from transition import Board
from tools import initial_state

board_list = initial_state()

board = Board(board_list,'gold')

board.show_state()

board.show_state()

print(board.get_number_pieces('gold'))

print(board.get_remaining_pieces('gold'))

print(board.get_turn())

board.switch_player_at_turn()

print(board.get_turn())
