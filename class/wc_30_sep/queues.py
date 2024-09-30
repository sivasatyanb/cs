# linear and circular queues:

from queue import Queue

q = Queue(maxsize=3)

# init head and tail
head = 0
tail = 0

# linear queues:

print('Linear Queues:')

# enqueue
for i in range(q.maxsize):
    q.put(chr(i + 65))
    tail += 1
    print(q.queue)
    if q.full():
        print('Queue is full')
        break
    
# dequeue
print('Dequeued items:')

print(q.get())
# >>> 'A'
head += 1
print(q.get())
# >>> 'B'
head += 1

# circular queues:

print('Circular Queues:')

for i in range(q.maxsize):
    q.put(chr(i + 65))
    tail = (tail + 1) % q.maxsize
    print(q.queue)
    if q.full():
        print('Queue is full')
        break
