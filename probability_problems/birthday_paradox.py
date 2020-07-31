# What is the probability that it is more likely than not that two people 
# in a group share the same birthday

from datetime import date
import random

def calculate_real_probability ():
    probability_not_sharing_birthday = 1 
    number_of_people = 0
    for i in range(365, 1, -1):
        number_of_people += 1
        probability_not_sharing_birthday *= (i/365) # 365/365 * 364/365 * 363/365 ....
        print(number_of_people, (1-probability_not_sharing_birthday)*100)

        if (1-probability_not_sharing_birthday > 0.5):
            break

def random_birthday(): 
    start_dt = date.today().replace(day=1, month=1).toordinal()
    end_dt = date.today().replace(day=31, month=12).toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    return(str(random_day))

def calculate_simulated_probability():
    for number_of_people in range(1,365):
        number_of_successful_events = 0
        repetitions = 10000
        for x in range (0,repetitions):
            all_birthdays = []
            for i in range (0,number_of_people):

                birthday = random_birthday()
                if birthday in all_birthdays:
                    number_of_successful_events += 1
                    break
                else:
                    all_birthdays.append(birthday) 

        print(number_of_people, number_of_successful_events/repetitions * 100)

        if(number_of_successful_events/repetitions > 0.5):
            break

calculate_simulated_probability()