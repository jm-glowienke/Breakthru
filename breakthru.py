## # TODO:
## Store moves
## Time stamps
## loading of old game
## choice possibility which player engine has to play

from transition import Board
import tools
import os
import time

# Initialization
os.system('clear')
board = Board(tools.initial_state())


# Game starts
print("Welcome to Breakthru! \n Press 1 for new game and 2 to continue old game:")
choice = int(input())
if choice == 1:
    print("Player GOLD: Do you want to skip your first move? [y/n]")
    skip = input()
    if skip.lower() == 'y':
        board.gold_skips()
        board.switch_player_at_turn()
    board.show_state()
elif choice == 2:
    while True:
        try:
            print("Enter the name of the file you want to load:")
            file = input()
            log = tools.read_game_log(file)
            if log[0][0][0] == 99:
                print("Gold skipped first move")
                board.switch_player_at_turn()
                board.gold_skips()
                del log[0]
            board.show_state()
            for i in range(0,len(log)):
                turn = board.get_turn()
                print("Player {} moves".format(turn.upper()))
                board.make_a_move(board.get_turn(),log[i][0],log[i][1],0,elapsed_time = log[i][2])
                board.show_state()
            print("\n Continuing old game...")
            break
        except FileNotFoundError:
            print("\n File or 'logs' folder not found!")
else: raise Exception

# Here the real game play is happening:
try:
    while board.is_terminal() != True:
        try:
            start_time = time.time()
            src, dest = board.enter_manual_move()
            if src == None:
                print("Undoing last move...")
                if board.undo_last_move() == False:
                    print("Undoing failed!")
                    raise Exception
                board.show_state()
                raise ValueError
            if board.make_a_move(board.get_turn(),src, dest,start_time) == False:
                raise ValueError
            board.show_state()
        except ValueError:
            print("Try again")
    tools.save_game_log(board.get_history())
    print("Player {0} wins the game!".format(board.get_winner()))
except KeyboardInterrupt:
    tools.save_game_log(board.get_history())
    print("\n Game interrupted! Log is saved!")
except: #any unexpected error occurs during game play
    tools.save_game_log(board.get_history())
    print("\n An error occurred! Log is saved!")
