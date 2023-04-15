import sqlite3

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

