'''
Program to increment a binary word by 1. This is to simulate a turing machine incrementing.
'''

typeHead = 0 #Index of where typehead would be
state = 0 # Initialisation state. 1 is main state. 2 is termination state

tape = [1,1,1,0,1,1,2,2,2,2] # 2 is my representation of the blank square
halted = False

def main(state, beltReading):
    global halted

    if state == 0:

        if beltReading == 0:
            movement(0,0,"right")
            # for (0,0) rule
        elif beltReading == 1:
            movement(0,1,"right")
            # for (0,1) rule
        elif beltReading == 2:
            movement(1, 2, "left")
            # for (0,2) rule

    elif state == 1:
        if beltReading == 0:
            movement(2,1,"right")
        elif beltReading == 1:
            movement(1,0,"left")
        elif beltReading == 2:
            halted = True

    elif state == 2:
        halted = True


def movement(newState, replacement, directionToMove):
    global state
    global typeHead

    state = newState
    tape[typeHead] = replacement
    if directionToMove == "right":
        typeHead += 1
    else:
        if (typeHead >= 1):
            typeHead -= 1
        else:
            typeHead = 0

while halted == False:
    main(state, tape[typeHead])

print(tape)