import sqlite3 as lite
db="PupilDatav2.db"
def createTable():
    con = lite.connect(db)  ## connects to the db
    cur = con.cursor() ## sets up positions
    cur.execute("DROP TABLE IF EXISTS ArrayDaLads")
    cur.execute('''CREATE TABLE "ArrayDaLads" (
    "PupilId" TEXT PRIMARY KEY UNIQUE,
    "Forename" TEXT NOT NULL,
    "Surname" TEXT NOT NULL,
    "RegGroup" TEXT NOT NULL,
    "Group" TEXT NOT NULL,
     "DOB" TEXT NOT NULL,
    "Hose" TEXT NOT NULL,
    "Autumn" INTERGER NOT NULL,
    "Spring" INTERGER NOT NULL,
    "UCAS" INTERGER NOT NULL,
    "BehaviourPoints" INTERGER NOT NULL,
     "AchievementPoints" INTERGER NOT NULL
   );''')
    con.commit()

createTable()