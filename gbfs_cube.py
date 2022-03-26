from collections import Counter #to act like a std::map<str, int> on cpp
from queue import PriorityQueue #to store node with automated queue based on f val
import time
from common_functions import *
from cube import Cube
import os
#pseudocode reference: 
#modifitying A star with pseudocode from: https://en.wikipedia.org/wiki/Best-first_search

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

def create_cube_state(cube_state, move):
    cube = Cube(cube_state)
    if(move == 'F'):
        cube.frontCW()
    elif(move == 'R'):
        cube.rightCW()
    elif(move == 'U'):
        cube.upCW()
    elif(move == 'B'):
        cube.backCW()
    elif(move == 'L'):
        cube.leftCW()
    elif(move == 'D'):
        cube.downCW()
    elif(move == 'FC'):
        cube.frontCCW()
    elif(move == 'RC'):
        cube.rightCCW()
    elif(move == 'UC'):
        cube.upCCW()
    elif(move == 'BC'):
        cube.backCCW()
    elif(move == 'LC'):
        cube.leftCCW()
    elif(move == 'DC'):
        cube.downCCW()
    else:
        raise ValueError
    return cube.state


#GLOBAL POSSIBLE MOVE
POS_MOVE = ('F', 'R', 'U', 'B', 'L', 'D', 'FC', 'RC', 'UC', 'BC', 'LC', 'DC')
def greedy_best_first_search(start_cube, goal_cube):
    total_opened_node = 0
    
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
        # print(f'this cube came from: {cameFrom[min_cube.state][1]}')
        # os.system("pause")
        if(min_cube == goal_cube):
            print("HEY, Found the goal!")
            path = reconstruct_path(min_cube.state, cameFrom)
            isFound = True
            break
        
        
        min_cube_state = min_cube.state
        #get all possible move
        for move in POS_MOVE:
            
            #generate node based on move
            new_state = create_cube_state(min_cube_state, move)
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
    return path, total_opened_node

def main():
    # create start and goal cube
    start_cube = Cube("BBYRRGGYOYBGBOWGWWRWOROY")
    goal_cube = Cube() # awal is: WWWWOOOOGGGGRRRRBBBBYYYY
    print("START CUBE")
    start_cube.printState()
    print("GOAL CUBE")
    goal_cube.printState()

    #search!
    print("Searching Solution using Greedy Best First Search Algorithm...")
    start_time = time.perf_counter()
    path, total_opened_node = greedy_best_first_search(start_cube, goal_cube)
    end_time = time.perf_counter()
    print(f'Greedy Best First Search elapsed time: {end_time - start_time}| [Elapsed time may not be stable, try run it a couple of times to get the elapsed time on average]')
    print(f'Total node opened: {total_opened_node}')
    print(f'Total move: {len(path)-1} (Without root)')
    print(f'Path:\n{path}')


if __name__ == "__main__":
    # import cProfile
    # cProfile.run('main()')
    main()