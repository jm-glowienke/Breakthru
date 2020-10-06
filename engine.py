from transition import Board
import random

class Agent(object):
    # Engine receives board state, i.e. 2-d list as input
    # It makes a decision based on that and returns the next move

    def __init__(self,type,turn):
        # self.state = board.get_state()
        self.turn = turn
        self.type = type

    # is this really necessary?
    # def update_state(self,new_state):
    #     # Update agent's state with state passed
    #     try:
    #         self.state = new_state
    #         return True
    #     except Exception as e:
    #         print("Error updating agent's state: {}".format(e))
    #         return False

    def next_move_engine(self,turn):
        # Start alpha-beta-algorithm

        # NEED TO BE ADAPTED
        # # Initialize a minimax tree.
        # decisionTree = Minimax_Agent(current_state, turn, self.utility)
        # decisions = decisionTree.get_val()
        # dest = decisions[0]
        # move_direction = decisions[1]

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
            src_2, dest_2 = moves[k][2][l][0], moves[k][2][l][1]
        else:
            src_2, dest_2 = None, None

        return src_1, dest_1, src_2, dest_2

    def next_move_manual(self,board):
        print(board.get_turn())
        print(board.get_moves_left())
        src_1, dest_1 = board.enter_manual_move()
        src_2, dest_2 = board.enter_manual_move()

        return src_1, dest_1, src_2, dest_2

    def get_move(self,board):
        if self.type == 'manual':
            return self.next_move_manual(board)
        elif self.type == 'engine':
            src_1, dest_1, src_2, dest_2 = self.next_move_rand(self.turn,board) # NEEDS TO BE CHANGED TO PROPER ENGINE
            print("Engine gives:")
            print("{0} {1} {2} {3}".format(chr(src_1[1]+97),11-src_1[0],chr(dest_1[1]+97),11-dest_1[0]))
            if src_2 != None:
                print("{0} {1} {2} {3}".format(chr(src_2[1]+97),11-src_2[0],chr(dest_2[1]+97),11-dest_2[0]))
            return src_1, dest_1, src_2, dest_2
        else:
            print("Something wrong with type of agent")
            raise Exception
