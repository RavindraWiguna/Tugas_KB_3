def readfile(filename):
    f = open(filename)
    data = f.read()
    return data

CB_DP = {
    "W": ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1)),
    "O": ((1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)),
    "G": ((2, 0, 0), (2, 0, 1), (2, 1, 0), (2, 1, 1)),
    "R": ((3, 0, 0), (3, 0, 1), (3, 1, 0), (3, 1, 1)),
    "B": ((4, 0, 0), (4, 0, 1), (4, 1, 0), (4, 1, 1)),
    "Y": ((5, 0, 0), (5, 0, 1), (5, 1, 0), (5, 1, 1)),
}

def get_heuristic_val(cubic_state, GOAL_POS="WWWWOOOOGGGGRRRRBBBBYYYY"):
    total_distance = 0
    for id, c in enumerate(cubic_state):
        #  extract side
        side = id//4
        col = id%2
        row  = (id%4)//2
        tupple_pos = CB_DP[c]
        distance = abs()
    return total_distance
