import requests
import os
import random
import string
import json
import datetime

send = False
random.seed = (os.urandom(1024))

#this ear, in short format
current_year = datetime.datetime.now().year - 2000
current_month = datetime.datetime.now().month

#variables for random date
start_date = datetime.date(1940, 1, 1) #this is not longer in the past than it is realistic to be born that year
end_date = datetime.date(2003, 1, 1) # you have to be 18 to have a credit card
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

url = 'https://ietarst-jansf7656.wpdevcloud.com/plugins/76g54fgf/24fhj23zet/jyukity68bf/gh65fdze43e/24qsfq24/valider.php'

names = json.loads(open('../data/names.json').read())
cards = json.loads(open('../data/cards.json').read())
surnames = json.loads(open('../data/surnames.json').read())
expiryYear = list(range(current_year, current_year + 4)) #since cards are typically valid about 4 years, and they
expiryMonth = list(range(1,13))

#Check if the selected month is in the past, and fix it if it is so
if expiryYear == current_year and expiryMonth < current_month:
    expiryMonth = current_month

for name in names:
    for surname in surnames:
        #Assemble full name
        fullname = name +' ' + surname
        #Generate CVV
        cvv = ''.join(random.choice(string.digits) for i in range(3))
        #Generate telephone number
        tlf = ''.join(random.choice(string.digits) for j in range(8))
        #Generate random D.O.B
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        dob = '%02d-%02d-%d' % (random_date.day, random_date.month, random_date.year)

        card = random.choice(cards)
        # select expiry year        
        aar = random.choice(expiryYear)
        #select expiry month
        mon = '{:02d}'.format(random.choice(expiryMonth))
        if send:
            r = requests.post(url, allow_redirects=False, data={
            	    'yy' : fullname,
                    'ii' : card,
                    'rr' : mon, #MM
                    'zz' : aar, #YY
                    'vv' : cvv, # 3-digit CVV
                    'aa' : tlf, # 8-digit telephone number
                    'ss' : dob #dd-mm-yyyy
               	})
            print( 'Submitted [%d] ' % (r.status_code), end="\t")
        else:
            print('Send is disabled.', end="\t")
        print("Data:\tcard: %s\tmon: %s\taar: %s\tcvv: %s\ttlf: %s\tdob: %s\tfullname: %s " % (card, mon, aar, cvv, tlf, dob, fullname))
        