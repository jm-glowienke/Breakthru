from transition import Board
import random

class NegaMax(object):

    def __init__(self,board,player):
        self.state = board
        # self.sim_board = self.state.get_board()
        self.player = player
        self.score = -9999999

    def get_opponent(self,player):
        if player == 'gold':
            return 'silver'
        elif player == 'silver':
            return 'gold'
        else: raise Exception

    def get_val(self,player,depth,alpha,beta):
        # run NegaMax algorithm
        if depth == 0 or self.state.is_terminal() == True:
            return self.utility(self.state)
        self.score = -9999999

        childNodes = self.state.get_all_moves(player)
        # childNodes = order_moves(childNodes)
        # print(childNodes)
        print(len(childNodes))
        print(player)
        # print(self.state.get_turn())
        # print(self.state.get_moves_left())
        for child in childNodes:
            print('NEW CHILD')
            print(player)
            # print(self.state.get_turn())
            print(child)
            src = child[0]
            dest = child[1]
            dest_object = self.state.get_board()[dest[0]][dest[1]]
            moves_left = self.state.make_simulated_move(player, src, dest, 2)
            # print(child)
            self.state.show_state()
            if moves_left == 0: # single move perfomed
                # self.state.switch_player_at_turn()
                value = -self.get_val(self.get_opponent(player),depth - 1,-beta,-alpha)
                self.state.undo_simulated_move(src,dest,dest_object)
                if value > self.score: self.score = value
                if self.score > alpha: alpha = self.score
                if self.score >= beta: break
            elif moves_left == 1: # two moves performed
                for child2 in child[2]:
                    src_2 = child2[0]
                    dest_2 = child2[1]
                    dest_object_2 = self.state.get_board()[dest_2[0]][dest_2[1]]
                    moves_left = self.state.make_simulated_move(player,src_2,dest_2,1)

                    self.state.show_state()
                    # self.state.switch_player_at_turn()
                    value = -self.get_val(self.get_opponent(player),depth-1,-beta,-alpha)
                    self.state.undo_simulated_move(src_2,dest_2,dest_object_2)
                    if value > self.score: self.score = value
                    if self.score > alpha: alpha = score
                    if self.score >= beta: break
                self.state.undo_simulated_move(src,dest,dest_object)

        return self.score


    def order_moves(childNodes):
        return False

    def utility(self,state):
        return random.randint(0,20)
