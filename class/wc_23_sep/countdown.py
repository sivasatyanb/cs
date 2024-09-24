# this function demonstrates a basic example of recursion:
def countdown(n):
    if n == 0:
        print('0' + '\n' + 'take-off!')
    else:
        print(n)
        countdown(n-1)
        
n = int(input('Enter a number to count down from: '))
countdown(n)