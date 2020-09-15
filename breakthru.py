## # TODO:
## Store moves
## Time stamps
## loading of old game
## choice possibility which player engine has to play

from transition import Board
from tools import initial_state
import os

# Initialization
os.system('clear')
board = Board(initial_state())


# Game starts
print("Welcome to Breakthru! \n Press 1 for new game and 2 to continue old game:")
choice = int(input())
if choice == 1:
    print("Player GOLD: Do you want to skip your first move? [y/n]")
    skip = input()
    if skip.lower() == 'y':
        board.switch_player_at_turn()
elif choice == 2:
    # load game and play to correct screen
    print("Loading")
else: raise Exception

board.show_state()

while board.is_terminal() != True:
    try:
        src, dest = board.enter_manual_move()
        if board.make_a_move(board.get_turn(),src, dest) == False:
            raise ValueError
        board.show_state()
    except ValueError:
        print("Try again:")

print("Player {0} wins the game!".format(board.get_winner())
