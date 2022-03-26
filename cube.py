# START INDEX OF EACH SIDE
UP = 0
LEFT = 4
FRONT = 8
RIGHT = 12
BACK = 16
DOWN = 20


# COLOR CODE
WHITE = 0
YELLOW = 1
ORANGE  = 2
RED = 3
BLUE = 4
GREEN = 5

class Cube:
    def __init__(self, state="WWWWOOOOGGGGRRRRBBBBYYYY"):
        #saved as ulfrbd
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

    def rotateSideCW(self, sideCode):
        state = list(self.state)
        s0 = state[sideCode]
        state[sideCode] = state[sideCode+2]
        state[sideCode+2] = state[sideCode+3]
        state[sideCode+3] = state[sideCode+1]
        state[sideCode+1] = s0
        self.state = "".join(state)
    
    def rotateSideCCW(self, sideCode):
        state = list(self.state)
        s0 = state[sideCode]
        state[sideCode] = state[sideCode+1]
        state[sideCode+1] = state[sideCode+3]
        state[sideCode+3] = state[sideCode+2]
        state[sideCode+2] = s0
        self.state = "".join(state)

    def frontCW(self):
        # rotate it side
        self.rotateSideCW(FRONT)
        # convert from string to a list, because a string is immutable
        state = list(self.state)
        u2, u3 = state[UP+2], state[UP+3]
        state[UP+2], state[UP+3] = state[LEFT+1], state[LEFT+3]
        state[LEFT+1], state[LEFT+3] = state[DOWN], state[DOWN+1]
        state[DOWN], state[DOWN+1] = state[RIGHT], state[RIGHT+2]
        state[RIGHT], state[RIGHT+2] = u2, u3
        # convert it back to string
        self.state = "".join(state)

    def frontCCW(self):
        self.rotateSideCCW(FRONT)
        # convert from string to a list, because a string is immutable
        state = list(self.state)
        u2, u3 = state[UP+2], state[UP+3]
        state[UP+2], state[UP+3] = state[RIGHT], state[RIGHT+2]
        state[RIGHT], state[RIGHT+2] = state[DOWN], state[DOWN+1]
        state[DOWN], state[DOWN+1] = state[LEFT+1], state[LEFT+3]
        state[LEFT+1], state[LEFT+3] = u3, u2
        # convert it back to string
        self.state = "".join(state)
    
    def upCW(self):
        self.rotateSideCW(UP)
        # convert from string to a list, because a string is immutable
        state = list(self.state)
        l0, l1 = state[LEFT], state[LEFT+1]
        state[LEFT], state[LEFT+1] = state[FRONT], state[FRONT+1]
        state[FRONT], state[FRONT+1] = state[RIGHT], state[RIGHT+1]
        state[RIGHT], state[RIGHT+1] = state[BACK], state[BACK+1]
        state[BACK], state[BACK+1] = l0, l1
        # convert it back to string
        self.state = "".join(state)

    def upCCW(self):
        self.rotateSideCCW(UP)
        # convert from string to a list, because a string is immutable
        state = list(self.state)
        l0, l1 = state[LEFT], state[LEFT+1]
        state[LEFT], state[LEFT+1] = state[BACK], state[BACK+1]
        state[BACK], state[BACK+1] = state[RIGHT], state[RIGHT+1]
        state[RIGHT], state[RIGHT+1] = state[FRONT], state[FRONT+1]
        state[FRONT], state[FRONT+1] = l0, l1
        # convert it back to string
        self.state = "".join(state)             

    def downCW(self):
        self.rotateSideCW(DOWN)
        # convert from string to a list, because a string is immutable
        state = list(self.state)
        l2, l3 = state[LEFT+2], state[LEFT+3]
        state[LEFT+2], state[LEFT+3] = state[BACK+2], state[BACK+3]
        state[BACK+2], state[BACK+3] = state[RIGHT+2], state[RIGHT+3]
        state[RIGHT+2], state[RIGHT+3] = state[FRONT+2], state[FRONT+3]
        state[FRONT+2], state[FRONT+3] = l2, l3
        # convert it back to string
        self.state = "".join(state)

    def downCCW(self):
        self.rotateSideCCW(DOWN)
        # convert from string to a list, because a string is immutable
        state = list(self.state)
        l2, l3 = state[LEFT+2], state[LEFT+3]
        state[LEFT+2], state[LEFT+3] = state[FRONT+2], state[FRONT+3]
        state[FRONT+2], state[FRONT+3] = state[RIGHT+2], state[RIGHT+3]
        state[RIGHT+2], state[RIGHT+3] = state[BACK+2], state[BACK+3]
        state[BACK+2], state[BACK+3] = l2, l3
        # convert it back to string
        self.state = "".join(state)

    def rightCW(self):
        self.rotateSideCW(RIGHT)
        # convert from string to a list, because a string is immutable
        state = list(self.state)
        b0, b2 = state[BACK], state[BACK+2]
        state[BACK], state[BACK+2] = state[UP+3], state[UP+1]
        state[UP+1], state[UP+3] = state[FRONT+1], state[FRONT+3]
        state[FRONT+1], state[FRONT+3] = state[DOWN+1], state[DOWN+3]
        state[DOWN+1], state[DOWN+3] = b2, b0
        # convert it back to string
        self.state = "".join(state)        

    def move(self, move):
        if(move == 'F'):
            self.frontCW()

    def printState(self):
        print(f'        +---+---+')
        print(f'        | {self.state[UP]} | {self.state[UP+1]} |')
        print(f'        +---+---+')
        print(f'        | {self.state[UP+2]} | {self.state[UP+3]} |')
        print(f'+---+---+---+---+---+---+---+---+')
        print(f'| {self.state[LEFT]} | {self.state[LEFT+1]} | {self.state[FRONT]} | {self.state[FRONT+1]} | {self.state[RIGHT]} | {self.state[RIGHT+1]} | {self.state[BACK]} | {self.state[BACK+1]} |')
        print(f'+---+---+---+---+---+---+---+---+')
        print(f'| {self.state[LEFT+2]} | {self.state[LEFT+3]} | {self.state[FRONT+2]} | {self.state[FRONT+3]} | {self.state[RIGHT+2]} | {self.state[RIGHT+3]} | {self.state[BACK+2]} | {self.state[BACK+3]} |')
        print(f'+---+---+---+---+---+---+---+---+')
        print(f'        | {self.state[DOWN]} | {self.state[DOWN+1]} |')
        print(f'        +---+---+')
        print(f'        | {self.state[DOWN+2]} | {self.state[DOWN+3]} |')
        print(f'        +---+---+')  


mycube = Cube()
mycube.frontCW()
mycube.printState()
# mycube.frontCCW()
mycube.upCW()
mycube.printState()
mycube.frontCCW()
mycube.printState()
mycube.downCCW()
mycube.printState()
mycube.upCCW()
mycube.printState()
mycube.downCW()
mycube.printState()
mycube.rightCW()
mycube.printState()
# mycube.printState()