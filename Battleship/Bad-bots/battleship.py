import numpy as np
import random
import matplotlib.pyplot as plt 
import seaborn as sns
from matplotlib import colors
from matplotlib import rcParams

opponentsBoard = np.zeros((10,10))
opponentsBoard[0:5,1] = 1
opponentsBoard[3,4:7] = 1
opponentsBoard[5:9,8] = 1
opponentsBoard[6,0:3] = 1
opponentsBoard[9,6:8] = 1
visitedBoard = np.zeros((10,10))
boardWithProbabilities = np.zeros((10,10))


def generatePlot(board, counter):
    name = "plot" + str(counter)
    cmap = 'plasma'

    ax = sns.heatmap(board, linewidth=0.5, cmap=cmap, cbar=False)
    plt.legend([],[], frameon=False)
    ax.set_xticklabels(['1','2','3','4','5','6','7','8','9','10'])
    ax.set_yticklabels(['10','9','8','7','6','5','4','3','2','1'])
    rcParams['figure.figsize'] = 11,11
    plt.savefig(name)

listOfAvailableMoves = []
for i in range(0,10):
    for j in range(0,10):
        listOfAvailableMoves.append(str(i)+str(j))


def randomGuessBot(opponentsBoard, visitedBoard, counter,successfulHits,listOfAvailableMoves):
    if successfulHits >=17:
        print("number of turns:" + str(counter), "number of hits:" + str(successfulHits))
        generatePlot(visitedBoard, counter)
        return(True)
    random_num = random.choice(listOfAvailableMoves)
    listOfAvailableMoves.remove(random_num)
    row = int(random_num[0])
    col = int(random_num[1])
    generatePlot(visitedBoard, counter)

    if opponentsBoard[row, col] == 1:
        successfulHits +=1
        visitedBoard[row, col] = 1
    else:
        visitedBoard[row, col] = 2

    randomGuessBot(opponentsBoard, visitedBoard, counter+1, successfulHits, listOfAvailableMoves)


def generateRandomMove(listOfAvailableMoves):
    return(random.choice(listOfAvailableMoves))

def generateNextMove(boardWithProbabilities):
    return(np.unravel_index(boardWithProbabilities.argmax(), boardWithProbabilities.shape))

def createProbabilitiesBoard(boardWithProbabilities, lastHit):
    if lastHit[0]>=0 and lastHit[0]<=9 and lastHit[1]+1>=0 and lastHit[1]+1<=9:
        if boardWithProbabilities[lastHit[0], lastHit[1]+1] == 0:
            boardWithProbabilities[lastHit[0], lastHit[1]+1] = 0.25

    if lastHit[0]>=0 and lastHit[0]<=9 and lastHit[1]-1>=0 and lastHit[1]-1<=9:
        if boardWithProbabilities[lastHit[0], lastHit[1]-1] == 0:
            boardWithProbabilities[lastHit[0], lastHit[1]-1] = 0.25
    
    if lastHit[0]+1>=0 and lastHit[0]+1<=9 and lastHit[1]>=0 and lastHit[1]<=9:
        if boardWithProbabilities[lastHit[0]+1, lastHit[1]] == 0:
            boardWithProbabilities[lastHit[0]+1, lastHit[1]] = 0.25

    if lastHit[0]-1>0 and lastHit[0]<=9 and lastHit[1]-1>=0 and lastHit[1]<=9:
        if boardWithProbabilities[lastHit[0]-1, lastHit[1]] == 0:
            boardWithProbabilities[lastHit[0]-1, lastHit[1]] = 0.25

    return(boardWithProbabilities)

def randomUsingProbability (opponentsBoard, turnCounter, succesfulHits, listOfAvailableMoves, boardWithProbabilities, lastHit, missed, visitedBoard):
    if succesfulHits >= 17 or turnCounter>=100:
        print("Number of turns: " + str(turnCounter), "Hits:" + str(succesfulHits))
        generatePlot(visitedBoard, turnCounter+100)
        return

    if (lastHit == -1): #last hit was miss && don't know have a place to check, so we take random guess
        print("random", turnCounter)
        random_num = generateRandomMove(listOfAvailableMoves)
        listOfAvailableMoves.remove(random_num)
        row = int(random_num[0])
        col = int(random_num[1])
        generatePlot(visitedBoard, turnCounter+100)

        if opponentsBoard[row,col] == 1:    
            succesfulHits += 1
            lastHit = [row,col]
            visitedBoard[row,col] = 1
            boardWithProbabilities[row,col]=-10 # random hit
            visitedBoard[row,col]=1
            createProbabilitiesBoard(boardWithProbabilities, lastHit)

        else:
            boardWithProbabilities[row,col]=-1 # miss
            visitedBoard[row,col]=2


    else:
        nextHit = generateNextMove(boardWithProbabilities)
        position = str(nextHit[0])+str(nextHit[1])
        if position in listOfAvailableMoves:  # should always be true
            listOfAvailableMoves.remove(position)     
            row = nextHit[0]
            col = nextHit[1]
            generatePlot(visitedBoard, turnCounter+100)
            if boardWithProbabilities[row,col] == 0:  #out of guesses
                lastHit = -1
                
            boardWithProbabilities[row,col]=-1

            if opponentsBoard[row,col] == 1:    
                succesfulHits += 1
                lastHit = [row,col]
                visitedBoard[row,col] = 1
                boardWithProbabilities[row,col]=-100 # rated move hit
                visitedBoard[row,col]=1
                missed = 0
            else:
                missed = 1
                visitedBoard[row,col]=2
            
    randomUsingProbability (opponentsBoard, turnCounter+1, succesfulHits, listOfAvailableMoves, boardWithProbabilities, lastHit, missed, visitedBoard)

randomUsingProbability (opponentsBoard, 0, 0, listOfAvailableMoves, boardWithProbabilities, -1, 0, visitedBoard)


# randomGuessBot(opponentsBoard, visitedBoard, 0, 0, listOfAvailableMoves)
# print(listOfAvailableMoves)
# generatePlot(opponentsBoard)
# print(opponentsBoard)
