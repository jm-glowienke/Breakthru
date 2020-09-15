from transition import Board
from tools import initial_state

board_list = initial_state()


board = Board(board_list)

# board.show_state()

a = [[[1, 5], [0, 5]], [[9, 5], [10, 5]]]

print(a[0][1])
