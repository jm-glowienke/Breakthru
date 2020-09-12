## # TODO:
## Store moves
## Time stamps
## skip first move for gold
## switching between players to be changed

from transition import Board
from tools import initial_state

board_list = initial_state()

board = Board(board_list,'gold')

board.show_state()

while board.is_terminal != True:
    src, dest = board.enter_manual_move()
    if board.make_a_move(board.get_turn(),src,dest) == False:
        raise Exception
    board.show_state()
