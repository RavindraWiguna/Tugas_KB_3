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
def greedy_best_first_search(start_cube, goal_cube):
    total_opened_node = 0
    total_removed_node = 0

    queue = PriorityQueue()#store node that haven't explored with pqueue
    visited = Counter() #counter for state that has been explored
    cameFrom = {}
    
    #node scores
    start_cube.h = get_heuristic_val(start_cube.state) 
    
    queue.put(start_cube) #add to queue
    cameFrom[start_cube.state] = (None, ".") #record it origin as None and "." -> root
    visited[start_cube.state]+=1 #mark it as visited
    total_opened_node+=1
    path = None #saved path for return value
    isFound = False
    #loop while open list is not empty in pythonic way
    while queue and not isFound:
        #get node with min f value
        min_cube = queue.get()
        total_removed_node+=1
        # print(f'this cube came from: {cameFrom[min_cube.state][1]}')
        # os.system("pause")
        if(min_cube.state == goal_cube.state):
            print("HEY, Found the goal!")
            path = reconstruct_path(min_cube.state, cameFrom)
            isFound = True
            break
        
        
        # min_cube_state = min_cube.state
        #get all possible move
        for move in POS_MOVE:
            
            #generate node based on move
            new_state = create_cube_state(min_cube.state, move)
            move_cube = Cube(new_state)
            #check if this node's state has been reached/visited/closed
            if(visited[move_cube.state] > 0):
                continue
            
            #this node has not visited so, add to queue, but first calc the h val
            move_cube.h = get_heuristic_val(move_cube.state)
            #do just like the start node
            queue.put(move_cube)
            cameFrom[move_cube.state] = (min_cube.state, move)
            visited[move_cube.state]+=1
            total_opened_node+=1     

        #End of For Loop
    #End of While Loop
    # return path, total_opened_node
    return path, total_opened_node, total_removed_node

def main():
    # create start and goal cube
    start_state = readfile("cube.txt")
    start_cube = Cube(start_state)
    goal_cube = Cube() # awal is: WWWWOOOOGGGGRRRRBBBBYYYY
    print("START CUBE")
    start_cube.printState()
    print("GOAL CUBE")
    goal_cube.printState()

    #search!
    print("Searching Solution using Greedy Best First Search Algorithm...")
    start_time = time.perf_counter()
    path, total_opened_node, total_removed_node = greedy_best_first_search(start_cube, goal_cube)
    end_time = time.perf_counter()
    print(f'Greedy Best First Search elapsed time: {end_time - start_time}| [Elapsed time may not be stable, try run it a couple of times to get the elapsed time on average]')
    print(f'Total node opened: {total_opened_node}')
    print(f'Total node removed from queue: {total_removed_node}')
    print(f'Total move: {len(path)-1} (Without root)')
    print(f'Path:\n{path}')


if __name__ == "__main__":
    # import cProfile
    # cProfile.run('main()')
    main()