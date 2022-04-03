#!/usr/bin/python3
from collections import Counter #to act like a std::map<str, int> on cpp
from collections import defaultdict #dictionary but with default value on missing key
from queue import Queue, PriorityQueue #to store node with automated queue based on f val
import time
from common_functions import *
from cube import Cube
import pickle

#GLOBAL POSSIBLE MOVE
POS_MOVE = ('F', 'R', 'U', 'B', 'L', 'D', 'FC', 'RC', 'UC', 'BC', 'LC', 'DC')

# WWWWOOOOGGGGRRRRBBBBYYYY
def bfs_gen():
    init_cube = Cube("WWWWOOOO................")
                      

    heuristic_dict = {}
    heuristic_dict[init_cube.state] = 0

    openQue = PriorityQueue()

    openQue.put((0, init_cube.state))
    try:
        while openQue.queue:
            depth, cur_cube_state = openQue.get()
            # update for next depth
            depth+=1
            for move in POS_MOVE:
                # generate node based on move
                move_state = create_cube_state(cur_cube_state, move)
                
                # check if this state is in heuristic dict
                if(move_state in heuristic_dict):
                    # if we found way to get to this state but faster
                    if(heuristic_dict[move_state] > depth):
                        # update the depth
                        heuristic_dict[move_state] = depth
                        # put it again in openque
                        openQue.put((depth, move_state))
                    continue
                # never visited so uh we add to queue
                # check if each side is equal
                isComplete = check_side_equalness(move_state)
                if(isComplete):
                    heuristic_dict[move_state] = 0
                    openQue.put((0, move_state))
                else:
                    heuristic_dict[move_state] = depth
                    openQue.put((depth, move_state))

                

            

    
    except KeyboardInterrupt:
        pass

    with open('BFS_Heuristic_WO.pickle', 'wb') as handle:
        pickle.dump(heuristic_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print("finished")
    print(f"got: {len(heuristic_dict)} states")
    print(Counter(heuristic_dict.values()))


if __name__=="__main__":
    print("generating")
    start_time = time.perf_counter()
    bfs_gen()
    end_time = time.perf_counter()
    print(f'Elapsed time: {end_time - start_time}')