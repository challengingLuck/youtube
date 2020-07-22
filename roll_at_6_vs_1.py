# You either roll again at 6 or 1 
# You add the new number that you get to the previous one
# The person with the highest number wins

import random

def reroll_at_6 (starting_value):
    roll_number = random.randint(1,6)
    if(roll_number == 6):
        return(reroll_at_6(starting_value + roll_number))
    else:
        return(starting_value + roll_number)

def reroll_at_1 (starting_value):
    roll_number = random.randint(1,6)
    if(roll_number == 1):
        return(reroll_at_1(starting_value + roll_number))
    else:
        return(starting_value + roll_number)

wins_for_1 = 0; wins_for_6 = 0; ties = 0
repetitions = 100000

for i in range (0, repetitions):
    player_1 = reroll_at_1(0)
    player_6 = reroll_at_6(0)

    if (player_1 > player_6):
        wins_for_1 += 1
    
    if (player_1 < player_6):
        wins_for_6 += 1

    if (player_1 == player_6):
        ties += 1

print('Win percentage for 1: ', wins_for_1/repetitions * 100, '%')    
print('Win percentage for 6: ', wins_for_6/repetitions * 100, '%') 
print('Tie percentage: ', ties/repetitions * 100, '%') 
