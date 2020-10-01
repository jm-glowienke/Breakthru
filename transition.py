# Everything needed to make transitions
import time

class Board(object):

    def __init__(self,board_list, turn = 'gold'):
        self.board = board_list
        self.playerG = 'gold'
        self.playerS = 'silver'
        self.turn = turn
        self.opponent = 'silver'
        self.game_over = False
        self.winner = None
        self.total_num_playerG = 13#self.get_number_pieces(self.playerG)
        self.total_num_playerS = 20#self.get_number_pieces(self.playerS)
        self.moves_left = 2
        self.height = 11
        self.width = 11
        self.last_dest = [99,99]
        self.history = []
        self.elapsed_timeG = 0
        self.elapsed_timeS = 0
        self.end_time = 0

    def is_game_over(self):
        return self.game_over

    def get_winner(self):
        return self.winner.upper()

    def get_history(self):
        return self.history

    def gold_skips(self):
        self.history.append([[99,0],[0,0],0])
        return

    def add_to_history(self,old_history): # probably not needed
        n = len(old_history)
        for i in range(0,n):
            self.history.append(old_history[i])
        return

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
            self.turn = self.playerG
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
        label_row = int(11)
        print("\n____________________________________________________")
        for element in ['A','B','C','D','E','F','G','H','I','J','K']:
            print(element, end=' ')
        print()
        for row in self.board:
            row.append(label_row)
            for column in row:
                print(column, end = ' ')
            print()
            label_row -= 1
            del row[-1]
        print("____________________________________________________\n")
        return None

    def get_all_positions(self,player):
        # Returns all positions occupied by certain player
        pos_found = []
        x = 0
        for row in self.board:
            y = 0
            for item in row:
                if self.get_player_at_field([x,y]) == player:
                    pos_found.append([x,y])
                y += 1
            x += 1
        return pos_found

    def get_all_moves(self,player):
        # Returns datastructure with all possible moves
        # A move can include moving two ships
        moves_found = []
        all_positions = self.get_all_positions(player)
        opp = self.get_opponent(player)

        # get all possible first moves
        for pos in all_positions:
            # moves_left = 2
            # while moves_left != 0:
            # if pos[0] != 0 or pos[0] != 10 or pos[1] != 0 or pos[1] != 10:
                # position is not on the edge of the board
                # possibility for capture move
            if self.get_player_at_field([pos[0]+1,pos[1]-1]) == opp \
            and pos[0]+1 <= 10 and pos[1]-1>=0:
                moves_found.append([pos,[pos[0]+1,pos[1]-1]])
            if self.get_player_at_field([pos[0]-1,pos[1]-1]) == opp \
            and pos[0]-1 >= 0 and pos[1]-1 >= 0:
                moves_found.append([pos,[pos[0]-1,pos[1]-1]])
            if self.get_player_at_field([pos[0]-1,pos[1]+1]) == opp \
            and pos[0]-1 >= 0 and pos[1]+1 <= 10:
                moves_found.append([pos,[pos[0]-1,pos[1]+1]])
            if self.get_player_at_field([pos[0]+1,pos[1]+1]) == opp \
            and pos[0]+1 <= 10 and pos[1]+1 <= 10:
                moves_found.append([pos,[pos[0]+1,pos[1]+1]])
            # check for regular moves
            # if self.get_player_at_field([pos[0]-1,pos[1]]) == 'empty':
            #     moves_found.append([pos,[pos[0]-1,pos[1]]])
            k = 1
            while (pos[0] - k) >= 0 and self.get_player_at_field([pos[0]-k,pos[1]]) == 'empty':
                moves_found.append([pos,[pos[0]-k,pos[1]]])
                k += 1
            # if self.get_player_at_field([pos[0]+1,pos[1]]) == 'empty':
                # moves_found.append([pos,[pos[0]+1,pos[1]]])
            k = 1
            while (pos[0] + k) <= 10 and self.get_player_at_field([pos[0]+k,pos[1]]) == 'empty':
                moves_found.append([pos,[pos[0]+k,pos[1]]])
                k += 1
            # if self.get_player_at_field([pos[0],pos[1]-1]) == 'empty':
                # moves_found.append([pos,[pos[0],pos[1]-1]])
            k = 1
            while (pos[1] - k) >= 0 and self.get_player_at_field([pos[0],pos[1]-k]) == 'empty':
                moves_found.append([pos,[pos[0],pos[1]-k]])
                k += 1
            # if self.get_player_at_field([pos[0],pos[1]+1]) == 'empty':
                # moves_found.append([pos,[pos[0],pos[1]+1]])
            k = 1
            while (pos[1] + k) <= 10 and self.get_player_at_field([pos[0],pos[1]+k]) == 'empty':
                moves_found.append([pos,[pos[0],pos[1]+k]])
                k += 1
            # moves_left = 0 # can be removed when while loop is removed
            # get second moves, if possible
            n = 0 # used to append 2nd moves to first moves in list
            sum = 0
            for move in moves_found:
                src = move[0]
                dest = move[1]
                dest_object = self.board[dest[0]][dest[1]]
                moves_left = self.make_simulated_move(player, src, dest, 2)
                if moves_left < 1:
                    sum+= 1
                    moves_found[n].append([]) # no second move gives empty list
                    self.undo_simulated_move(src,dest,dest_object)
                    n += 1
                    continue # skip to next possible move

                all_positions_2 = self.get_all_positions(player) # this could be made faster by just changing the one position which was moved
                all_positions_2.remove(dest) # same ship cannot move twice
                for pos in all_positions_2:
                    # check for regular moves, only regular move can be second move
                    k = 1
                    while (pos[0] - k) >= 0 and self.get_player_at_field([pos[0]-k,pos[1]]) == 'empty':
                        moves_found[n].append([pos,[pos[0]-k,pos[1]]])
                        k += 1

                    k = 1
                    while (pos[0] + k) <= 10 and self.get_player_at_field([pos[0]+k,pos[1]]) == 'empty':
                        moves_found[n].append([pos,[pos[0]+k,pos[1]]])
                        k += 1

                    k = 1
                    while (pos[1] - k) >= 0 and self.get_player_at_field([pos[0],pos[1]-k]) == 'empty':
                        moves_found[n].append([pos,[pos[0],pos[1]-k]])
                        k += 1

                    k = 1
                    while (pos[1] + k) <= 10 and self.get_player_at_field([pos[0],pos[1]+k]) == 'empty':
                        moves_found[n].append([pos,[pos[0],pos[1]+k]])
                        k += 1
                self.undo_simulated_move(src,dest,dest_object)
                n += 1
        print(sum)
        return moves_found

    def get_moves(self, player, pos):
        return -9999999

    def is_move_valid(self, src, dest):
        # returns whether move is valid and adapts variable self.moves_left
        type = -99 # 10 = normal, 11 = capture
        old_moves_left = self.moves_left
        # Check for basic incorrects
        if src[0] == dest[0] and src[1] == dest[1]: # Eliminate when source equals destination
            print("source == destination")
            return False
        elif self.get_player_at_field(dest) == self.turn:
            print("destination field has own stone")
            return False
        elif self.moves_left == 1 and src == self.last_dest:
            print("same ship cannot move twice")
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
            if abs(src[0] - dest[0]) == 1 and abs(src[1] - dest[1]) == 1:
                return True
            else:
                print("Illegal capture move")
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
                return False
        else:
            print("Type not correctly defined")
            raise Exception

        self.moves_left = old_moves_left
        print("Move validation went completely wrong")
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
                print("Player {0}: It's your move! Format: <Z 99 Z 99>".format(self.turn.upper())\
                + "\n <-1 0 0 0> to undo last move")
                a, b, c, d = input().split()
                if a == '-1':
                    return None,None
                src = [11-int(b), ord(a.lower())-96-1] # -1 since python indexing starts at 0
                dest = [11-int(d), ord(c.lower())-96-1]
                if src[0] < 0 or src[0] > self.width - 1 or src[1] < 0 or src[1] > self.height - 1\
                or dest[0] < 0 or dest[0] > self.width - 1 or dest[1] < 0 or dest[1] > self.height - 1:
                    raise IndexError
                break
            except IndexError:
                print("Invalid input! Try again and remember expected input format: <Z 99 Z 99>!")
        # return integer lists for positions on board
        return src, dest

    def make_a_move(self,player,src,dest,start_time,elapsed_time = 0):
        try:
            #validate turn - check if correct stone at starting field
            if player != self.get_player_at_field(src):
                print("Source field is incorrect!")
                return False

            # validate move
            if self.is_move_valid(src,dest) != True:
                print("Irregular move!")
                return False

            self.end_time = time.time()
            # Make move
            self.board[dest[0]][dest[1]] = self.board[src[0]][src[1]]
            self.board[src[0]][src[1]] = '.' #reset old position
            self.last_dest = dest # save last destination


            # save moves to history
            self.history.append([src,dest])

            self.tracking_time(start_time,elapsed_time)

            # Flip turn to other player
            if self.moves_left < 1:
                self.switch_player_at_turn()
            return True

        except Exception as e:
            # Anything goes wrong
            print("Exception occured: ", e)
            return False

    def is_terminal(self):
        k = 0
        for row in self.board:
            if 3 in row:
                if row.index(3) == 0 or row.index(3) == 10 \
                or k == 0 or k == 10:
                    self.winner = self.playerG
                    return True # flagship found on edges of board
                else:
                    return False # no terminal state --> continue
            k += 1
        # no 3 found on board = silver wins
        self.winner = self.playerS
        return True

    def undo_last_move(self):
        src = self.history[-1][1] # opposite direction
        dest = self.history[-1][0]
        elapsed_time = self.history[-1][2]
        del self.history[-1]
        self.winner = None

        # reset total elapsed time per player
        if self.turn == self.playerG:
            self.elapsed_timeG -= int(elapsed_time)

        elif self.turn == self.playerS:
            self.elapsed_timeS -= int(elapsed_time)
        print("Silver:%s " % self.elapsed_timeS)
        print("Gold:%s " % self.elapsed_timeG)
        if self.moves_left == 1:
            self.board[dest[0]][dest[1]] = self.board[src[0]][src[1]]
            self.board[src[0]][src[1]] = '.' #reset old position
            self.moves_left += 1
            return True
        elif self.moves_left == 2:
            self.switch_player_at_turn()
            if self.turn == self.playerG :
                if self.board[src[0]][src[1]] == 3: # flag ship moved
                    if abs(src[0]-dest[0]) == 1 and abs(src[1]-dest[1]) == 1: # capture
                        self.board[dest[0]][dest[1]] = self.board[src[0]][src[1]]
                        self.board[src[0]][src[1]] = 1 #reset old position
                        return True
                    elif src[0] == dest[0] or src[1] == dest[1]: # regular
                        self.board[dest[0]][dest[1]] = self.board[src[0]][src[1]]
                        self.board[src[0]][src[1]] = '.' #reset old position
                        return True
                elif self.board[src[0]][src[1]] == 2: # escort moved
                    if abs(src[0]-dest[0]) == 1 or abs(src[1]-dest[1]) == 1: # capture
                        self.board[dest[0]][dest[1]] = self.board[src[0]][src[1]]
                        self.board[src[0]][src[1]] = 1 #reset old position
                        self.moves_left = 2
                        return True
                    elif src[0] == dest[0] and src[1] == dest[1]: # regular
                        self.board[dest[0]][dest[1]] = self.board[src[0]][src[1]]
                        self.board[src[0]][src[1]] = '.' #reset old position
                        self.moves_left = 1
                        return True
                    else: return False
                else: return False
            elif self.turn == self.playerS:
                 if abs(src[0]-dest[0]) == 1 and abs(src[1]-dest[1]) == 1: # capture
                     self.board[dest[0]][dest[1]] = self.board[src[0]][src[1]]
                     for row in self.board:
                         if 3 in row: # flagship was not captured
                            self.board[src[0]][src[1]] = 2
                            return True
                     self.board[src[0]][src[1]] =  3
                        #reset old position
                     return True
                 elif src[0] == dest[0] or src[1] == dest[1]: # regular
                     self.board[dest[0]][dest[1]] = self.board[src[0]][src[1]]
                     self.board[src[0]][src[1]] = '.' #reset old position
                     return True
                 else: return False
        else:   return False

    def tracking_time(self,start_time,elapsed_time = 0):
        if elapsed_time != 0: # possibility to edit time for loading of game
            if self.turn == self.playerG:
                self.elapsed_timeG += int(elapsed_time)
                self.history[-1].append(int(elapsed_time))
            elif self.turn == self.playerS:
                self.elapsed_timeS += elapsed_time
                self.history[-1].append(int(elapsed_time))
            return
        else:
            if self.turn == self.playerG:
                elapsed_time = self.end_time - start_time
                self.elapsed_timeG += elapsed_time
                self.history[-1].append(int(elapsed_time))
            elif self.turn == self.playerS:
                elapsed_time = self.end_time - start_time
                self.elapsed_timeS += elapsed_time
                self.history[-1].append(int(elapsed_time))
        return

    def get_time_left(self):
        if self.get_turn() == self.playerG:
            return 600 - self.elapsed_timeG
        else:
            return 600 - self.elapsed_timeS

    def get_opponent(self,player):
        if player == self.playerG:
            return self.playerS
        elif player == self.playerS:
            return self.playerG
        else: raise Exception

    def make_simulated_move(self,player,src,dest,moves_left):
        try:
            # validate move -- can be deleted later, just for control purposes right now
            # if self.is_move_valid(src,dest) != True:
            #     print("Irregular move!")
            #     return False

            # Determine type of move, adapt moves left
            if self.get_player_at_field(dest) == self.get_opponent(player):
                moves_left -= 2
            elif self.board[src[0]][src[1]] == 3:
                moves_left -= 2
                print("flagship moved")
            elif self.get_player_at_field(dest) == 'empty':
                moves_left -= 1
            else:
                print("Adapting moves_left simulation gone wrong")
                raise Exception

            # Make move
            self.board[dest[0]][dest[1]] = self.board[src[0]][src[1]]
            self.board[src[0]][src[1]] = '.' #reset old position

            return moves_left

        except Exception as e:
            # Anything goes wrong
            print("Exception occured: ", e)
            return False

    def undo_simulated_move(self,src,dest,dest_object):
        # function to undo simulated move, where src and dest are from original move
        self.board[src[0]][src[1]] = self.board[dest[0]][dest[1]]
        self.board[dest[0]][dest[1]] = dest_object
        return True
