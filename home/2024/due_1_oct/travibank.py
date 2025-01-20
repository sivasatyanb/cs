'''
TraviBank has just installed an ATM machine at its local branch and
has asked you to write an algorithm which to be used to access users
accounts. The program should allow the user 3 attempts to enter the
correct number. The program needs to be able to validate that the PIN
number entered is a 4 digit number entered. The program should tell
the user each time if the attempt is successful or not. The user should
be given the option of either re-entering the number of withdrawing
their card if the attempt is unsuccessful. If after 3 attempts the program
should output then the attempt was unsuccessful and no further
attempts are permitted.
'''
# part 1:
import random

pin = random.randint(1000, 9999)
attempts = 3

while attempts > 0:
    attempt = int(input('Please enter your pin: '))
    attempts -= 1
    
    if len(str(attempt)) != 4:
        print('This pin is not 4 digits.')
        print(f'You have {attempts} remaining.')
    elif attempt == pin:
        print('Transaction successful.')
        break
    elif attempt != pin:
        print('This pin is incorrect.')
        print(f'You have {attempts} remaining.')

if attempts == 0:
    print('You have ran out of attempts.' + '\n' + 'Transaction unsuccessful.')
    
# part 2:
if attempt == pin:
    options = [
        'View Balance',
        'Order Statement',
        'Withdraw Cash',
        'Exit ATM'
    ]
    
    option = options[random.randint(0, 3)]
    
    print(f'You have chosen to: {option}.')
    
    if option == options[2]:
        amount = int(input('How much money would you like to withdraw?: '))
        if amount > 200:
            print('You have exceeded the daily withdrawal amount')