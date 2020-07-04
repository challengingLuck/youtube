# There are three doors 
# You choose a door at random
# After you make the choice the host will open one of the two doors left
# The door that the host opens always contains a goat 
# Should you change your choice or not 
import random
from random import choice

repetitions = 100000
number_of_successful_events_with_no_change = 0
number_of_successful_events_with_the_change = 0
for i in range(1,repetitions):
    doors = {}
    prizes = ["goat", "car","goat"]
    for i in range(1,4):
        prize_for_door_i = prizes.pop(random.randrange(len(prizes))) 
        doors[i] = prize_for_door_i

    players_choice = random.randint(1,3)
    hosts_removed_door = choice([i for i in range(1,4) if i is not players_choice and doors[i] == "goat"])
    door_left = choice([i for i in range (1,4) if i is not players_choice and i is not hosts_removed_door])

    if doors[players_choice] == "car":
        number_of_successful_events_with_no_change += 1 

    if doors[door_left] == "car":
        number_of_successful_events_with_the_change += 1 

print("Win percentage with change:", number_of_successful_events_with_the_change/repetitions)
print("Win percentage with no change:", number_of_successful_events_with_no_change/repetitions)
