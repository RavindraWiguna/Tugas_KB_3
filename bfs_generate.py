#!/usr/bin/python3
from collections import Counter #to act like a std::map<str, int> on cpp
from collections import defaultdict #dictionary but with default value on missing key
from queue import Queue #to store node with automated queue based on f val
import time
from common_functions import *
from cube import Cube
import pickle

#GLOBAL POSSIBLE MOVE
POS_MOVE = ('F', 'R', 'U', 'B', 'L', 'D', 'FC', 'RC', 'UC', 'BC', 'LC', 'DC')

# color = 'W'
def bfs_gen():
    init_cube = Cube("....................YYYY")
                      

    heuristic_dict = {}
    heuristic_dict[init_cube.state] = 0

    openQue = Queue()

    openQue.put((init_cube.state, 0))
    try:
        while openQue.queue:
            cur_cube_state, depth = openQue.get()
            # update for next depth
            depth+=1
            for move in POS_MOVE:
                # print(move)
                #generate node based on move
                move_state = create_cube_state(cur_cube_state, move)

                if(move_state in heuristic_dict):
                    continue
                # never visited so uh we add to queue
                openQue.put((move_state, depth))
                heuristic_dict[move_state] = depth

            

    
    except KeyboardInterrupt:
        pass

    with open('BFS_Heuristic_Y.pickle', 'wb') as handle:
        pickle.dump(heuristic_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print("finished")
    print(f"got: {len(heuristic_dict)} states")


if __name__=="__main__":
    print("generating")
    bfs_gen()