from transition import Board
from tools import initial_state

board_list = initial_state()


board = Board(board_list)

# board.show_state()

k = 0
for row in board_list:
    if 3 in row:
        print(row.index(3))
        if row.index(3) == 0 or row.index(3) == 10 \
        or k == 0 or k == 10:
            print("Gold wins")
        else:
            print("Continue")
    k += 1
# print("Silver wins")
