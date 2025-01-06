import sqlite3
from player import Player

connection = sqlite3.connect('class/wc_14_oct/players.db')

cursor = connection.cursor()

cursor.execute('CREATE TABLE players (first text, last text, rating integer)')

def addPlayer(p):
    with connection:
        cursor.execute('INSERT INTO players VALUES (:first, :last, :rating)', {'first': p.first, 'last': p.last, 'rating': p.rating})

def removePlayer(p):
    with connection:
        cursor.execute('DELETE FROM players WHERE first = :first AND last = :last', {'first': p.first, 'last': p.last})

def selectAllPlayers():
    cursor.execute('SELECT * FROM players WHERE 1=1')
    return cursor.fetchall()

def updatePlayer(p, rating: int):
    cursor.execute('UPDATE players SET rating = :rating WHERE first = :first and last = :last', {'first': p.first, 'last': p.last, 'rating': rating})

p1 = Player('Magnus', 'Carlsen', 2800)
p2 = Player('Anish', 'Giri', 2700)

addPlayer(p1)
addPlayer(p2)
updatePlayer(p2, 2750)

players = selectAllPlayers()

print(*players)