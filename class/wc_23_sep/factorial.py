# calculating the factorial of a number,
# i.e. 4! = 4 * 3 * 2 * 1 = 24
# using recursion:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input('Enter a number: '))
print(f'{n} factorial is {factorial(n)}')

# # the cooler way:
# import math

# n = int(input('Enter a number: '))
# print(f'{n} factorial is {math.factorial(n)}')