from cube import Cube
from common_functions import *
from random import randint

#GLOBAL POSSIBLE MOVE
POS_MOVE = ('F', 'R', 'U', 'B', 'L', 'D', 'FC', 'RC', 'UC', 'BC', 'LC', 'DC')

def scramble(n):
    init_cube = Cube()
    for i in range(n):
        init_cube.state = move_func_dict[POS_MOVE[randint(0, 11)]](init_cube.state)

    
    print(init_cube.state)

scramble(15)