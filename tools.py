import time
import os
import copy

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
    if not os.path.isdir("./logs/"): # if not present create folder to store logs
        os.makedirs("./logs/")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    with open('./logs/log_'+timestamp, 'w') as f:
        f.write('log_'+timestamp + '\n')
        f.write('%s \n ' % history[0])
        del(history[0])
        f.write('src_row src_col dest_row dest_col\n')
        for row in history:
            for item in row:
                f.write('%s        ' % item[0])
                f.write('%s        ' % item[1])
            f.write('\n')
            # f.write('%s\n' % row)
    return

def read_game_log(filename):
    history = []
    # open file and read the content in a list
    with open('./logs/'+filename, 'r') as filehandle:
        next(filehandle)
        k = -1
        for line in filehandle: #skip first two lines
            k += 1
            if k == 0:
                type = int(line[1].split()[0])
                continue
            if k == 1:
                continue
            # remove linebreak which is the last character of the string
            current = line[:-1].split()
            #print(current)
            save = []
            for item in current:
                save.append(int(item))
            history.append([[save[0],save[1]],[save[2],save[3]]])
    return type,history

def remove_double_moves(moves):
    cache = []
    moves_adapted = copy.deepcopy(moves)
    if moves_adapted != moves:
        print("deep copy wrong")
        return False
    n = 0
    for move in moves:
        if move[3] == []:
            # no second move, not possible to have double
            n+= 1
            continue
        else:
            k = 0
            for move2 in move[3]:
                if [move2,[move[0],move[1]]] in cache:
                    del moves_adapted[n][3][k]
                    continue
                else:
                    cache.append([[move[0],move[1]],move2])
                k += 1
        n+= 1
    return moves_adapted

def get_number_moves(moves):
    n = 0
    for move in moves:
        n += len(move[3])
        if len(move[3]) == 0:
            n += 1
    return n
