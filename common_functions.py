from collections import Counter
from cube import Cube
import pickle
def readfile(filename):
    f = open(filename)
    data = f.read()
    arr = ["W", "O", "G", "R", "B", "Y"]
    count = [0, 0, 0, 0, 0, 0]
    for c in data:
        for i, color in enumerate(arr):
            count[i] += c==color
    # print(count)
    for i in count:
        if(i != 4):
            print(count)
            raise ValueError
    return data


SIDE_DP = {
    "W": 0,
    "O": 1,
    "G": 2,
    "R": 3,
    "B": 4,
    "Y": 5,
}

# hW = pickle.load(open("BFS_Heuristic_W.pickle", "rb"))
# hO = pickle.load(open("BFS_Heuristic_O.pickle", "rb"))
# hG = pickle.load(open("BFS_Heuristic_G.pickle", "rb"))
# hR = pickle.load(open("BFS_Heuristic_R.pickle", "rb"))
# hB = pickle.load(open("BFS_Heuristic_B.pickle", "rb"))
# hY = pickle.load(open("BFS_Heuristic_Y.pickle", "rb"))
try:
    hWY = pickle.load(open("BFS_Heuristic_WY.pickle", "rb"))
    hOR = pickle.load(open("BFS_Heuristic_OR.pickle", "rb"))
    hGB = pickle.load(open("BFS_Heuristic_GB.pickle", "rb"))
except FileNotFoundError:
    print("HEURISTIC DICT NOT FOUND")


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

def get_heuristic_val(cubic_state):
    # if(check_side_equalness(cubic_state)):
    #     return 0
    # total_wrong_side = 0
    # sW = ""
    # sO = ""
    # sG = ""
    # sR = ""
    # sB = ""
    # sY = ""
    sWY, sGB, sOR = "", "", ""
    # get state for each color
    for c in cubic_state:
        # sW += chr(ord('.')*(c!='W') + ord('W')*(c=='W'))
        # sO += chr(ord('.')*(c!='O') + ord('O')*(c=='O'))
        # sG += chr(ord('.')*(c!='G') + ord('G')*(c=='G'))
        # sR += chr(ord('.')*(c!='R') + ord('R')*(c=='R'))
        # sB += chr(ord('.')*(c!='B') + ord('B')*(c=='B'))
        # sY += chr(ord('.')*(c!='Y') + ord('Y')*(c=='Y'))
        sWY += chr(ord('.')*(c!='W' and c!= 'Y') + ord('W')*(c=='W') + ord('Y')*(c=='Y'))
        sOR += chr(ord('.')*(c!='O' and c!= 'R') + ord('O')*(c=='O') + ord('R')*(c=='R'))
        sGB += chr(ord('.')*(c!='G' and c!= 'B') + ord('G')*(c=='G') + ord('B')*(c=='B'))

    # hhW = hW[sW]
    # hhO = hO[sO]
    # hhG = hG[sG]
    # hhR = hR[sR]
    # hhB = hB[sB]
    # hhY = hY[sY]
    hhWY = hWY[sWY]
    hhOR = hOR[sOR]
    hhGB = hGB[sGB]
    # print([hhWY, hhOR, hhGB])
    return max(hhWY, hhOR, hhGB)

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


def print_history(init_state, path):
    cube = Cube(init_state)
    #cut from id 1-end
    for i, move in enumerate(path[1:]):
        cube = Cube(move_func_dict[move](cube.state))
        print(f'MOVE #{i+1}: {move}')
        cube.printState()
        input("continue")
