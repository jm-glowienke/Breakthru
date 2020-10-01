from transition import Board
from tools import initial_state

# board_list = initial_state()

test_1 =    [
            [1,".",".",".",".",".",".",".",".",".","."],
            [".",2,".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."]]

board = Board(initial_state())

moves = board.get_all_moves('silver')

# #print(len(moves))
# #moves[0].append([[1,2],[3,4]])
# #print(moves)
# # sum = 0
# cnt = 0
# cnt1 = 0
# for move in moves:
#     bool1,moves_left = board.is_move_valid2(move[0],move[1],2)
#     board.make_simulated_move('silver',move[0],move[1],2)
#     moves_left_old = moves_left
#     if bool1 == True:
#         for move2 in move[2]:
#             cnt1 += 1
#             bool2,moves_left = board.is_move_valid2(move2[0],move2[1],moves_left_old)
#             if bool2 == False:
#                 print(move2[0],move2[1])
#                 print("False 2nd move")
#                 board.show_state()
#                 continue
#             cnt += 1
#         board = Board(initial_state())
#     else:
#         print(move2[0],move2[1])
#         print(False)
# print(cnt,cnt1)
# count = 0
#
# for move in moves:
#     count += 1
#     count += len(move[2])
# print(count)
# # print(len(moves[0]))
# # print(moves[0][0])
# # print(moves[0][1])
# # print(moves[0][2])
