# TraviAir - Siva

n = int(input('number of suitcases: '))
accepted = 0
rejected = 0
total = 0
fee = 0

for i in range(n):
  w = int(input('enter the weight: '))
  if w < 25:
    accepted += 1
    total += w
  elif w > 25 and w < 35:
    fee += (w - 25) * 5
    total += w
  elif w > 35 and w < 50:
    fee += (w - 35) * 7.50
    total += w
  elif w > 50 and w < 75:
    fee += (w - 50) * 10
    total += w
  elif w > 100:
    rejected += 1
    
print('total weight:', total)
print('total items:', n)
print('accepted items:', accepted)
print('rejected items:', rejected)
print('additional fees: £', fee, sep='')