# Andri Fannar og Halldór

def info():
    n = '(N)orth'
    e = '(E)ast'
    s = '(S)outh'
    w = '(W)est'
    not_valid = 'Not a valid direction!'
    victory = 'Victory!'

    return n, e, s, w, not_valid, victory


def main_function(pos_x, pos_y, movement):
    info = info()

    flag = True
    while flag:
        if pos_x == 1 and pos_y == 1 or pos_x == 2 and pos_y == 1:
            print('You can travel: ' + info[0] + '.')
            if movement == 'n' or movement == 'N':
                pos_y += 1
            else:
                print(info[4])
        elif pos_x == 2 and pos_y == 2 or pos_x == 3 and pos_y == 3:
            print('You can travel: ' + info[0] + ' or ' + info[1] + ' or ' + info[2] + '.')
            if movement == 's' or movement == 'S':
                pos_y -= 1
            elif movement == 'e' or movement == 'E':
                pos_x -= 1
            else:
                print(info[4])
        elif pos_x == 1 and pos_y == 3:
            print('You can travel: ' + info[1] + ' or ' + info[2] + '.')
            if movement == 'e' or movement == 'E':
                pos_x += 1
            elif movement == 's' or movement == 'S':
                pos_y -= 1
            else:
                print(info[4])
        elif pos_x == 2 and pos_y == 3:
            print('You can travel: ' + info[1] + ' or ' + info[3] + '.')
            if movement == 'e' or movement == 'E':
                pos_x += 1
            elif movement == 'w' or movement == 'W':
                pos_x -= 1
            else:
                print(info[4])
        elif pos_x == 1 and pos_y == 2:
            print('You can travel: ' + info[0] + ' or ' + info[1] + ' or ' + info[2] + '.')
            if movement == 'n' or movement == 'N':
                pos_y += 1
            elif movement == 'e' or movement == 'E':
                pos_x += 1
            elif movement == 's' or movement == 'S':
                pos_y -= 1
            else:
                print(info[4])
        elif pos_x == 3 and pos_y == 2:
            print('You can travel: ' + info[0] + ' or ' + info[2] + '.')
            if movement == 'n' or movement == 'N':
                pos_y += 1
            elif movement == 's' or movement == 'S':
                pos_y += 1
            else:
                print(info[4])
        else:
            print(info[5])


def get_pos():
    pos_x = 1
    pos_y = 1
    movement = get_input()
    print_info(pos_x, pos_y, movement)

def get_input():
    movement = input('Direction: ')
    return movement

get_input()