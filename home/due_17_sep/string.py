# The following are some questions that were all on the final slide of the homework powerpoint,
# so I decided to keep them all in a single file as they were quite short and similar.
# The inputs/outputs for each function has been commented below the subprogram.

# this function makes every second character of the string uppercase
# and every other character lower case.
def capitalise_string(string):
    i = 0
    new_string = ''
    for letter in string:
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
        i += 1
    
    return new_string

# print('Modified String:')
# print(capitalise_string('SIVASATYANbalasundaram'))

# this function calculates the total ascii value for all the characters in the string
# and then adds 2 at the end (as per mr travi's instructions :) ). 
def calculate_ascii(string):
    total = 0
    for letter in string:
        total += ord(letter)
    return total + 2

# print('ASCII Total:')
# print(calculate_ascii('SIVASATYANbalasundaram'))

# this calculates how many there are of different types of characters:
# lower case, special chars, etc.
# the function is later used to check the strength of an inputted password 
def calculate_case(string):
    lower = 0
    upper = 0
    number = 0
    special = 0
    
    for letter in string:
        if ord(letter) >= 97 and ord(letter) <= 122:
            lower += 1
        if ord(letter) >= 65 and ord(letter) <= 90:
            upper += 1
        if ord(letter) >= 48 and ord(letter) <= 57:
            number += 1
        if (ord(letter) >= 33 and ord(letter) <= 47) or (ord(letter) >= 58 and ord(letter) <= 64):
            special += 1
            
    return lower, upper, number, special

# cases = calculate_case('SIVASATYANbalasundaram')

# if cases[0] > 0 and cases[1] > 0 and cases[2] > 0 and cases[3] > 0:
#     print('This is a valid password')
# else:
#     print('This is an invalid password')

# print(f'There are {cases[0]} lower case characters.')
# print(f'There are {cases[1]} upper case characters.')
# print(f'There are {cases[2]} numbers.')
# print(f'There are {cases[3]} special characters.')

def caeser_cipher(letter):
    key = (ord(letter) - 65) + 2
    cipher = chr(ord('A') + key)
    return cipher

# print(caeser_cipher('B'))