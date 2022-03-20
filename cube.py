# SIDE INDEX
FRONT = 0
BACK = 4
RIGHT = 8
LEFT = 12
UP = 16
DOWN = 20 #START INDEX OF EACH SIDE

# COLOR CODE
RED = 1
ORANGE = 2
GREEN = 3
BLUE = 4
YELLOW = 5
WHITE = 6

class Cube:
    def __init__(self, state):
        #F1234B1234R1234L1234U1234D1234
        # WWWWYYYYOOOORRRRBBBBGGGG
        self.state = state # a string og 24 char
        self.h = 0
        self.g = 0
        self.f = 0

    # comparing 2 cube if they are the same (if needed)
    def __eq__(self, other):
        return self.state == other.state
    # comparing 2 cube if one is greater ( f value)
    def __gt__(self, other):
        if(self.f == other.f):
            return self.h > other.h
        return self.f > other.f

    def frontCW(self):
        # convert from string to a list, because a string is immutable
        state = list(self.state)
        # rotate (F23<-R13<-D01<-L02<-(past)F23)
        tFront2, tFront3 = state[FRONT+2], state[FRONT+3]
        # change f23 to r13
        state[FRONT+2], state[FRONT+3] = state[RIGHT+1], state[RIGHT+3]
        # change r13 to d01
        state[RIGHT+1], state[RIGHT+3] = state[DOWN], state[DOWN+1]
        # change d01 to l02
        state[DOWN], state[DOWN+1] = state[LEFT], state[LEFT+2]
        # change l02 to f23
        state[LEFT], state[LEFT+2] = tFront2, tFront3
        # convert it back to string
        self.state = str(state)


    def frontCCW(self):
        # convert from string to a list, because a string is immutable
        state = list(self.state)
        # rotate (F23<-L02<-D01<-R13<-(past)F23)
        tFront2, tFront3 = state[FRONT+2], state[FRONT+3]
        # change f23 to l02
        state[FRONT+2], state[FRONT+3] = state[LEFT], state[LEFT+2]
        # change l02 to d01
        state[LEFT], state[LEFT+2] = state[DOWN], state[DOWN+1]
        # chang d01 to r13
        state[DOWN], state[DOWN+1] = state[RIGHT+1], state[RIGHT+3]
        # change r13 to f23
        state[RIGHT+1], state[RIGHT+3] = tFront2, tFront3
        # convert it back to string
        self.state = str(state)
    
    def upCW(self):
        # convert from string to a list, because a string is immutable
        state = list(self.state)
        # rotate r01<-d01<-l01<-u01<-r01
        tright0, tright1= state[RIGHT], state[RIGHT+1]
        # change r01 to d01
        state[RIGHT], state[RIGHT+1] = state[DOWN], state[DOWN+1]
        # change d01 t0 l01
        state[DOWN], state[DOWN+1] = state[LEFT], state[LEFT+1]
        # change l01 to u01
        state[LEFT], state[LEFT+1] = state[UP], state[UP+1]
        # change u01 to r01
        state[UP], state[UP+1] = tright0, tright1
        # convert it back to string
        self.state = str(state)

    def upCCW(self):
        # convert from string to a list, because a string is immutable
        state = list(self.state)
        # rotate r01<-u01<-l01<-d01<-r01
        tright0, tright1= state[RIGHT], state[RIGHT+1]
        # change r01 to u01
        state[RIGHT], state[RIGHT+1] = state[UP], state[UP+1]
        # change u01 t0 l01
        state[UP], state[UP+1] = state[LEFT], state[LEFT+1]
        # change l01 to d01
        state[LEFT], state[LEFT+1] = state[DOWN], state[DOWN+1]
        # change d01 to r01
        state[UP], state[UP+1] = tright0, tright1
        # convert it back to string
        self.state = str(state)               

    def move(self, move):
        if(move == 'F'):
            self.frontCW()



# mycube = Cube()