import random

# function to generate the classic mr travi's baby brother name problem
def generate_name(forename, surname):
    letters = []
    numbers = []
    name = ''
    
    for i in range(3):
        letter = chr(random.randint(97, 122))
        number = random.randint(1, 9)
        letters.append(letter)
        numbers.append(str(number))
        
    name += forename[-3:] 
    for letter in letters:
        name += letter
    name += surname[-3:]
    for number in numbers:
        name += number
    
    return name

# get inputs and pass into function
forename = input('Enter your first name: ')
surname = input('Enter your last name: ')
names = []

for i in range(3):
    name = generate_name(forename, surname)
    names.append(name)

# output the generated baby names
print('The chosen names were:')
for name in names:
    print(name)