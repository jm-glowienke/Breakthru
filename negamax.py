from transition import Board
import random
import time

class NegaMax(object):

    def __init__(self,board,player):
        self.state = board
        # self.sim_board = self.state.get_board()
        self.player = player
        self.score = -9999999
        self.time = time.time()

    def get_opponent(self,player):
        if player == 'gold':
            return 'silver'
        elif player == 'silver':
            return 'gold'
        else: raise Exception

    def get_val(self,player,depth,alpha,beta):
        # print(alpha,beta)
        # run NegaMax algorithm
        if depth == 0 or self.state.is_terminal() == True:
            return self.utility(self.state,player),[]
        self.score = -9999999

        best_move = []
        childNodes = self.state.get_all_moves(player)
        childNodes = self.order_moves(childNodes)
        for child in childNodes:
            if time.time() - self.time > 30:
                print("Search timed out!")
                return self.score, best_move
            src = child[0]
            dest = child[1]
            dest_object = self.state.get_board()[dest[0]][dest[1]]
            moves_left = self.state.make_simulated_move(player, src, dest, 2)
            if moves_left == 0: # single move perfomed
                value, best_sub_move = self.get_val(self.get_opponent(player),depth - 1,-beta,-alpha)
                value = -value
                self.state.undo_simulated_move(src,dest,dest_object)
                if value > self.score: self.score = value
                if self.score > alpha:
                    alpha = self.score
                    best_move = [[src,dest]]
                    best_move.append(best_sub_move)
                if self.score >= beta:
                    break
            elif moves_left == 1: # two moves performed
                for child2 in child[3]:
                    src_2 = child2[0]
                    dest_2 = child2[1]
                    dest_object_2 = self.state.get_board()[dest_2[0]][dest_2[1]]
                    moves_left = self.state.make_simulated_move(player,src_2,dest_2,1)
                    value, best_sub_move = self.get_val(self.get_opponent(player),depth-1,-beta,-alpha)
                    value = -value
                    self.state.undo_simulated_move(src_2,dest_2,dest_object_2)
                    if value > self.score: self.score = value
                    if self.score > alpha:
                        alpha = self.score
                        best_move = [[src,dest]]
                        best_move.append([src_2,dest_2])
                        best_move.append(best_sub_move)
                    if self.score >= beta:
                        break
                self.state.undo_simulated_move(src,dest,dest_object)
        return self.score, best_move


    def order_moves(self,moves):
        moves.sort(key = lambda x: x[2])
        return moves

    def utility(self,state,player):
        if player == 'gold':
            if state.is_terminal() == True and state.get_winner() == 'GOLD':
                return 30
            elif state.is_terminal():
                return -30
            else:
                opp = self.get_opponent(player)
                flag_attack = 0
                attack = 0
                direct_access = 0
                flag_covered = 0
                positions = state.get_all_positions(player)
                number_ships_left = len(positions)
                silver_number_ships_left = state.get_number_pieces('silver')
                for pos in positions:
                    if pos[0]+1 <= 10 and pos[1]-1>=0 \
                    and state.get_player_at_field([pos[0]+1,pos[1]-1]) == opp:
                        if state.get_board()[pos[0]][pos[1]] == 3:
                            flag_attack += 1
                        else:
                            attack += 1
                    if pos[0]-1 >= 0 and pos[1]-1 >= 0 \
                    and state.get_player_at_field([pos[0]-1,pos[1]-1]) == opp:
                        if state.get_board()[pos[0]][pos[1]] == 3:
                            flag_attack += 1
                        else:
                            attack += 1
                    if pos[0]-1 >= 0 and pos[1]+1 <= 10 \
                    and state.get_player_at_field([pos[0]-1,pos[1]+1]) == opp:
                        if state.get_board()[pos[0]][pos[1]] == 3:
                            flag_attack += 1
                        else:
                            attack += 1
                    if pos[0]+1 <= 10 and pos[1]+1 <= 10 \
                    and state.get_player_at_field([pos[0]+1,pos[1]+1]) == opp:
                        if state.get_board()[pos[0]][pos[1]] == 3:
                            flag_attack += 1
                        else:
                            attack += 1
                    if state.get_board()[pos[0]][pos[1]] == 3:
                        k = 1
                        while (pos[0] - k) >= 0 and state.get_player_at_field([pos[0]-k,pos[1]]) == 'empty':
                            if pos[0] - k == 0:
                                direct_access += 1
                            k += 1
                        k = 1
                        while (pos[0] + k) <= 10 and state.get_player_at_field([pos[0]+k,pos[1]]) == 'empty':
                            if pos[0] + k == 10:
                                direct_access += 1
                            k += 1
                        k = 1
                        while (pos[1] - k) >= 0 and state.get_player_at_field([pos[0],pos[1]-k]) == 'empty':
                            if pos[0] - k == 0:
                                direct_access += 1
                            k += 1
                        k = 1
                        while (pos[1] + k) <= 10 and state.get_player_at_field([pos[0],pos[1]+k]) == 'empty':
                            if pos[1] + k == 10:
                                direct_access += 1
                            k += 1
                        if pos[0]+1 <= 10 and pos[1]-1>=0 \
                        and state.get_player_at_field([pos[0]+1,pos[1]-1]) == player:
                            flag_covered += 1
                        if pos[0]-1 >= 0 and pos[1]-1 >= 0 \
                        and state.get_player_at_field([pos[0]-1,pos[1]-1]) == player:
                            flag_covered += 1
                        if pos[0]-1 >= 0 and pos[1]+1 <= 10 \
                        and state.get_player_at_field([pos[0]-1,pos[1]+1]) == player:
                            flag_covered += 1
                        if pos[0]+1 <= 10 and pos[1]+1 <= 10 \
                        and state.get_player_at_field([pos[0]+1,pos[1]+1]) == player:
                            flag_covered += 1
            utility =  number_ships_left - 4*flag_attack - attack + 6 * direct_access + 3 * flag_covered - silver_number_ships_left
            return utility

        elif player == 'silver':
            if state.is_terminal() == True and state.get_winner() == 'SILVER':
                return 30
            elif state.is_terminal():
                return -30
            else:
                opp = self.get_opponent(player)
                flag_attack = 0
                attack = 0
                direct_access = 0
                flag_covered = 0
                positions = state.get_all_positions(player)
                number_ships_left = len(positions)
                gold_number_ships_left = state.get_number_pieces('gold')
                for pos in positions:
                    if pos[0]+1 <= 10 and pos[1]-1>=0 \
                    and state.get_player_at_field([pos[0]+1,pos[1]-1]) == opp:
                        if state.get_board()[pos[0]+1][pos[1]-1] == 3:
                            flag_attack += 1
                        else:
                            attack += 1
                    if pos[0]-1 >= 0 and pos[1]-1 >= 0 \
                    and state.get_player_at_field([pos[0]-1,pos[1]-1]) == opp:
                        if state.get_board()[pos[0]-1][pos[1]-1] == 3:
                            flag_attack += 1
                        else:
                            attack += 1
                    if pos[0]-1 >= 0 and pos[1]+1 <= 10 \
                    and state.get_player_at_field([pos[0]-1,pos[1]+1]) == opp:
                        if state.get_board()[pos[0]-1][pos[1]+1] == 3:
                            flag_attack += 1
                        else:
                            attack += 1
                    if pos[0]+1 <= 10 and pos[1]+1 <= 10 \
                    and state.get_player_at_field([pos[0]+1,pos[1]+1]) == opp:
                        if state.get_board()[pos[0]+1][pos[1]+1] == 3:
                            flag_attack += 1
                        else:
                            attack += 1
                # Analyse flagship situation
                k = 0
                for row in state.get_board():
                    if 3 in row:
                        pos = [k,row.index(3)]
                        if state.get_board()[pos[0]][pos[1]] == 3:
                            k = 1
                            while (pos[0] - k) >= 0 and state.get_player_at_field([pos[0]-k,pos[1]]) == 'empty':
                                if pos[0] - k == 0:
                                    direct_access += 1
                                k += 1
                            k = 1
                            while (pos[0] + k) <= 10 and state.get_player_at_field([pos[0]+k,pos[1]]) == 'empty':
                                if pos[0] + k == 10:
                                    direct_access += 1
                                k += 1
                            k = 1
                            while (pos[1] - k) >= 0 and state.get_player_at_field([pos[0],pos[1]-k]) == 'empty':
                                if pos[0] - k == 0:
                                    direct_access += 1
                                k += 1
                            k = 1
                            while (pos[1] + k) <= 10 and state.get_player_at_field([pos[0],pos[1]+k]) == 'empty':
                                if pos[1] + k == 10:
                                    direct_access += 1
                                k += 1
                            if pos[0]+1 <= 10 and pos[1]-1>=0 \
                            and state.get_player_at_field([pos[0]+1,pos[1]-1]) == opp:
                                flag_covered += 1
                            if pos[0]-1 >= 0 and pos[1]-1 >= 0 \
                            and state.get_player_at_field([pos[0]-1,pos[1]-1]) == opp:
                                flag_covered += 1
                            if pos[0]-1 >= 0 and pos[1]+1 <= 10 \
                            and state.get_player_at_field([pos[0]-1,pos[1]+1]) == opp:
                                flag_covered += 1
                            if pos[0]+1 <= 10 and pos[1]+1 <= 10 \
                            and state.get_player_at_field([pos[0]+1,pos[1]+1]) == opp:
                                flag_covered += 1
                    else:
                        k+= 1
            utility =  number_ships_left + 4*flag_attack + attack - 6 * direct_access - 3 * flag_covered - gold_number_ships_left
            return utility
