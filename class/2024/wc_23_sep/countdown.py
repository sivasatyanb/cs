# this function demonstrates a basic example of recursion:
def countdown(n):
    if n == 1:
        print('1' + '\n' + 'take-off!')
    else:
        print(n)
        countdown(n-1)
    
    # # alternative using iteration:
    # for i in range(n):
    #     print(n)
    #     n -= 1
    # print('take-off!')
        
n = int(input('Enter a number to count down from: '))
countdown(n)