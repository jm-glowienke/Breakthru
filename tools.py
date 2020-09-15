import json
import time

def initial_state():
    # define initial start board: silver = 1, gold = 2, flagship = 3
        board_initial = [
        [".",".",".",".",".",".",".",".",".",".","."],
        [".",".",".",1,1,1,1,1,".",".","."],
        [".",".",".",".",".",".",".",".",".",".","."],
        [".",1,".",".",2,2,2,".",".",1,"."],
        [".",1,".",2,".",".",".",2,".",1,"."],
        [".",1,".",2,".",3,".",2,".",1,"."],
        [".",1,".",2,".",".",".",2,".",1,"."],
        [".",1,".",".",2,2,2,".",".",1,"."],
        [".",".",".",".",".",".",".",".",".",".","."],
        [".",".",".",1,1,1,1,1,".",".","."],
        [".",".",".",".",".",".",".",".",".",".","."]]
        return board_initial

# create subdirectory
def save_game_log(history):
    with open('./logs/log_'+time.strftime("%Y%m%d-%H%M%S"), 'w') as f:
        for item in history:
            f.write('%s\n' % item)
    return

def read_game_log(filename):
    history = []

    # open file and read the content in a list
    with open('./logs/'+filename, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            current = line[1:-3]
            for item in current:
                print(item, end = '')
            print()
            #print(type(current))
            # add item to the list
            history.append(current)
    return history

a = [[1,2,3],[4,5,6]]
# save_game_log(a)

read_game_log('log_20200915-181301')
