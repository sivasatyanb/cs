import random

# function to generate a hand of cards
def generate_hand():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    hand = []
    random.shuffle(cards)
    for i in range(10):
        hand.append(cards[i])
    
    return hand

# calling function to get hand of cards
p1_hand = generate_hand()
p2_hand = generate_hand()

p1_total = 0
p2_total = 0

# iterating through cards to calculate total
for i in range(10):
    p1_card = p1_hand[i]
    p2_card = p2_hand[i]
    
    if not p1_card.isnumeric():
        if p1_card == 'J':
            p1_card = '11'
        if p1_card == 'Q':
            p1_card = '12'
        if p1_card == 'K':
            p1_card = '13'
        if p1_card == 'A':
            p1_card = '1'
    
    if not p2_card.isnumeric():
        if p2_card == 'J':
            p2_card = '11'
        if p2_card == 'Q':
            p2_card = '12'
        if p2_card == 'K':
            p2_card = '13'
        if p2_card == 'A':
            p2_card = '1'
    
    p1_total += int(p1_card)
    p2_total += int(p2_card)

# checks to see whih player is the winner and outputs results
if p1_total > p2_total:
    print('Player 1 Wins!')
elif p2_total > p1_total:
    print('Player 2 Wins!')
elif p1_total == p2_total:
    print('Draw!')

print('Player 1 score:', p1_total)
print('Player 2 score:', p2_total)