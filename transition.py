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

    def get_remaining_pieces(self,player): # is this really needed?
        difference = -99

        if player == playerG:
            diff = self.total_num_playerG - self.get_number_pieces(player)
        else:
            diff = self.total_num_playerS - self.get_number_pieces(player)

        return

    def get_number_pieces(self,player):
        counter = 0
        if player == 'gold':
            for row in self.board:
                for column in row:
                    if column == 2 or column == 3:
                        counter += 1
        else:
            for row in self.board:
                for column in row:
                    if column == 1:
                        counter += 1

        return counter

    def show_state(self):
        col = 1
        print("\n######################################################\n")
        for row in self.board:
            for column in row:
                #column = [column].append([col])
                print(column, end = '')
                col += 1
            print()
        print("######################################################\n")
        return

    def get_all_positions(self,player):
        return -9999999

    def get_all_moves(self,player):
        return -9999999

    def get_moves(self, player, pos):
        return -9999999

    def is_move_valid(self, src, dest):
        return -9999999
