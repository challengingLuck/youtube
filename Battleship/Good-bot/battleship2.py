import numpy as np
import random 
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors
from matplotlib import rcParams

def generatePlot(board_with_probabilities, turn_counter):
    name = "plot" + str(turn_counter)

    cmap = colors.ListedColormap(['slateblue','red','lightgrey']) if turn_counter >= 100 else 'plasma'        

    ax = sns.heatmap(board_with_probabilities , linewidth = 0.5 , cmap = cmap, cbar=False)
    plt.legend([],[], frameon=False)
    ax.set_xticklabels(['1','2','3','4','5','6','7','8', '9', '10'])
    ax.set_yticklabels(['10','9','8','7','6','5','4','3', '2', '1'])
    rcParams['figure.figsize'] = 11,11
    # plt.imshow(board_with_probabilities, cmap='plasma', linewidth = 0.5)
    plt.savefig(name)

def saveCSV(board_with_probabilities, turn_counter):
    name = "textfile" + str(turn_counter) + ".csv"
    np.savetxt(name, board_with_probabilities, delimiter=",")

def generateRandomBoard():
    opponents_board = np.full((10, 10), 0)
    ships = [5,4,3,3,2]

    for length_of_the_ship in ships:
        placed = False
        while placed == False:
            col_or_row = random.randint(0,1)
            
            # row
            if col_or_row == 1:  
                empty_slot_counter = 0              
                random_row = random.randint(0,9)
                random_col = random.randint(0,9-length_of_the_ship)

                for i in range(0,length_of_the_ship):
                    if opponents_board[random_row,random_col+i] == 0:
                        empty_slot_counter += 1

                if empty_slot_counter == length_of_the_ship:
                    for i in range(0,length_of_the_ship):
                        opponents_board[random_row,random_col+i] = 1
                    placed = True

            # col
            if col_or_row == 0:  
                empty_slot_counter = 0              
                random_col = random.randint(0,9)
                random_row = random.randint(0,9-length_of_the_ship)

                for i in range(0,length_of_the_ship):
                    if opponents_board[random_row+i,random_col] == 0:
                        empty_slot_counter += 1

                if empty_slot_counter == length_of_the_ship:
                    for i in range(0,length_of_the_ship):
                        opponents_board[random_row+i,random_col] = 1
                    placed = True

    return(opponents_board)

def possibibleLocationsProbability(board_with_hits, board_with_misses, length_of_the_ship):
    list_of_probabilities = []
    
    # Check all rows for possible locations
    for row in range(0,10):
        for col in range(0,11-length_of_the_ship):
            positions_to_consider = range(col, col+length_of_the_ship)
            # State where hits happened
            positions_with_hits = []
            empty_slot_counter = 0
            # Check if the elements of a list all correspond to 0s, and if they do create a matrix where that segment has a certain probabiliity
            for element in positions_to_consider:
                if board_with_misses[row,element] == 0:
                    if board_with_hits[row, element] == 1:
                        positions_with_hits.append(element)    
                    empty_slot_counter += 1

            # Check if the number of continious empty slots corresponds to the length of the ship   
            if empty_slot_counter == length_of_the_ship:
                new_state = np.full((10, 10), 0.0)
                if_there_is_hit = 4*len(positions_with_hits) if len(positions_with_hits) else 1
                for element in positions_to_consider:
                    if element in positions_with_hits:
                        new_state[row, element] = 0
                    else:    
                        new_state[row,element] = float(length_of_the_ship) * if_there_is_hit
                list_of_probabilities.append(new_state)

    # Check all cols for possible locations
    for col in range(0,10):
        for row in range(0,11-length_of_the_ship):
            positions_to_consider = range(row, row+length_of_the_ship)
            positions_with_hits = []
            empty_slot_counter = 0

            # Check if the elements of a list all correspond to 0s, and if they do create a matrix where that segment has a certain probabiliity
            for element in positions_to_consider:
                if board_with_misses[element,col] == 0:
                    if board_with_hits[element,col] == 1:
                        positions_with_hits.append(element)
                    empty_slot_counter += 1

            # Check if the number of continious empty slots corresponds to the length of the ship   
            if empty_slot_counter == length_of_the_ship:
                if_there_is_hit = 4 if len(positions_with_hits) else 1

                new_state = np.full((10, 10), 0.0)
                for element in positions_to_consider:
                    if element in positions_with_hits:
                        new_state[element,col] = 0
                    else:    
                        new_state[element,col] = float(length_of_the_ship) * if_there_is_hit
                list_of_probabilities.append(new_state)


    final_matrix = np.full((10, 10), 0)
    for curr_matrix in list_of_probabilities:
        final_matrix = np.add(final_matrix, curr_matrix)

    return(final_matrix)

def generateProbabilitiesForAllShips(board_with_hits, board_with_misses):
    final = np.full((10, 10), 0)
    ships = [5,4,3,3,2]
    for i in ships:
        probabilites = possibibleLocationsProbability(board_with_hits, board_with_misses, i)
        final = np.add(final, probabilites)
    return(final)

def generateNextMove(board_with_probabilities):
    return(np.unravel_index(board_with_probabilities.argmax(), board_with_probabilities.shape))

def bot (opponents_board, board_with_hits, board_with_misses, turn_counter, successful_hits):
    if successful_hits >= 17 or turn_counter>=100:
        generatePlot((board_with_hits+board_with_misses), turn_counter + 100)
        return (turn_counter)

    board_with_probabilities = generateProbabilitiesForAllShips(board_with_hits, board_with_misses)
    nextHit = generateNextMove(board_with_probabilities)
    row = nextHit[0]
    col = nextHit[1]
    generatePlot(board_with_probabilities, turn_counter)
    generatePlot((board_with_hits+board_with_misses), turn_counter + 100)
    # saveCSV(board_with_probabilities, turn_counter)

    if opponents_board[row,col] == 1:    
        successful_hits += 1
        board_with_hits[row,col] = 1
        board_with_probabilities[row,col] = 0 

    else:
        board_with_misses[row,col] = 2

    return (bot (opponents_board, board_with_hits, board_with_misses, turn_counter+1, successful_hits))


final_sum = 0
opponents_board = generateRandomBoard()
board_with_probabilities = np.zeros((10,10))
board_with_hits = np.zeros((10,10))
board_with_misses = np.zeros((10,10))
final_sum += bot(opponents_board, board_with_hits, board_with_misses, 0, 0)
# generateProbabilitiesForAllShips(board_with_hits, board_with_misses)
# print(final_sum/100)
# plt.imshow(board_with_probabilities, cmap='hot')
# plt.show()
