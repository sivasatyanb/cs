import random

# initialise empty array
numbers = ['' for i in range(100)]

# randomly populate half of the numbers array
for i in range(100):
    n = random.randint(0, 3)
    
    if n == 0:
        pass
    elif n == 1:
        numbers[i] = 'A'
    elif n == 2:
        numbers[i] = 'B'
    elif n == 3:
        numbers[i] = 'C'

random.shuffle(numbers)

# print(numbers)

# recieve input and store in array (if place isn't taken)
a = int(input('Please enter a number: '))

if numbers[a] == '':
    numbers[a] = 'A'
elif numbers[a] != '':
    print('This place is taken')


# # Extension:

# empty = False
# a = 0
# b = 0
# c = 0

# # checks whether the array is full
# for number in numbers:
#     if number == '':
#         empty = True
#         break
#     elif number == 'A':
#         a += 1
#     elif number == 'B':
#         b += 1
#     elif number == 'C':
#         c += 1

# # calculates and outputs winner
# if not empty:
#     maximum = a
#     winner = 'A'


#     if b > maximum:
#         maximum = b
#         winner = 'B'

#     if c > maximum:
#         maximum = c
#         winner = 'C'

#     print(winner, 'won with', maximum, 'points!')
