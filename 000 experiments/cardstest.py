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
from tools.cards import generate_expiry_year

# checking checkdigit
c = '4012888888881881'
expected = 1
actual = calculate_checkdigit(c)
print("Checkdigit for %s should be %d is %s" % (c, actual, actual == expected))

#generate and validate 20 cards of each type
for t in ['Dankort','VisaDankort','Visa','Visa-Electron','MasterCard','MasterCard2']:
    for x in range(20):
        gc = generate_card(t)
        print("Validating %s card %s to %s" % (t, gc, validate_luhn(gc)))

print(generate_expiry_year())
print(generate_expiry_year(True))
print(generate_expiry_year(False))
