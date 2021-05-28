import random
import json
import string
import datetime

card_iins = json.loads(open('../data/iin.json').read())

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

def validate_card(cardnum):

    return validate_luhn(cardnum) and validate_iin(cardnum)

def validate_iin(cardnum):
    return False

# Calculate the checkdigit for a number
def calculate_checkdigit(number):
    #pad with 0 if odd length
    if len(number) % 2 != 0:
        number = number + '0'
    checkdigit = 0
    digits = list(map(int, number))
    csum = 0
    for x in range(0, len(digits)-1):
        #Double every second digit from the back. TODO: Change the modulus function if the number is odd instead of even
        if((x + 1) % 2 != 0):
            digits[x] = sum_digits(2 * digits[x])
        csum += digits[x]
    checkdigit = (csum * 9) % 10
    return checkdigit

#Validate whether the card number validates aaccording to the Luhn algorithm
def validate_luhn(cardnum):

    return_val = False
    checkdigit = calculate_checkdigit(cardnum)
    if checkdigit == int(cardnum[len(cardnum)-1]):
        return_val = True
    return return_val


def generate_card(ctype):
    iin = 0
    for iin_item in card_iins:
        if iin_item['name'] == ctype:
            iin = str(random.choice(iin_item['iin']))
    cardnum = iin + ''.join(random.choice(string.digits) for j in range(15-len(iin)))
    checkdigit = calculate_checkdigit(cardnum)
    cardnum = cardnum + str(checkdigit)
    return cardnum

#Generators for dates

current_year = datetime.datetime.now().year - 2000
max_validity = 4
valid_expiry_year_list = list(range(current_year, current_year + max_validity))
expired_expiry_year_list = list(range(current_year - 9, current_year))

def generate_expiry_year(valid=True):
    if valid:
        year = random.choice(valid_expiry_year_list)
    else:
        year = random.choice(expired_expiry_year_list)
    return year
