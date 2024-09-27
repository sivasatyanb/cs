import random

arrayClassRecords = []

for i in range(10):
    student = []
    for j in range(3):
        n = random.randint(1, 100)
        student.append(n)
    arrayClassRecords.append(student)
    
for student in arrayClassRecords:
    print(f'Highest mark: {max(student)}')
    print(f'Lowest mark: {min(student)}')
    print(f'Average mark: {sum(student) / len(student)}')