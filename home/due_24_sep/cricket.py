import random

# initialise scores array and populate with random data - dimensions are 15x11
scores = [['' for j in range(15)] for i in range(11)]

for i in range(11):
    for j in range(15):
        runs = random.randint(1, 100)
        scores[i][j] = runs

maximum = 0
maximum_player = ''
i = 0

# iterate through the array and perform the relevant calculations
for player in scores:
    average = sum(player) / len(player)
    if average > maximum:
        maximum = sum(player) / len(player)
        maximum_player = i

    print(f'Player {i} scored {sum(player)} runs.')
    print(f'Their highest number of runs was {max(player)}.')
    print(f'Their lowest number of runs was {min(player)}.')
    print(f'Their average number of runs was {int(round(average, 0))}.')

    i += 1

# output the results
print(f'The player with the highest average runs was Player {maximum_player} with {int(round(maximum, 0))} runs!')