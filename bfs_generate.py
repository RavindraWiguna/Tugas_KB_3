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

# WWWWOOOOGGGGRRRRBBBBYYYY
def bfs_gen():
    init_cube = Cube("........GGGGRRRR........")
                      

    arr_hdict = [{}, {}]
    id_h = 0
    arr_hdict[id_h][init_cube.state] = 0
    openQue = Queue()
    total_in_dict = 0
    openQue.put((init_cube.state, 0))
    try:
        while openQue.queue:
            cur_cube_state, depth = openQue.get()
            # update for next depth
            depth+=1
            for move in POS_MOVE:
                # generate node based on move
                move_state = create_cube_state(cur_cube_state, move)
                
                # boolean indicating if a node has been visited                
                isEverVisited = False
                for i in range(2):
                    if(isEverVisited):
                        # if this nove ever visited (exist in dict[0])
                        break
                    
                    # check if this state is in [i-th] heuristic dict 
                    if(move_state in arr_hdict[i]):
                        # exist in dict, so must have been visited
                        isEverVisited = True
                        # if we found way to get to this state but faster
                        if(arr_hdict[i][move_state] > depth):
                            # update the depth
                            arr_hdict[i][move_state] = depth
                            # put it again in openque
                            openQue.put((move_state, depth))
                # continue to next move if we already visit this
                if(isEverVisited):
                    continue

                # never visited so uh we add to queue
                # check if each side is equal
                isComplete = check_side_equalness(move_state)
                if(isComplete):
                    arr_hdict[id_h][move_state] = 0
                    openQue.put((move_state, 0))
                else:
                    arr_hdict[id_h][move_state] = depth
                    openQue.put((move_state, depth))
                # update total in dict
                total_in_dict+=1
                # switch to next dict if more than 1800000
                id_h = total_in_dict > 1800000
                

            

    
    except KeyboardInterrupt:
        pass
    
    for i in range(2):
        with open(f'BFS_Heuristic_GR_{i}.pickle', 'wb') as handle:
            pickle.dump(arr_hdict[i], handle, protocol=pickle.HIGHEST_PROTOCOL)

    print("finished")
    print(f"got: {len(arr_hdict[0]) + len(arr_hdict[1])} states")
    # print(Counter(heuristic_dict.values()))


if __name__=="__main__":
    print("generating")
    start_time = time.perf_counter()
    bfs_gen()
    end_time = time.perf_counter()
    print(f'Elapsed time: {end_time - start_time}')