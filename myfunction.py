import random

def compare(a, b, c):
    return (a == b and b == c and a != 0)
    
#check if the game is finished, return 1 if X wins, 2 if O wins and 0 if ties
def isFinish(inputBoard):
    result = 0
    for i in range(3):
        # - horizontal
        if compare(inputBoard[i][0], inputBoard[i][1], inputBoard[i][2]):
            result = inputBoard[i][0]
        # | vertical
        if compare(inputBoard[0][i], inputBoard[1][i], inputBoard[2][i]):
            result = inputBoard[0][i]

    # \
    if compare(inputBoard[0][0], inputBoard[1][1], inputBoard[2][2]):
            result = inputBoard[1][1]
    # /
    if compare(inputBoard[0][2], inputBoard[1][1], inputBoard[2][0]):
            result = inputBoard[1][1]

    return result

#return the score of the board
def fScore(inputBoard):
    result = isFinish(inputBoard)
    if result == 1:
        return 2
    elif result == 2:
        return -2
    else:
        return 0
    
