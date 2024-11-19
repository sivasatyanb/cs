import pandas as pd
import sqlite3

def initialiseDatabase():
    entries_df = pd.read_csv('class/wc_18_nov/Entries.csv')
    pupils_df = pd.read_csv('class/wc_18_nov/Pupils.csv')
    subjects_df = pd.read_csv('class/wc_18_nov/Subjects.csv')

    conn = sqlite3.connect('class/wc_18_nov/database.db')
    cursor = conn.cursor()

    entries_df.to_sql('Entries', conn, if_exists='replace', index=False)
    pupils_df.to_sql('Pupils', conn, if_exists='replace', index=False)
    subjects_df.to_sql('Subjects', conn, if_exists='replace', index=False)

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    conn.close()

def main():
    initialiseDatabase()

if __name__ == '__main__':
    main()