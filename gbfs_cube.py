from collections import Counter #to act like a std::map<str, int> on cpp
from queue import PriorityQueue #to store node with automated queue based on f val
import time
from common_functions import *
from cube import Cube
import os
#pseudocode reference: 
#modifitying A star with pseudocode from: https://en.wikipedia.org/wiki/Best-first_search

#GLOBAL POSSIBLE MOVE
POS_MOVE = ('F', 'R', 'U', 'B', 'L', 'D', 'FC', 'RC', 'UC', 'BC', 'LC', 'DC')
def greedy_best_first_search(start_cube):
    total_opened_node = 0
    total_removed_node = 0

    queue = PriorityQueue()#store node that haven't explored with pqueue
    cameFrom = {} # store where the node came from (also as visited)
    
    #node scores
    start_cube.h = get_heuristic_val(start_cube.state) 
    
    queue.put(start_cube) #add to queue
    cameFrom[start_cube.state] = (None, ".") #record it origin as None and "." -> root
    total_opened_node+=1
    path = None #saved path for return value
    isFound = False
    #loop while open list is not empty in pythonic way
    while queue and not isFound:
        #get node with min f value
        min_cube = queue.get()
        total_removed_node+=1

        #get all possible move
        for move in POS_MOVE:
            
            #generate node based on move
            new_state = create_cube_state(min_cube.state, move)
            move_cube = Cube(new_state)
            #check if this node's state has been reached/visited/closed
            if(move_cube.state in cameFrom):
                continue
            # check if it is goal
            move_cube.h = get_heuristic_val(move_cube.state)
            if(move_cube.h == 0):
                print("HEY, Found the goal!")
                # add it to cameFrom first
                cameFrom[move_cube.state] = (min_cube.state, move)
                path = reconstruct_path(move_cube.state, cameFrom)
                isFound = True
                break

            #this node has not visited so, add to queue
            #do just like the start node
            queue.put(move_cube)
            cameFrom[move_cube.state] = (min_cube.state, move)
            total_opened_node+=1     

        #End of For Loop
    #End of While Loop
    # return path, total_opened_node
    return path, total_opened_node, total_removed_node

def main():
    start_state = readfile("cube.txt")
    start_cube = Cube(start_state)
    print("START CUBE")
    start_cube.printState()
    print(f"Estimated cost from start [h(n)]: {get_heuristic_val(start_state)}\n")  
    print("GOAL CUBE: each side has same color\n")  

    #search!
    print("Searching Solution using Greedy Best First Search Algorithm...")
    start_time = time.perf_counter()
    path, total_opened_node, total_removed_node = greedy_best_first_search(start_cube)
    end_time = time.perf_counter()
    print(f'- A star elapsed time: {end_time - start_time}')
    print(f'- Total node opened: {total_opened_node}')
    print(f'- Total node removed from queue: {total_removed_node}')
    print(f'- Total move: {len(path)-1} (Without root)')
    print(f'- Path:\n{path}')
    ans = input("Do you want to see the solutions in play? [y/n] Default:y\n>>>")
    if(ans == 'n' or ans == 'N'):
        print("Alright then, closing program...")
        return 0
    print_history(start_state, path)


if __name__ == "__main__":
    # import cProfile
    # cProfile.run('main()')
    main()