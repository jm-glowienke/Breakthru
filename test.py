from transition import Board
from tools import initial_state,read_game_log
import random
from negamax import NegaMax

# board_list = initial_state()

test_1 =    [
            [1,".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",3,".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".","."]]

board = Board(initial_state())
# board = Board(test_1)

# log = read_game_log("log_20201004-141438")
# for i in range(0,len(log)):
#     turn = board.get_turn()
#     print("Player {} moves".format(turn.upper()))
#     board.make_a_move(board.get_turn(),log[i][0],log[i][1],0,elapsed_time = log[i][2])
#     board.show_state()
# print("\n Continuing old game...")

agent = NegaMax(board,'gold')

x = agent.get_val('gold',depth = 2,alpha = 20,beta = 0)

print(x)






# agents = { 1: 'manual - manual',
#     2: 'engine - manual',
#     3: 'manual - engine',
#     4: 'engine - engine'
#     }
# print("    gold - silver \n   --------------")
# for i in range(1,5):
#     print("{0} : {1}".format(i, agents[i]))

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
