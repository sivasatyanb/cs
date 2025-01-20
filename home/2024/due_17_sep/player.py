import random

green = 0
red = 0

# initialise empty array with dimensions 2x20
player = [[0 for row in range(2)] for column in range(20)]

# populate the array with random values
for i in range(20):
    player[i][0] = random.randint(1, 2)
    player[i][1] = random.randint(1, 50)

# print(player)

# calculate total scores for each team
for i in range(20):
    if player[i][0] == 1:
        green += player[i][1]
    elif player[i][0] == 2:
        red += player[i][1]
        
# check the winner and output results
if red > green:
    print('Red team wins!')
elif green > red:
    print('Green team wins!')
elif green == red:
    print('Draw!')

print('Red team score:', red)
print('Green team score:', green)