import random

def calculateScore(dice1, dice2):
    
    if dice1 == dice2:
        dice3 = random.randint(1, 6)
        if dice1 + dice2 + dice3 > 15:
            return 12
    elif dice1 + dice2 > 8:
        return 10
    elif dice1 + dice2 > 4:
        return 4

player1 = calculateScore(random.randint(1, 6), random.randint(1, 6))
player2 = calculateScore(random.randint(1, 6), random.randint(1, 6))

if player1 > player2:
    print('Player 1 wins!')
elif player1 == player2:
    print('Draw!')
elif player1 < player2:
    print('Player 2 wins!')