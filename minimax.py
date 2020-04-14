from myfunction import fScore

def maxVal(inputBoard, depth, slotsLeft):
    score = fScore(inputBoard)
    val = -10000000
    if slotsLeft == 0 or depth == 0 or score != 0:
        val = score
    else:
        for i in range(3):
            for j in range(3):
                if inputBoard[i][j] == 0:
                    inputBoard[i][j] = 1    #set X at board[i][j]
                    temp = minVal(inputBoard, depth-1, slotsLeft-1)
                    inputBoard[i][j] = 0
                    val = max(val, temp)
    return val-depth


def minVal(inputBoard, depth, slotsLeft):
    score = fScore(inputBoard)
    val = 10000000
    if slotsLeft == 0 or depth == 0 or score != 0:
        val = score
    else:
        for i in range(3):
            for j in range(3):
                if inputBoard[i][j] == 0:
                    inputBoard[i][j] = 2    #set O at board[i][j]
                    temp = maxVal(inputBoard, depth-1, slotsLeft-1)
                    inputBoard[i][j] = 0
                    val = min(val, temp)
    return val+depth



def miniMax(inputBoard, depth, slotsLeft):
    val = -1000000
    first = True
    result = (0, 0)
    for i in range(3):
        for j in range(3):
            #1 == X
            if inputBoard[i][j] == 0:
                if first:
                    result = (i, j)
                    first = False
                inputBoard[i][j] = 1 
                tempval = minVal(inputBoard, depth-1, slotsLeft-1)
                inputBoard[i][j] = 0
                if tempval > val:
                    val = tempval
                    result = (i, j)
    return result

