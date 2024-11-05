def countdown(n):
    if n == 0:
        print('take-off!')
        return
    else:
        print(n)
        countdown(n-1)

# countdown(10)

import random

def cafe(chosen, options):
    if len(chosen) == 3:
        return
    else:
        if chosen != []:
            options.remove(chosen[-1])
        chosen.append(options[random.randint(0, len(options) - 1)])
        print(options,'\n', chosen)
        cafe(chosen, options)

cafe([], ['pizza', 'cake', 'burger', 'chips', 'veg'])