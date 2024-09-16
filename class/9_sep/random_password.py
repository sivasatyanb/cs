import random

def check_password(password):
    strength = 'weak'
    
    upper = 0
    number = 0
    special = 0
    
    for letter in password:
        if ord(letter) >= 65 and ord(letter) <= 90:
            upper += 1
        if ord(letter) >= 48 and ord(letter) <= 57:
            number += 1
        if (ord(letter) >= 33 and ord(letter) <= 47) or (ord(letter) >= 58 and ord(letter) <= 64):
            special += 1
    
    if upper >= 2:
        strength = 'medium'
        if number >= 2:
            strength = 'strong'
            if special >= 2:
                strength = 'impenetrable'
    
    return strength

array = []

length = random.randint(20, 20)

for i in range(length):
    num = random.randint(33, 126)
    array.append(num)

password = ''
for n in array:
    n = int(n)
    password += chr(n) 

strength = check_password(password)

with open('data.txt', 'a') as f:
    string = password + ', ' + strength
    f.write(string + '\n')
    f.close()

print(password)
print('Your password is', strength)