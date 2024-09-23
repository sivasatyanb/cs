# pushing/popping numbers from a stack
# it also calculates the total if stack becomes full

# note: numpy is importing because this program can also be
# (and previously was) implemented with this library
import numpy as np
import random

# initialise main varaibles
stack = [random.randint(1, 10), random.randint(1, 10)]
pointer = 1
inp1 = input('Please choose to add to the stack or remove from the stack: ')

# push onto the stack
if inp1 == 'push':
    n = int(input('Please enter a number to push onto the stack: '))
    stack[pointer] = n
    pointer += 1
    
    # calculate total of stack
    if len(stack) == 2:
        inp2 = input('This stack is full, would you like to add the numbers in it: ')
        if inp2 == 'yes':
            print(f'Total: {sum(stack)}')
        else:
            print('Stack:', stack)
    else:
        pass

# pop from the stack
elif inp1 == 'pop':
    if sum(stack) != 0:
        stack[pointer] = 0
        pointer -= 1
        print('Stack: ', stack)
        
    # error detection :)
    else:
        print('This stack is already empty')