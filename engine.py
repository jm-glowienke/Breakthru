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

    # is this really necessary?
    # def update_state(self,new_state):
    #     # Update agent's state with state passed
    #     try:
    #         self.state = new_state
    #         return True
    #     except Exception as e:
    #         print("Error updating agent's state: {}".format(e))
    #         return False

    #  Function below can be improved when function is_move_valid is changed to not change the move_left
    def next_move_engine(self,board,depth = 1):
        # Start alpha-beta-algorithm
        self.state = board
        agent = NegaMax(self.state,self.turn)
        value, move_list = agent.get_val(self.turn,depth,-30,30)
        src_1 = move_list[0][0]
        dest_1 = move_list[0][1]
        if move_list[1] != []:
            src_2 = move_list[1][0]
            dest_2 = move_list[1][1]
        else:
            src_2 = None
            dest_2 = None
        # Check if move is valid otherwise return random move
        if self.state.is_move_valid(src_1,dest_1):
            # print(self.state.get_moves_left())
            if self.state.get_moves_left() == 1 and src_2 != None and self.state.is_move_valid(src_2,dest_2):
                # print("2nd move correct")
                # print(src_1,dest_1,src_2,dest_2)
                self.state.switch_player_at_turn()
                self.state.switch_player_at_turn()
                return src_1, dest_1, src_2, dest_2
            elif self.state.get_moves_left() == 0 and src_2 == None:
                # print("Only 1 move")
                # print(src_1, dest_1, src_2, dest_2)
                self.state.switch_player_at_turn()
                self.state.switch_player_at_turn()
                return src_1, dest_1, src_2, dest_2
        print("engine move invalid:")
        print(move_list)
        print("returning random move")
        self.state.switch_player_at_turn()
        self.state.switch_player_at_turn()
        return self.next_move_rand(self.turn,self.state)

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
        src_1, dest_1 = board.enter_manual_move()
        if abs(src_1[0]-dest_1[0]) == 1 and abs(src_1[1]-dest_1[1]) == 1:
            return src_1, dest_1, None, None
        elif board.get_board()[src_1[0]][src_1[1]] == 3:
            return src_1, dest_1, None, None
        else:
            src_2, dest_2 = board.enter_manual_move()
            return src_1, dest_1, src_2, dest_2

    def get_move(self,board,N = None):
        if self.type == 'manual':
            return self.next_move_manual(board)
        elif self.type == 'engine':
            if N == 0 and self.turn == 'gold':
                src_1, dest_1, src_2, dest_2 = [3,4],[4,4],[3,6],[4,6]
            elif N == 2 and self.turn == 'gold':
                src_1, dest_1, src_2, dest_2 = [7,4],[6,4],[7,6],[6,6]
            # elif self.turn == 'silver':
            else:
                # src_1, dest_1, src_2, dest_2 = self.next_move_rand(self.turn,board) # NEEDS TO BE CHANGED TO PROPER ENGINE
                src_1, dest_1, src_2, dest_2 = self.next_move_engine(board)
            print("Engine gives:")
            print("{0} {1} {2} {3}".format(chr(src_1[1]+97),11-src_1[0],chr(dest_1[1]+97),11-dest_1[0]))
            if src_2 != None:
                print("{0} {1} {2} {3}".format(chr(src_2[1]+97),11-src_2[0],chr(dest_2[1]+97),11-dest_2[0]))
            return src_1, dest_1, src_2, dest_2
        else:
            print("Something wrong with type of agent")
            raise Exception
