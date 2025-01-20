import random

code = ''
multiplier = 1
total = 0

for i in range(7):
    n = random.randint(30, 39)
    code += str(n)

code = '1324562'

for letter in code:
    
    if multiplier % 2 == 1:
        total += int(letter) * 3
    else:
        total += int(letter) * 1
    
    multiplier += 1

multiplier = 10

while total > multiplier:
    multiplier += 10

cd = total - multiplier

code += str(cd)[-1]

print(code)