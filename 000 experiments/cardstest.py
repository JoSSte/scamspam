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
from tools.cards import validate_card
from tools.cards import validate_luhn
from tools.cards import calculate_checkdigit


#Validating cards
cards = json.loads(open('../data/cards.json').read())
for card in cards:
    print("Validating %s to %s" % (card, validate_luhn(card)))

# checking checkdigit
c = '4012888888881881'
expected = 1
actual = calculate_checkdigit(c)
print("Checkdigit for %s should be %d is %s" % (c, actual, actual == expected))


for t in ['Dankort','VisaDankort','Visa','Visa-Electron','MasterCard','MasterCard2']:
    gc = generate_card(t)
    print("Validating %s to %s" % (gc, validate_luhn(gc)))
