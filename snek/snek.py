import time
import random
import msvcrt

#global snekLen
global running
running = True

def updateSnek():
    counter = 0
    #for posIndex in snekPos:
    #    if axisIndex[posIndex[2]]:  
     #       snekPos[counter][1] += dirVal[posIndex[2]]
      #      if snekPos[counter][1] < 0:
       #         snekPos[counter][1] = 9
        #    elif snekPos[counter][1] > 9:
         #       snekPos[counter][1] = 0
#        else:
 #           snekPos[counter][0] += dirVal[posIndex[2]]
  #          if snekPos[counter][0] < 0:
   #             snekPos[counter][0] = 9
    #        elif snekPos[counter][0] > 9:
     #           snekPos[counter][0] = 0
      #  counter+= 1
    partContainer = snekPos[0].copy()
    if axisIndex[snekPos[0][2]]:  
        snekPos[0][1] += dirVal[snekPos[0][2]]
        if snekPos[0][1] < 0:
           snekPos[0][1] = 9
        elif snekPos[0][1] > 9:
            snekPos[0][1] = 0
    else:
        snekPos[0][0] += dirVal[snekPos[0][2]]
        if snekPos[0][0] < 0:
            snekPos[0][0] = 9
        elif snekPos[0][0] > 9:
            snekPos[0][0] = 0
    for part in range(1, len(snekPos)):
        temp = snekPos[part].copy()
        snekPos[part] = partContainer.copy()
        partContainer = temp.copy()

def updateFrame():
    map = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
    map[applePos[1]][applePos[0]] = "@"
    notHead = False
    for posIndex in snekPos:
        if notHead:
            map[posIndex[1]][posIndex[0]] = "#"
        else:
            if axisIndex[posIndex[2]]:  
                if dirVal[posIndex[2]] == 1:
                    map[posIndex[1]][posIndex[0]] = "V"
                else:
                    map[posIndex[1]][posIndex[0]] = "^"
            else:
                if dirVal[posIndex[2]] == 1:
                    map[posIndex[1]][posIndex[0]] = ">"
                else:
                    map[posIndex[1]][posIndex[0]] = "<"
        notHead = True
    return map

def moveApple():
    check = True
    while check:
        applePos[0] = random.randint(0, 9)
        applePos[1] = random.randint(0, 9)
        check = False
        for offset in range(0, 3):
           if snekPos[0][0] + dirVal[offset] == applePos[0]:
               check = True
               break
           if snekPos[0][1] + dirVal[offset] == applePos[1]:
               check = True
               break
        for part in snekPos:
            if part[0] == applePos[0] and part[1] == applePos[1]:
                check = True
                break
def checkApple():
    if snekPos[0][0] == applePos[0] and snekPos[0][1] == applePos[1]:
        lastSnekPos = []
        lastSnekPos = snekPos[len(snekPos) - 1].copy()
        if axisIndex[lastSnekPos[2]]:
            lastSnekPos[1] -= dirVal[lastSnekPos[2]]
        else:
            lastSnekPos[0] -= dirVal[lastSnekPos[2]]
        if lastSnekPos[0] > 9:
            lastSnekPos[0] = 0
        elif lastSnekPos[0] < 0:
            lastSnekPos[0] = 9
        if lastSnekPos[1] > 9:
            lastSnekPos[1] = 0
        elif lastSnekPos[1] < 0:
            lastSnekPos[1] = 9
        snekPos.append(lastSnekPos)
        #snekLen += 1
        moveApple()
def getInput():
    #move = ''
    #move = input("move")
    #if move == 'w' or move == 'a' or move == 's' or move == 'd':
     #   snekPos[0][2] = charDir[move]
    #else:
     #   return
    global running
    if msvcrt.kbhit():
        text = msvcrt.getch()
        if text == b'w' or text == b'a' or text == b's' or text == b'd':
            snekPos[0][2] = charDir[text]
        if text == b'\x1b':
            running = False

def checkCollision():
    global running
    prevPart = snekPos[0].copy()
    for part in snekPos[1:]:
        if part[0] == prevPart[0] and part[1] == prevPart[1]:
            running = False
tick = 0
board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ">", ".", "@", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
#snekLen = 0
#DIRECTIONS
#   ^0
# <3  >1
#   V2
charDir = {b'w' : 0,
           b'd' : 1,
           b's' : 2,
           b'a' : 3}
dirVal = {0 : -1,
            1 : 1,
            2 : 1,
            3 : -1}
axisIndex = {0 : True, #v
             1 : False, #h
             2 : True, #v
             3 : False} #h
#snekDir = 1
#[head, body segments][x, y, rotation]
snekPos = [[1, 2, 1], [0, 2, 1]]
applePos = [0, 8]
while (running):
    tick += 1
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    #running = True
    #game code
    updateSnek()

    checkApple()

    board = updateFrame()

    #print('itWork')
    checkCollision()

    #end tick
    #render frame
    for row in board:
        for item in row:
            print(item, end=" ")
        print()
    for i in range(60):
        getInput()
        time.sleep(1/960)
Length = len(snekPos)
print(f'you finished with a length of {Length}')