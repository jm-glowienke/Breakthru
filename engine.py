from transition import Board
from negamax import NegaMax
import random

class Agent(object):
    # Engine receives board state, i.e. 2-d list as input
    # It makes a decision based on that and returns the next move

    def __init__(self,type,turn):
        # self.state = board.get_state()
        self.turn = turn
        self.type = type
        self.state = None

    def next_move_engine(self,board,depth = 1):
        # Start alpha-beta-algorithm
        agent = NegaMax(board,self.turn)
        value, move_list = agent.get_val(self.turn,depth,-30,30)
        print("Value of move: {}".format(value))
        src_1 = move_list[0][0]
        dest_1 = move_list[0][1]
        if move_list[1] != []:
            src_2 = move_list[1][0]
            dest_2 = move_list[1][1]
        else:
            src_2 = None
            dest_2 = None
            type_2 = None
        # Check if move is valid otherwise return random move
        correct_1, type_1 = board.is_move_valid(src_1,dest_1,2)
        if correct_1 != True:
            print("engine move invalid:")
            print(move_list)
            print("returning random move")
            return self.next_move_rand(self.turn,board)
        elif correct_1 == True:
            if type_1 == 13:
                dest_object = board.get_board()[dest_1[0]][dest_1[1]]
                board.make_simulated_move(self.turn,src_1,dest_1,1)
                correct_2, type_2 = board.is_move_valid(src_2,dest_2,1)
                board.undo_simulated_move(src_1,dest_1,dest_object)
                if correct_2 != True:
                    print("engine move invalid:")
                    print(move_list)
                    print("returning random move")
                    return self.next_move_rand(self.turn,board)
            return src_1, dest_1, src_2, dest_2, type_1, type_2
        print("returning random move")
        return self.next_move_rand(self.turn,board)

        return src, dest

    def next_move_rand(self,turn,board):
        # returns random legal move for player at turn
        moves = board.get_all_moves(turn)
        n_1 = len(moves)
        k = random.randint(0,n_1-1)
        src_1, dest_1 = moves[k][0],moves[k][1]
        n_2 = len(moves[k][2])
        if n_2 !=0:
            l = random.randint(0,n_2-1)
            src_2, dest_2 = moves[k][3][l][0], moves[k][3][l][1]
        else:
            src_2, dest_2 = None, None

        return src_1, dest_1, src_2, dest_2, None, None

    def next_move_manual(self,board):
        src_1, dest_1 = board.enter_manual_move()
        correct_1, type_1 = board.is_move_valid(src_1,dest_1)
        if correct_1 != True:
            raise ValueError
        if type_1 == 13:
            dest_object = board.get_board()[dest_1[0]][dest_1[1]]
            board.make_simulated_move(self.turn,src_1,dest_1,1)
            src_2, dest_2 = board.enter_manual_move()
            correct_2, type_2 = board.is_move_valid(src_2,dest_2,1)
            board.undo_simulated_move(src_1,dest_1,dest_object)
            if correct_2 != True:
                raise ValueError
            return src_1, dest_1, src_2, dest_2, type_1, type_2
        return src_1, dest_1, None, None, type_1, None

    def get_move(self,board,N = None):
        if self.type == 'manual':
            return self.next_move_manual(board)
        elif self.type == 'engine':
            if N == 0 and self.turn == 'gold':
                src_1, dest_1, src_2, dest_2,type_1, type_2 = [3,4],[4,4],[3,6],[4,6],13,13
            elif N == 2 and self.turn == 'gold':
                src_1, dest_1, src_2, dest_2,type_1, type_2 = [7,4],[6,4],[7,6],[6,6],13,13
            else:
                src_1, dest_1, src_2, dest_2,type_1,type_2 = self.next_move_engine(board)
            print("Engine gives:")
            print("{0} {1} {2} {3}".format(chr(src_1[1]+97),11-src_1[0],chr(dest_1[1]+97),11-dest_1[0]))
            if src_2 != None:
                print("{0} {1} {2} {3}".format(chr(src_2[1]+97),11-src_2[0],chr(dest_2[1]+97),11-dest_2[0]))
            return src_1, dest_1, src_2, dest_2, type_1, type_2
        else:
            print("Something wrong with type of agent")
            raise Exception
