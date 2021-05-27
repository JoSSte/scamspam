import requests
import os
import random
import string
import json
import datetime
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from tools.cards import generate_card
from tools.birthday import generate_birthdate

send = False
random.seed = (os.urandom(1024))

#this ear, in short format
current_year = datetime.datetime.now().year - 2000
current_month = datetime.datetime.now().month

url = 'https://ietarst-jansf7656.wpdevcloud.com/plugins/76g54fgf/24fhj23zet/jyukity68bf/gh65fdze43e/24qsfq24/valider.php'

card_types = ['Dankort','VisaDankort','Visa','Visa-Electron','MasterCard']
names = json.loads(open('../data/names.json', encoding='utf-8').read())
surnames = json.loads(open('../data/surnames.json', encoding='utf-8').read())
expiry_year = list(range(current_year, current_year + 4)) #since cards are typically valid about 4 years, and they have to be valid
expiry_month = list(range(1,13))

#Check if the selected month is in the past, and fix it if it is so
if expiry_year == current_year and expiry_month < current_month:
    expiry_month = current_month

for name in names:
    for surname in surnames:
        #Assemble full name
        fullname = name +' ' + surname
        #Generate CVV
        cvv = ''.join(random.choice(string.digits) for i in range(3))
        #Generate telephone number
        tlf = ''.join(random.choice(string.digits) for j in range(8))
        dob = generate_birthdate()
        card = generate_card(random.choice(card_types))
        # select expiry year        
        aar = random.choice(expiry_year)
        #select expiry month
        mon = '{:02d}'.format(random.choice(expiry_month))
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
        