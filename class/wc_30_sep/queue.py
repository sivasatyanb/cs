import queue

q = queue.Queue(maxsize=3)

# linear queues:

head = 0
tail = 0

print(q.qsize()) 

q.put('a')
tail += 1
q.put('b')
tail += 1
q.put('c')
tail += 1

print('Full: ', q.full()) 

print(q.get())
head += 1
print(q.get())
head += 1
print(q.get())
head += 1

print('Empty: ', q.empty())