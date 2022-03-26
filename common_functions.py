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

SIDE_DP = {
    "W": 0,
    "O": 1,
    "G": 2,
    "R": 3,
    "B": 4,
    "Y": 5,
}

def get_heuristic_val(cubic_state):
    total_wrong_side = 0
    for id, c in enumerate(cubic_state):
        #  extract side
        side = id//4
        total_wrong_side+=SIDE_DP[c] != side
        # col = id%2
        # row  = (id%4)//2
    #     tupple_pos = CB_DP[c]
    #     distance = 0
    #     for tside, trow, tcol in tupple_pos:
    #         temp_distance = 0
    #         temp_distance += abs(side - tside)
    #         if(temp_distance==0):
    #             # udah di side yang sama, berhenti
    #             distance = 0
    #             break
    #         # kalau gak 0, mungkin salah tempat
    #         distance += temp_distance
    #     # end of for loop
    #     distance /= 4 # karena ada 4 possible position
    #     total_distance+= distance
    total_wrong_side/=8 # because one turn, move 8 tiles
    return total_wrong_side

# print(get_heuristic_val("WWWWOOOOGGGGRRRRBBBBYYYY"))
# print(get_heuristic_val("GOOYWBWOYBWWRYOGGRRRGBBY"))