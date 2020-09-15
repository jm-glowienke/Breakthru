# Everything needed to make transitions


class Board(object):

    def __init__(self,board_list, turn = 'gold'):
        self.board = board_list
        self.playerG = 'gold'
        self.playerS = 'silver'
        self.turn = turn
        self.opponent = 'silver'
        self.game_over = False
        self.total_num_playerG = 13#self.get_number_pieces(self.playerG)
        self.total_num_playerS = 20#self.get_number_pieces(self.playerS)
        self.moves_left = 2
        self.height = 11
        self.width = 11

    def is_game_over(self):
        return self.game_over

    def get_turn(self):
        return self.turn

    def get_current_state(self):
        return current_state

    def get_moves_left(self):
        return self.moves_left

    def switch_player_at_turn(self):
        if self.turn == self.playerG:
            self.turn = self.playerS
            self.opponent = self.playerG
            self.moves_left = 2
        elif self.turn == self.playerS:
            self.turn == self.playerG
            self.opponent = self.playerS
            self.moves_left = 2
        else: raise Exception("Player not existent")
        return


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
        # returns whether move is valid adn adapts variable self.moves_left
        type = -99 # 10 = normal, 11 = capture
        old_moves_left = self.moves_left
        # Check for basic incorrects
        if src[0] == dest[0] and src[1] == dest[1]: # Eliminate when source equals destination
            Print("src == dest")
            return False
        elif self.get_player_at_field(dest) == self.turn:
            Print("destination field has own stone")
            return False

        # Determine type of move, check if enough moves left, adapt moves left
        if self.get_player_at_field(dest) == self.opponent and self.moves_left < 2:
            self.moves_left = old_moves_left
            print("2nd move cannot be a capture")
            return False
        elif self.get_player_at_field(dest) == self.opponent:
            type = 11
            self.moves_left -= 2
        elif self.board[src[0]][src[1]] == 3 and self.moves_left < 2:
            print("2nd move cannot move the flagship")
            self.moves_left = old_moves_left
            return False
        elif self.board[src[0]][src[1]] == 3 and self.get_player_at_field(dest) == self.opponent:
            type = 11
            self.moves_left -= 2
        elif self.board[src[0]][src[1]] == 3 and self.get_player_at_field(dest) == 'empty':
            type = 10
            self.moves_left -= 2
        elif self.get_player_at_field(dest) == 'empty':
            type = 10
            self.moves_left -= 1
        else:
            print("Move definition went wrong")
            raise Exception

        # Check if move is valid
        if type == 11: # check for capture move
            if abs(src[0] - dest[0]) == 1 and abs(src[1] == dest[1]) == 1:
                return True
            else:
                self.moves_left = old_moves_left
                return False
        elif type == 10: # check for regular move
            if src[0] == dest[0]: # horizontal move
                for i in range(min(src[1],dest[1])+1,max(src[1],dest[1])):
                    if self.board[src[0]][i] != '.':
                        print("Cannot jump over stones!")
                        self.moves_left = old_moves_left
                        return False
                return True
            elif src[1] == dest[1]: # vertical move
                for i in range(min(src[0],dest[0])+1,max(src[0],dest[0])):
                    if self.board[i][src[1]] != '.':
                        print("Cannot jump over stones!")
                        self.moves_left = old_moves_left
                        return False
                return True
            else:
                print("Regular move went wrong")
                raise Exception
        else:
            print("Type not correctly defined")
            raise Exception

        self.moves_left = old_moves_left
        return False

    def get_player_at_field(self,pos):
        x = self.board[pos[0]][pos[1]]
        if x == 2 or x == 3:
            field = 'gold'
        elif x == 1:
            field = 'silver'
        elif x == '.':
            field = 'empty'
        else:
            raise Exception
        return field

    def enter_manual_move(self): #function to manually enter move using keyboard
        while True:
            try:
                print("Player {0}: It's your move! Format: <Z 99 Z 99>".format(self.turn.upper()))
                a, b, c, d = input().split()
                src = [int(b)-1, ord(a.lower())-96-1] # -1 since python indexing starts at 0
                dest = [int(d)-1, ord(c.lower())-96-1]
                if src[0] < 0 or src[0] > self.width - 1 or src[1] < 0 or src[1] > self.height - 1\
                or dest[0] < 0 or dest[0] > self.width - 1 or dest[1] < 0 or dest[1] > self.height - 1:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input! Try again and remember expected input format: <Z 99 Z 99>!")
        return src, dest # return integer lists for positions on board

    def make_a_move(self,player,src,dest):
        try:
            #validate turn - check if correct stone at starting field
            if self.turn != self.get_player_at_field(src):
                print("Source field is incorrect!")
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
            if self.moves_left < 1:
                self.switch_player_at_turn()
            return True

        except Exception as e:
            # Anything goes wrong
            print("Exception occured: ", e)
            return False

    def is_terminal(self):
        return False
