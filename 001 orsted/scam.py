import requests
import os
import random
import string
import json
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from tools.birthday import generate_birthdate
import tools.cards

send = False
random.seed = (os.urandom(1024))

url = 'https://ietarst-jansf7656.wpdevcloud.com/plugins/76g54fgf/24fhj23zet/jyukity68bf/gh65fdze43e/24qsfq24/valider.php'

card_types = ['VisaDankort','Visa','Visa-Electron','MasterCard']
names = json.loads(open('../data/names.json', encoding='utf-8').read())
surnames = json.loads(open('../data/surnames.json', encoding='utf-8').read())

for name in names:
    for surname in surnames:
        #Assemble full name
        fullname = name +' ' + surname
        #Generate CVV
        cvv = ''.join(random.choice(string.digits) for i in range(3))
        #Generate telephone number
        tlf = ''.join(random.choice(string.digits) for j in range(8))
        dob = generate_birthdate()
        #generate a random card, based on a random card type
        card = tools.cards.generate_card(random.choice(card_types))
        
        expiry_year, expiry_month = tools.cards.generate_expiry_date()
        
        if send:
            r = requests.post(url, allow_redirects=False, data={
            	    'yy' : fullname,
                    'ii' : card,
                    'rr' : expiry_month, #MM
                    'zz' : expiry_year, #YY
                    'vv' : cvv, # 3-digit CVV
                    'aa' : tlf, # 8-digit telephone number
                    'ss' : dob #dd-mm-yyyy
               	})
            print( 'Submitted [%d] ' % (r.status_code), end="\t")
        else:
            print('Send is disabled.', end="\t")
        print("Data:\tcard: %s\texpiry_month: %s\texpiry_year: %s\tcvv: %s\ttlf: %s\tdob: %s\tfullname: %s " % (card, expiry_month, expiry_year, cvv, tlf, dob, fullname))
        