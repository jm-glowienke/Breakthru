## # TODO:
## Store moves
## Time stamps
## skip first move for gold
## not move same ship twice should be implemented
## problem with stone check

from transition import Board
from tools import initial_state

board_list = initial_state()

board = Board(board_list)

board.show_state()

while board.is_terminal() != True:
    try:
        src, dest = board.enter_manual_move()
        if board.make_a_move(board.get_turn(),src, dest) == False:
            raise ValueError
        board.show_state()
    except ValueError:
        print("Try again:")
