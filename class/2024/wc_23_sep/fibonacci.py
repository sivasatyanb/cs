# generating the fibonacci sequence using recursion:
def fibonacci(n):
    
    if (n == 0):
        return 0
    elif (n == 1 or n == 2):
        return 1
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

# get user input and print function output
n = int(input('Enter a number of terms from the fibonacci sequence: '))
print(f'The fibonacci sequence for the first {n} terms are:', end = ' ')
for i in range(n):
    print(f'{fibonacci(i)}', end = ' ')