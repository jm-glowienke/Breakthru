from transition import Board
from tools import initial_state

board_list = initial_state()

board = Board(board_list,'gold')

board.show_state()

src, dest = board.enter_manual_move()

board.make_a_move('gold',src,dest)

board.show_state()
