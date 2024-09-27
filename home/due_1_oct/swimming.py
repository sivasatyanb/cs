scores = []

total = 0

# store all of inputted scores in an array
for i in range(5):
    score = int(input('Enter a score from 1 to 10: '))
    scores.append(score)

maximum = False
minimum = False

# discard the highest and lowest score and find team total
for score in scores:
    if score == max(scores) and not maximum:
        maximum = True
    elif score == min(scores) and not minimum:
        minimum = True
    else:
        total += score

# output the team's total score
print('The total team score was:', total)