import cv2
import time
import numpy as np
from myfunction import *
import pyautogui as pag
from minimax import miniMax

#FHD_____________________________
mouseClickPosX = [330, 480, 630]
mouseClickPosY = [355, 505, 655]

checkPixelPosY = [112, 262, 412]
checkPixelPosX = [54, 204, 354]

pixelPos = [82, 232, 382]
#________________________________
 

while(1):
    board = np.zeros((3, 3))
    playing = True
    print("Playing!")
    while(playing):
        time.sleep(1)
        img = np.array(pag.screenshot(region = (247, 271, 465, 465)))
        emptySlot = 0
        for i in range(3):
            for j in range(3):
                #check at position i j in the image has been marked or not
                if (img[checkPixelPosX[i]][checkPixelPosY[j]][0] != 0):
                    #if it has been marked, check if it is X or O
                    if (img[pixelPos[i]][pixelPos[j]][0] != 0):
                        board[i][j] = 1 #X
                    else:
                        board[i][j] = 2 #O
                else:
                    #count the number of empty slots
                    emptySlot += 1      
        
        if (isFinish(board) != 0 or emptySlot == 0):
            break

        print("finding next step...")
        nextClick = miniMax(board, 7, emptySlot)

        print("next step: ", nextClick)
        pag.click(x = mouseClickPosX[nextClick[1]], y = mouseClickPosY[nextClick[0]])
        
    for sec in range(3, 0, -1):
        print(sec, "...")
        time.sleep(1)
    pag.click(x = 403, y = 403)


    