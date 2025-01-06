# # Program (i):
# # Computer generates a random number and user tries to guess it in 10 tries.

# import random

# # initialise number of attempts and generate random number
# attempts = 10
# answer = random.randint(1, 100)

# # iteration until there are enough guesses
# while attempts > 0:
#     n = int(input('Please guess a number from 1-100: '))
    
#     # selection to give hints to user
#     if n == answer:
#         print('Correct, you win!')
#         break
#     elif n > answer:
#         print('Too high, try again!')
#     elif n < answer:
#         print('Too low, try again!')
    
#     # user loses an attempt after every guess
#     attempts -= 1

# # if the user has run out of attempts
# if attempts == 0:
#     print('You\'ve run out of guesses!')
#     print(f'The answer was {answer}.')

# Program (ii):
# User inputs a number and computer tries to guess it in as few attempts as possible
# (this is also the binary research algorithm)

# get initial inputs and initialise required variables
n = int(input('Please enter a number for the computer to guess:'))
upper_bound = 100
lower_bound = 0
attempts = 0
error = False

# check that there is a valid user input
if not (n >= 0 and n <= 100):
    print('This input is invalid. Try again')
    error = True

if not error:
    # while the computer hasn't guessed the number
    while True:
        
        # guess is the midpoint of the upper and lower bound
        guess = (upper_bound + lower_bound) // 2
        attempts += 1
        
        # output the computer's guess
        print(f'The computer guessed the number {guess}')
        
        # selection to adjust upper and lower bounds
        if guess == n:
            print(f'The computer guessed the number in {attempts} attempts!')
            break
        elif guess > n:
            upper_bound = guess
        elif guess < n:
            lower_bound = guess
