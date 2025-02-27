from transition import Board
from engine import Agent
import tools
from os import system, name
import time

# Initialization
    # for windows
if name == 'nt':
    system('cls')
    # for mac and linux
else:
    system('clear')
board = Board(tools.initial_state())
silver_agents = {1: Agent('manual','silver'),
                2: Agent('manual','silver'),
                3: Agent('engine','silver'),
                4: Agent('engine','silver')}
gold_agents = {1: Agent('manual','gold'),
                2: Agent('engine','gold'),
                3: Agent('manual','gold'),
                4: Agent('engine','gold')}


# Game SetUp
N = 0
print("Welcome to Breakthru! \n Remember: You can use <-1 0 0 0> to undo last move \
\n Press 1 for new game and 2 to continue old game:")
choice = int(input())
if choice == 1:
    print("Choose type of game:")
    agents = { 1: 'manual - manual',
        2: 'engine - manual',
        3: 'manual - engine',
        4: 'engine - engine'
        }
    print("    gold - silver \n   --------------")
    for i in range(1,5):
        print("{0} : {1}".format(i, agents[i]))
    type = int(input())
    GOLD = gold_agents[type]
    SILVER = silver_agents[type]
    board.save_type(type)
    if type == 1 or type == 3:
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
            type,log = tools.read_game_log(file)
            GOLD = gold_agents[type]
            SILVER = silver_agents[type]
            board.save_type(type)
            if log[0][0][0] == 99:
                print("\n Gold skipped first move")
                board.switch_player_at_turn()
                board.gold_skips()
                del log[0]
            board.show_state()
            for i in range(0,len(log)):
                turn = board.get_turn()
                print("Player {} moves".format(turn.upper()))
                print("from {0}{1} to {2}{3}".format(chr(log[i][0][1]+97).upper(),11-log[i][0][0],\
                chr(log[i][1][1]+97).upper(),11-log[i][1][0]))
                board.make_a_move(board.get_turn(),log[i][0],log[i][1],0,elapsed_time = 0.1)
                board.show_state()
            N = len(log)
            print("\n Continuing old game...")
            break
        except FileNotFoundError:
            print("\n File or 'logs' folder not found!")
else: raise Exception

# Here the real game play is happening:
# Engine interacts with manual player
# Board enforces the rules
try:
    while board.is_terminal() != True:
        try:
            # if board.get_moves_left() != 2: # enable for testing purposes
            #     print("error in moves_left")
            #     raise Exception
            start_time = time.time()
            if board.get_turn() == 'gold':
                print("Player Gold moves")
                src_1,dest_1,src_2,dest_2,type_1,type_2 = GOLD.get_move(board,N = N)
            elif board.get_turn() == 'silver':
                print("Player Silver moves")
                src_1,dest_1,src_2, dest_2,type_1,type_2 = SILVER.get_move(board,N = N)
            if src_1 == None: # Code to undo move
                print("Undoing moves...")
                # Undo most recent move of other player
                if board.undo_last_move(type) == False:
                    print("Undoing failed!")
                    raise Exception
                # Undo 2nd recent move, if present
                if board.get_moves_left() == 1:
                    if board.undo_last_move(type) == False:
                        print("Undoing failed!")
                        raise Exception
                N -= 1
                # If not playing manual-manual, undo own last moves
                if type != 1 and N > 1:
                    if board.undo_last_move(type) == False:
                        print("Undoing failed!")
                        raise Exception
                    if board.get_moves_left() == 1:
                        if board.undo_last_move(type) == False:
                            print("Undoing failed!")
                            raise Exception
                    N -= 1
                raise ValueError
            if board.make_a_move(board.get_turn(),src_1, dest_1,start_time,type=type_1) == False:
                raise ValueError
            if src_2 != None:
                if board.make_a_move(board.get_turn(),src_2, dest_2,start_time,type=type_2) == False:
                    raise ValueError
            board.show_state()
            N += 1
        except ValueError:
            print("Try again")
            board.show_state()
    tools.save_game_log(board.get_history())
    print("Player {0} wins the game!".format(board.get_winner()))
    print("\nPress any key to continue...")
    input()
except KeyboardInterrupt:
    tools.save_game_log(board.get_history())
    print("\n Game interrupted! Log is saved.")
except: #any unexpected error occurs during game play # disable for testing purposes
    tools.save_game_log(board.get_history())
    print("\n An error occurred! Log is saved!")
