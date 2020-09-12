# Everything needed to make transitions


class Board(object):

    def __init__(self,board_list, turn = 'gold'):
        self.board = board_list
        self.playerG = 'gold'
        self.playerS = 'silver'
        self.turn = turn
        self.game_over = False
        self.total_num_playerG = self.get_number_pieces(self.playerG)
        self.total_num_playerS = self.get_number_pieces(self.playerS)

    def is_game_over(self):
        return self.game_over

    def get_turn(self):
        return self.turn

    def get_current_state(self):
        return current_state

    def switch_player_at_turn(self):
        if self.turn == self.playerG:
            self.turn = self.playerS
        elif self.turn == self.playerS:
            self.turn == self.playerG
        else: raise Exception("Player not existent")

        return self.turn


    def get_remaining_pieces(self,player): # is this really needed?
        difference = -99

        if player == self.playerG:
            diff = self.total_num_playerG - self.get_number_pieces(player)
        elif player == self.playerS:
            diff = self.total_num_playerS - self.get_number_pieces(player)
        else: raise Exception("Player not existent")

        return

    def get_number_pieces(self,player):
        counter = 0
        if player == self.playerG:
            for row in self.board:
                for column in row:
                    if column == 2 or column == 3:
                        counter += 1
        elif player == self.playerS:
            for row in self.board:
                for column in row:
                    if column == 1:
                        counter += 1
        else: raise Exception("Player not existent")

        return counter

    def show_state(self):
        label_row = int(1)
        print("\n____________________________________________________")
        for element in ['A','B','C','D','E','F','G','H','I','J','K']:
            print(element, end=' ')
        print()
        for row in self.board:
            row.append(label_row)
            for column in row:
                print(column, end = ' ')
            print()
            label_row += 1
        print("____________________________________________________\n")
        return

    def get_all_positions(self,player):
        return -9999999

    def get_all_moves(self,player):
        return -9999999

    def get_moves(self, player, pos):
        return -9999999

    def is_move_valid(self, src, dest):
        return -9999999
