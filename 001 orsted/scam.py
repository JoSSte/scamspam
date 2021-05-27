import requests
import os
import random
import string
import json
import datetime

random.seed = (os.urandom(1024))
#variables for random date
start_date = datetime.date(1940, 1, 1)
end_date = datetime.date(2003, 1, 1)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

url = 'https://ietarst-jansf7656.wpdevcloud.com/plugins/76g54fgf/24fhj23zet/jyukity68bf/gh65fdze43e/24qsfq24/valider.php'

names = json.loads(open('../data/names.json').read())
cards = json.loads(open('../data/cards.json').read())
surnames = json.loads(open('../data/surnames.json').read())
expiryYear = ["21","23","24"]
expiryMonth = ["01","02","03","04","05","06","07","08","09","10","11","12"]

for name in names:
    for surname in surnames:
        #Assemble full name
        fullname = name +' ' + surname
        #generate CVV
        cvv = ''.join(random.choice(string.digits) for i in range(3))
        #generate tel
        tlf = ''.join(random.choice(string.digits) for j in range(8))
        #generate random dob
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        dob = '%02d-%02d-%d' % (random_date.day, random_date.month, random_date.year)

        card = random.choice(cards)
        # select expiry year        
        aar = random.choice(expiryYear)
        #select expiry month
        mon = random.choice(expiryMonth)

        r = requests.post(url, allow_redirects=False, data={
        	    'yy' : fullname,
                'ii' : card,
                'rr' : mon, #MM
                'zz' : aar, #YY
                'vv' : cvv, # 3-digit CVV
                'aa' : tlf, # 8-digit telephone number
                'ss' : dob #dd-mm-yyyy
           	})
        print( 'Submitted [%d] fullname: %s card: %s mon: %s aar: %s cvv: %s tlf: %s dob: %s ' % (r.status_code, fullname, card, mon, aar, cvv, tlf, dob))