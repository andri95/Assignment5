# Andri Fannar og Halldór

def info():
    n = '(N)orth'
    e = '(E)ast'
    s = '(S)outh'
    w = '(W)est'

    return n, e, s, w

def print_info(pos_x, pos_y, movement):
    directions = info()

    flag = True
    while flag:
        if pos_x == 1 and pos_y == 1 or pos_x == 2 and pos_y == 1:
            print('You can travel: ' + directions[0] + '.')
            if movement == 'n' or movement == 'N':
                pos_y += 1
            else:
                print('Not a valid direction!')
        elif pos_x == 2 and pos_y == 2 or pos_x == 3 and pos_y == 3:
            print('You can travel: ' + directions[0] + ' or ' + directions[1] + ' or ' + directions[2] + '.')
            




def get_pos():
    pos_x = 1
    pos_y = 1
    movement = get_input()
    print_info(pos_x, pos_y, movement)

def get_input():
    movement = input('Direction: ')
    return movement