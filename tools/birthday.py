import random
import datetime

#variables for random date
start_date = datetime.date(1940, 1, 1) #this is not longer in the past than it is realistic to be born that year
end_date = datetime.date(2003, 1, 1) # you have to be 18 to have a credit card
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

#Generate random D.O.B between jan 1940 and jan 2003
def generate_birthdate():
    
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    dob = '%02d-%02d-%d' % (random_date.day, random_date.month, random_date.year)
    return dob
