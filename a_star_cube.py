#!/usr/bin/python3
from collections import Counter #to act like a std::map<str, int> on cpp
from collections import defaultdict #dictionary but with default value on missing key
from queue import PriorityQueue #to store node with automated queue based on f val
import time
from common_functions import *
from cube import Cube

#pseudocode reference: 
#https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
#https://en.wikipedia.org/wiki/A*_search_algorithm

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

def a_star(start_cube, goal_cube):
    total_opened_node = 0
    
    open_nodes = PriorityQueue()#store node that haven't explored with pqueue
    closed_state = Counter() #counter for state that has been explored
    everInOpen = Counter()
    cameFrom = {} #dict to map where a node came from
    
    #node scores
    gScore = defaultdict(lambda:float('inf'))
    gScore[start_cube.state] = 0 #save start node state gscore to 0
    start_cube.h = get_heuristic_val(start_cube.state) 
    start_cube.f = start_cube.h
    
    open_nodes.put(start_cube)
    everInOpen[start_cube.state]+=1
    cameFrom[start_cube.state] = (None, ".")
    total_opened_node+=1
    path = None #saved path for return value
    tentative_gScore = None #variable to hold min node gScore
    #loop while open list is not empty in pythonic way
    while open_nodes:
        #get node with min f value
        min_cube = open_nodes.get()
        #add min node counter in 
        closed_state[min_cube.state]+=1
        
        #check if it is the goal node
        min_cube_state = min_cube.state
        if (min_cube == goal_cube):
            print("HEY, Found the goal!")
            path = reconstruct_path(min_cube.state, cameFrom)
            break
        
        # loop for every possible move
        for move in POS_MOVE:
            #generate node based on move
            new_state = create_cube_state(min_cube_state, move)
            move_node = Cube(new_state)
            # os.system("pause")
            #check if this node's state has been reached/visited/closed
            if(closed_state[move_node.state] > 0):
                continue
           
            #this node havent yet visited
            tentative_gScore = gScore[min_cube.state] + 1 #distance of node is same, so always +1
            if(tentative_gScore < gScore[move_node.state]):
                #Found a smaller g score of this state, so update the g score and cameFrom
                cameFrom[move_node.state] = (min_cube.state, move)
                gScore[move_node.state] = tentative_gScore
                #calculate other value of this node
                move_node.h = get_heuristic_val(move_node.state)
                move_node.f = tentative_gScore + move_node.h
                
                #check if it is not in the open set
                if(everInOpen[move_node.state]==0):
                    #never in open
                    total_opened_node+=1
                    open_nodes.put(move_node)
                    everInOpen[move_node.state]+=1
                # if(move_node not in open_nodes.queue):
                    # total_opened_node+=1
                    # open_nodes.put(move_node)

        #End of For Loop
    #End of While Loop
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
    print("Searching Solution using A* Algorithm...")
    start_time = time.perf_counter()
    path, total_opened_node = a_star(start_cube, goal_cube)
    end_time = time.perf_counter()
    print(f'A star elapsed time: {end_time - start_time}| [Elapsed time may not be stable, try run it a couple of times to get the elapsed time on average]')
    print(f'Total node opened: {total_opened_node}')
    print(f'Total move: {len(path)-1} (Without root)')
    print(f'Path:\n{path}')



if __name__ == "__main__":
    # import cProfile
    # cProfile.run('main()')
    main()