# Everything needed to make transitions


class Board(object):

    def __init__(self,board_list, turn = 'gold'):
        self.board = board_list
        self.playerG = 'gold'
        self.playerS = 'silver'
        self.turn = turn
        self.game_over = False
        self.total_num_playerG = 13#self.get_number_pieces(self.playerG)
        self.total_num_playerS = 20#self.get_number_pieces(self.playerS)
        self.moves_left = 2

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


    def get_remaining_pieces(self,player):
        difference = None

        if player == self.playerG:
            difference = self.total_num_playerG - self.get_number_pieces(player)
        elif player == self.playerS:
            difference = self.total_num_playerS - self.get_number_pieces(player)
        else: raise Exception("Player not existent")

        return difference

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
            del row[-1]
        print("____________________________________________________\n")
        return None

    def get_all_positions(self,player):
        return -9999999

    def get_all_moves(self,player):
        return -9999999

    def get_moves(self, player, pos):
        return -9999999

    def is_move_valid(self, src, dest):
        return True

    def get_player_at_field(self,pos): # function should return which player has it's stone at position asked
        return 'gold' # should return 'gold' or 'silver'

    def enter_manual_move(self): #function to manually enter move using keyboard
        print("Enter source and destination in following format: <Z 99 Z 99>:")
        a, b, c, d = input().split()
        src = [int(b)-1,ord(a.lower())-96-1] # -1 since python indexing starts at 0
        dest = [int(d)-1,ord(c.lower())-96-1]

        return src, dest # return integer lists for positions on board

    def make_a_move(self,player,src,dest):
        try:
            #validate turn
            if self.turn != self.get_player_at_field(src):
                print("Not your stone!")
                return False

            # validate move
            if self.is_move_valid(src,dest) != True:
                print("Irregular move!")
                return False

            # Make move
            self.board[dest[0]][dest[1]] = self.board[src[0]][src[1]]
            self.board[src[0]][src[1]] = '.' #reset old position

            # Flip turn to other player
            # change this because two moves in a row are possible, 1 capture or 1 for flag
            self.moves_left -= 1
            self.switch_player_at_turn()
            return True

        except Exception as e:
            # Anything goes wrong
            print("Exception occured: ", e)
            return False
