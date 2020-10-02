from transition import Board
import random

class Agent(object):
    # Engine receives board state, i.e. 2-d list as input
    # It makes a decision based on that and returns the next move

    def __init__(self,current_state,turn):
        self.state = current_state
        self.turn = turn

    # is this really necessary?
    def update_state(self,new_state):
        # Update agent's state with state passed
        try:
            self.state = new_state
            return True
        except Exception as e:
            print("Error updating agent's state: {}".format(e))
            return False

    def next_move(self,current_state, turn):
        # Start alpha-beta-algorithm

        # NEED TO BE ADAPTED
        # # Initialize a minimax tree.
        # decisionTree = Minimax_Agent(current_state, turn, self.utility)
        # decisions = decisionTree.get_val()
        # dest = decisions[0]
        # move_direction = decisions[1]

        return src, dest

    def next_move_rand(self,current_state,turn):
        # returns random legal move for player at turn

        moves = board.get_all_moves(turn)

        n_1 = len(moves)
        k = random.randint(0,n_1)
        src_1, dest_1 = moves[k][0],moves[k][1]
        n_2 = len(moves[k][2])
        if n_2 !=0:
            l = random.randint(0,n_2)
            src_2, dest_2 = moves[k][2][l][0], moves[k][2][l][1]
        else:
            src_2, dest_2 = None, None

        return src_1, dest_1, src_2, dest_2
