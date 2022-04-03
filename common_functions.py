#!/usr/bin/python3.10
from collections import defaultdict
from cube import Cube
from pickle import load as pkload
from time import perf_counter
from snipped_termcolor import draw

def readfile(filename):
    f = open(filename)
    data = f.read()
    arr = ["W", "O", "G", "R", "B", "Y"]
    count = [0, 0, 0, 0, 0, 0]
    for c in data:
        for i, color in enumerate(arr):
            count[i] += c==color

    for i in count:
        if(i != 4):
            print(count)
            raise ValueError
    return data

# load heuristic
def load_heuristic(fileName):
    handle0 = open(f"{fileName}_{0}.pickle", "rb")
    handle1 = open(f"{fileName}_{1}.pickle", "rb")
    heuristic_part1 = pkload(handle0)
    heuristic_part2 = pkload(handle1)
    output = heuristic_part1 | heuristic_part2 # merge 2 parts
    
    return output


# hWY = pickle.load(open("BFS_Heuristic_WY.pickle", "rb"))
# hOR = pickle.load(open("BFS_Heuristic_OR.pickle", "rb"))
# hGB = pickle.load(open("BFS_Heuristic_GB.pickle", "rb"))
print("Loading Heuristic...")
start_time = perf_counter()
hWO = load_heuristic("BFS_Heuristic_WO")
hGR = load_heuristic("BFS_Heuristic_GR")
hBY = load_heuristic("BFS_Heuristic_BY")
end_time = perf_counter()
print(f'Loading time: {end_time - start_time}')
print("Finish Loading")
    


def check_side_equalness(cubic_state):
    side = (0, 4, 8, 12, 16) # only need check 5 side, if all 5 right, sisanya must be right
    isComplete = True
    for i in side:
        for j in range(3):
            if(cubic_state[i+j] != cubic_state[i+j+1]):
                isComplete = False
                break
        if(not isComplete):
            break
    
    return isComplete

# endoding dictionary
# eWY = defaultdict(lambda:'.')
# eWY['W'] = 'W'
# eWY['Y'] = 'Y'
# eOR = defaultdict(lambda:'.')
# eOR['O'] = 'O'
# eOR['R'] = 'R'
# eGB = defaultdict(lambda:'.')
# eGB['G'] = 'G'
# eGB['B'] = 'B'
eWO = defaultdict(lambda:'.')
eWO['W'] = 'W'
eWO['O'] = 'O'
eGR = defaultdict(lambda:'.')
eGR['G'] = 'G'
eGR['R'] = 'R'
eBY = defaultdict(lambda:'.')
eBY['Y'] = 'Y'
eBY['B'] = 'B'

def get_heuristic_val(cubic_state):
    # sWY, sGB, sOR = "", "", ""
    sWO, sGR, sBY = "", "", ""
    # get state for each color
    for c in cubic_state:
        # sWY += eWY[c]
        # sOR += eOR[c]
        # sGB += eGB[c]
        sWO += eWO[c]
        sGR += eGR[c]
        sBY += eBY[c]

    # hhWY = hWY[sWY]
    # hhOR = hOR[sOR]
    # hhGB = hGB[sGB]
    hhWO = hWO[sWO]
    hhGR = hGR[sGR]
    hhBY = hBY[sBY]
    return max(hhBY, hhGR, hhWO)

def frontCW(cube_state):
    cube = Cube(cube_state)
    cube.frontCW()
    return cube.state

def frontCCW(cube_state):
    cube = Cube(cube_state)
    cube.frontCCW()
    return cube.state

def rightCW(cube_state):
    cube = Cube(cube_state)
    cube.rightCW()
    return cube.state

def rightCCW(cube_state):
    cube = Cube(cube_state)
    cube.rightCCW()
    return cube.state

def leftCW(cube_state):
    cube = Cube(cube_state)
    cube.leftCW()
    return cube.state

def leftCCW(cube_state):
    cube = Cube(cube_state)
    cube.leftCCW()
    return cube.state

def backCW(cube_state):
    cube = Cube(cube_state)
    cube.backCW()
    return cube.state

def backCCW(cube_state):
    cube = Cube(cube_state)
    cube.backCCW()
    return cube.state

def upCW(cube_state):
    cube = Cube(cube_state)
    cube.upCW()
    return cube.state

def upCCW(cube_state):
    cube = Cube(cube_state)
    cube.upCCW()
    return cube.state

def downCW(cube_state):
    cube = Cube(cube_state)
    cube.downCW()
    return cube.state

def downCCW(cube_state):
    cube = Cube(cube_state)
    cube.downCCW()
    return cube.state

move_func_dict ={'F':frontCW, 
                 'R':rightCW, 
                 'U':upCW, 
                 'B':backCW, 
                 'L':leftCW, 
                 'D':downCW, 
                 'FC':frontCCW, 
                 'RC':rightCCW, 
                 'UC':upCCW, 
                 'BC':backCCW, 
                 'LC':leftCCW, 
                 'DC':downCCW}


def create_cube_state(cube_state, move):
    return move_func_dict[move](cube_state)

def reconstruct_path(finish_state, cameFrom: dict):
    path = []
    cur_state = finish_state
    while (cur_state):
        # print(cur_state)
        cur_state, move = cameFrom[cur_state]
        # create_cube_state(Cube(cur_state), )
        path.append(move)
        # print(f'{move}, ', end="")
    return path[::-1] #reverse the path, and return it

def get_cube_input():
    print(f"ENCODED COLOR:\nWhite = {draw('W')}\nOrange = {draw('O')}\nGreen = {draw('G')}\nRed = {draw('R')}\nBlue = {draw('B')}\nYellow = {draw('Y')}")
    msg = ("UP", "LEFT", "FRONT", "RIGHT", "BACK", "DOWN")
    state = ""
    for m in msg:
        tstate = input(f"Type in the {m} side: ")
        state += tstate
    
    return state


def print_history(init_state, path):
    cube = Cube(init_state)
    #cut from id 1-end
    for i, move in enumerate(path[1:]):
        cube = Cube(move_func_dict[move](cube.state))
        print(f'MOVE #{i+1}: {move}')
        cube.printState()
        input("continue")
