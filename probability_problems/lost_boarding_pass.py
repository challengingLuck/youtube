# 1- The airplane has 100 seats and 100 passangers 
# 2- The first person has lost their boarding pass 
# 3- The first person goes in and they choose a seat at random 
# 4- Every other person goes in and: 
#    a) sits in their seat if their seat is open 
#    b) chooses a seat at random if their seat is taken
# 5- What is the probability that when the last person goes in their seat will be open 
# Note: For this simulation person 1 sits in seat 1, 2 in seat 2 and so on

import random
from random import choice

def find_random_seat(): 
    seat = choice([i for i in range(1,101) if i not in list_of_seats_already_taken])
    seat_assignment[seat] = "Occupied"
    list_of_seats_already_taken.append(seat)

number_of_reppetitions = 100
number_of_successful_events = 0 

for i in range (0, number_of_reppetitions): 
    seat_assignment = {}
    for seat in range(1,101): 
        seat_assignment[seat] = "Free"

    seat_that_first_person_takes = random.randint(1,100)
    seat_assignment[seat_that_first_person_takes] = "Occupied"
    list_of_seats_already_taken = [seat_that_first_person_takes]

    for passenger in range(2,101): 
        if seat_assignment[passenger] == "Free": 
            seat_assignment[passenger] = "Occupied"
            list_of_seats_already_taken.append(passenger) 
        else: 
            find_random_seat()

    
    if list_of_seats_already_taken[99] == 100:
        number_of_successful_events = number_of_successful_events + 1

    if list_of_seats_already_taken[99] == 1:
        number_of_successful_events = number_of_successful_events + 1



# print(seat_assignment)
print(list_of_seats_already_taken)
print("Probability that the last person gets to sit in their seat or in seat 1 is " + str(number_of_successful_events/number_of_reppetitions))
