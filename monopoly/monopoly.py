import numpy as np 
import sys
import scipy.linalg as la

def CalculateRollProbabilites ():
    rollProbabilities = [1,2,3,4,5,6,5,4,3,2,1]
    rollProbabilities = [x / 36 for x in rollProbabilities]
    return (rollProbabilities)


#Function to create the roll matrix
def CreateMatrix (probabilities, matrix, counter, dim):
    if counter == dim:
        return (matrix)

    lastElement = probabilities.pop()
    probabilities = [lastElement] +probabilities
    matrix[:,counter] = probabilities
    CreateMatrix (probabilities, matrix, counter+1, dim)

###################################################################################################################################
goSquareProbabilities = [0]*40
goSquareProbabilities[2:13] = CalculateRollProbabilites()
rollMatrix = np.zeros((40, 40))
rollMatrix[:,0] = goSquareProbabilities
CreateMatrix(goSquareProbabilities, rollMatrix, 1, 40)
# Add two columns of 0s




rollMatrix = np.column_stack((rollMatrix, ([0] *40)))
rollMatrix = np.column_stack((rollMatrix, ([0] *40)))

rollMatrix = np.row_stack((rollMatrix, ([0] *42)))
rollMatrix = np.row_stack((rollMatrix, ([0] *42)))


rollMatrix[41,40] = 5.0/6
rollMatrix[10,41] = 5.0/6

#in case you roll doubles and get out of jail
rollMatrix[[12,14,16,18,20,22],40] = 1.0/36
rollMatrix[[12,14,16,18,20,22],41] = 1.0/36
#######################################################################################################################################





######################################################################################################################################
goToJailRow = [1] + [0]*41
goToJailMatrix = np.zeros((42, 42))
goToJailMatrix[0] = goToJailRow
CreateMatrix(goToJailRow, goToJailMatrix,1,42)

# Send the player to the first part of the jail. 
goToJailMatrix[40,30] = 1 
goToJailMatrix[30,30] = 0


######################################################################################################################################

#####################################################################################################################################
# Advance to Go
# Go to Jail
# Go to Illinois Avenue
# Go to St. Charles
# Take a walk on the Boardwalk (Go to Boardwalk)
# Go back three spaces
# Go to nearest Utility (depends on which Chance location you are on)
# Go to nearest Railroad - there are two of these cards
# Go to Reading Railroad

chanceRow = [1] + [0]*41
chanceMatrix = np.zeros((42, 42))
chanceMatrix[0] = chanceRow
CreateMatrix(chanceRow, chanceMatrix,1,42)

chanceMatrix[:,7] = [0]*42
chanceMatrix[[0,10,24,11,39,5,4,12],7] = 1.0/16
chanceMatrix[15,7] = 2.0/16
chanceMatrix[7,7] = 6.0/16

chanceMatrix[:,22] = [0]*42
chanceMatrix[[0,10,24,11,39,5,19,28],22] = 1.0/16
chanceMatrix[25,22] = 2.0/16
chanceMatrix[22,22] = 6.0/16

chanceMatrix[:,36] = [0]*42
chanceMatrix[[0,10,24,11,39,33,12],36] = 1.0/16
chanceMatrix[5,36] = 3.0/16
chanceMatrix[36,36] = 6.0/16


#########################################################################################################################################


####################################################################################################################################
# Community chest has 16 cards and two of them move you around. So probability to stay is 14.0/16, and probability to go to jail, or advance to go is 1.0/16. 
# Community chest is located at spots 3, 18 and 34 

communityRow = [1] + [0]*41
communityMatrix = np.zeros((42, 42))
communityMatrix[0] = communityRow
CreateMatrix(communityRow, communityMatrix,1,42)

communityMatrix[[0,40],2] = 1.0/16
communityMatrix[2,2] = 14.0/16

communityMatrix[[0,40],17] = 1.0/16
communityMatrix[17,17] = 14.0/16

communityMatrix[[0,40],33] = 1.0/16
communityMatrix[33,33] = 14.0/16

##################################################################################################################################



############# Three doubles and you go to jail part ##############################################################################

# Matrix similar to the identity one. 
threeDoublesJailRow = [215.0/216] + [0]*41
threeDoublesJailMatrix = np.zeros((42, 42))
threeDoublesJailMatrix[0] = threeDoublesJailRow
CreateMatrix(threeDoublesJailRow, threeDoublesJailMatrix,1,42)


#sending every other state to jail with probability 1.0/216
threeDoublesJailMatrix[41,[range(0,40)]]=1.0/216
threeDoublesJailMatrix[30,30]=0
threeDoublesJailMatrix[40,30]=1

threeDoublesJailMatrix[41,41]=1
threeDoublesJailMatrix[40,40]=1

print(threeDoublesJailMatrix)


####################################################################################################################################
finalMatrix = np.matmul(np.matmul(np.matmul(np.matmul(communityMatrix, chanceMatrix), goToJailMatrix), rollMatrix), threeDoublesJailMatrix)
eigenVector = la.eig(finalMatrix)[1]
steadyStateVec = eigenVector[:,0]
steadyStateVec = steadyStateVec/sum(steadyStateVec)

for element in steadyStateVec:
    print (element)
