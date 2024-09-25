'''
Write an algorithm for an eager shopper who is keen to shop at the new
TraviMart online store which is opening. Before transactions take place the
user has to input the maximum amount of money they have to spend aka their
budget. After each transaction the program should prompt the user if they
want to purchase another item. The program should keep a running total of
Number of items purchased, total spent on all items and how much the user
has left to spend. The user should not be allowed to go over their maximum
budget the program should terminate when the user no longer wishes to
purchase anything else and should output total Number of items, total amount
spent and the total amount remaining.

The owner of TraviMart Da Good Looking One is concerned products such as
Cleaning Products such as Hand Sanitizer, Tissues, Bleach and Toilet Roll
are going to run out and tinned foods and he has placed a restriction of these
of 10 products of each variety Cleaning products and tinned food. If shoppers
go over 10 items of cleaning products they are required to pay an extra 30%
and over 20 products an extra 60%. No shopper is allowed any more than 25
units of cleaning products. Adapt your algorithm to work out a new total cost
'''
import random

budget = float(input('Please enter your budget in pounds: '))
expenditure = 0
items = 0
cleaning = 0
tinned = 0

while budget > 0:
    product = input('Would you like to buy toys, cleaning products, or tinned food?: ')
    price = round(random.uniform(0.5, 50.0), 2)
    
    if budget - price < 0:
        print('You do not have enough money to buy this item.')
        break
    
    if product == 'cleaning products':
        
        if cleaning > 25:
            print('You have already bought the maximum number of cleaning products.')
            items -= 1
            cleaning -= 1
            price = 0
        elif cleaning > 20:
            price *= 1.6
        elif cleaning > 10:
            price *= 1.3
        
        items += 1
        cleaning += 1
        budget -= price
        expenditure += price
    
    elif product == 'tinned food':
        
        if tinned > 25:
            print('You have already bought the maximum number of tinned food items.')
            items -= 1
            tinned -= 1
            price = 0
        elif tinned > 20:
            price *= 1.6
        elif tinned > 10:
            price *= 1.3
        
        items += 1
        tinned += 1
        budget -= price
        expenditure += price
    
    else:
        items += 1
        budget -= price
        expenditure += price
    
    round(budget, 2)
    round(expenditure, 2)
    
    if price != 0:
        print(f'The price of this item was: £{price}.')
    print(f'Your remaining budget is: £{budget}.')
    
    cont = input('Would you like to continue shopping?: ')
    
    if cont != 'yes':
        break

print('---------------------------')
print(f'You spent £{expenditure}.')
print(f'You bought {items} items.')
print(f'Your remaining budget is £{budget}.')
print('Hope you enjoyed your visit to TraviMart!')
        