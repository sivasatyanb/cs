import random

code = ''
multiplier = 11
total = 0

for i in range(10):
    n = random.randint(30, 39)
    code += str(n)

code = '0241034812'

for letter in code:
    total += (multiplier * int(letter))
    multiplier -= 1

cd = 11- (total % 11)

if cd == 10:
    code += 'X'
else:
    code += str(cd)

print(f'ISBN: {code}')