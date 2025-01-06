import sqlite3

connection = sqlite3.connect('cs/class/wc_21_oct/students.db')

cursor = connection.cursor()

# average mark
def averageMark():
    with connection:
        cursor.execute('''
                       SELECT Forename, Surname, AVG(Autumn + Spring + UCAS) AS Average
                       FROM ArrayDaLads
                       WHERE NOT Forename = 'Forename'
                       GROUP BY Surname;
                       ''')
        students = cursor.fetchall()
    return students

# achievement points - behaviour points
def calculateAttitude():
    with connection:
        # cursor.execute('''
        #                ALTER TABLE ArrayDaLads 
        #                ADD Attitude int;
        #                ''')
        # cursor.execute('''
        #                 UPDATE ArrayDaLads 
        #                 SET Attitude = Achievement - Behaviour;
        #                ''')
        cursor.execute('''
                       SELECT Forename, Surname, Attitude
                       FROM ArrayDaLads
                       WHERE NOT Forename = 'Forename';
                       ''')
        students = cursor.fetchall()
    return students

# order students by date of birth
def orderByAge():
    with connection:
        cursor.execute('''
                       SELECT Forename, Surname, DOB
                       FROM ArrayDaLads
                       WHERE (DOB BETWEEN '2006-09-01' AND '2007-01-01') AND NOT Forename = 'Forename'
                       ORDER BY DOB ASC;
                       ''')
        students = cursor.fetchall()
    return students

# calculate the age of all students using julianday
def calculateAge():
    with connection:
        cursor.execute(
            '''
            SELECT Forename, Surname, CAST((julianday('now') - julianday(DOB)) / 365.25 AS INTEGER) AS Age
            FROM ArrayDaLads
            WHERE NOT Forename = 'Forename';
            '''
        )
        students = cursor.fetchall()
    return students

students = calculateAge()

for student in students:
    print(*student)