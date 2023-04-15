import sqlite3

import os.path


def CreateStudentsTable():
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # db_path = os.path.join(BASE_DIR, "students.db")
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()

def CreateSponsorsTable():
    conn = sqlite3.connect('sponsors.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sponsors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            company TEXT NOT NULL
        )
    ''')
    conn.commit()

def InsertStudent(first_name: str, last_name: str, username: str, password: str, email: str):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO students (first_name, last_name, username, password, email)
        VALUES (?, ?, ?, ?, ?)
    ''', (first_name, last_name, username, password, email))
    conn.commit()


def InsertSponsor(first_name: str, last_name: str, username: str, password: str, email: str, company: str):
    conn = sqlite3.connect('sponsors.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO sponsors (first_name, last_name, username, password, email, company)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, username, password, email, company))
    conn.commit()

# CreateStudentsTable()
# CreateSponsorsTable()
# # SAMPLE INSERTIONS
# InsertStudent('Essa','Zuberi','echu123','abc123','essa123@gmai.com')
# InsertStudent('Laiba','Jamil','libbu123','abc123','laiba123@gmai.com')
# InsertStudent('Hania','Zuberi','hania123','abc123','hania123@gmai.com')
# InsertStudent('Ibrahim','Haider','ibrahim123','abc123','ibrahim123@gmai.com')

# InsertSponsor('Abdullah','Ahmed','abdullah123','abc123','abdullah123@tcf.pk','TCF')
# InsertSponsor('Zain','Ali','zain123','abc123','zain123@ibex.pk','ibex')
