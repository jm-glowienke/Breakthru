from transition import Board
from tools import initial_state

board_list = initial_state()

board = Board(board_list)

board.show_state()

src = [0,0]
dest = [0,0]
src[1] = 2
dest[1] = 6
dest[0] = 5
src[0] = 5
for i in range(min(src[0],dest[0]),max(src[0],dest[0])):
    print(board_list[i][src[1]])
    if board_list[i][src[1]] != '.':
        print("False")
for i in range(min(src[1],dest[1]),max(src[1],dest[1])):
    print(board_list[src[0]][i])
    if board_list[src[0]][i] != '.':
        print("False")
