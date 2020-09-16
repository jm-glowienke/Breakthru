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
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    with open('./logs/log_'+timestamp, 'w') as f:
        f.write('log_'+timestamp + '\n')
        f.write('src_row src_col dest_row dest_col\n')
        for row in history:
            for item in row:
                f.write('%s       ' % item[0])
                f.write('%s       ' % item[1])
            f.write('\n')
            # f.write('%s\n' % row)
    return

def read_game_log(filename):
    try:
        history = []
        # open file and read the content in a list
        with open('./logs/'+filename, 'r') as filehandle:
            next(filehandle)
            next(filehandle)
            for line in filehandle: #skip first two lines
                # remove linebreak which is the last character of the string
                current = line[:-1].replace(' ','')
                #print(current)
                save = []
                for item in current:
                    save.append(int(item))
                print(save)
                history.append([[save[0],save[1]],[save[2],save[3]]])
        return history
    except FileNotFoundError:
        print("File or 'logs' folder not found!")
