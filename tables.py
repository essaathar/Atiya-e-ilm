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

def create_student_funding_table():
    conn = sqlite3.connect('student_funding.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_funding (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            amount_collected INTEGER NOT NULL,
            amount_needed INTEGER NOT NULL,
            FOREIGN KEY(student_id) REFERENCES students(id)
        )
    ''')

    conn.commit()
    conn.close()
def update_student_funds(student_id: int, amount_collected: int, amount_needed: int):
    conn = sqlite3.connect('student_funding.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT OR REPLACE INTO student_funding (student_id, amount_collected, amount_needed)
        VALUES (?, ?, ?)
    ''', (student_id, amount_collected, amount_needed))

    conn.commit()
    conn.close()
# def CreateStudentFundingTable():
#     conn = sqlite3.connect('student_funding.db')
#     cursor = conn.cursor()

#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS student_funding (
#             id INTEGER PRIMARY KEY,
#             first_name TEXT NOT NULL,
#             last_name TEXT NOT NULL,
#             amount_collected INTEGER,
#             amount_needed INTEGER,
#             FOREIGN KEY(id) REFERENCES students(id)
#         )
#     ''')
#     conn.commit()


# def UpdateStudentFunding(student_id: int, amount_collected: int, amount_needed: int):
#     conn = sqlite3.connect('student_funding.db')
#     cursor = conn.cursor()

#     cursor.execute('ATTACH DATABASE "students.db" AS students_db')
#     cursor.execute('''
#     INSERT INTO student_funding (id, first_name, last_name, amount_collected, amount_needed)
#     SELECT students.id, students.first_name, students.last_name, ?, ?
#     FROM students
#     WHERE students.id=?
# ''', (amount_collected, amount_needed, student_id))
#     conn.commit()

# def CreateStudentFundingTable():
#     conn = sqlite3.connect('student_funding.db')
#     cursor = conn.cursor()

#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS student_funding (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             student_id INTEGER NOT NULL,
#             first_name TEXT NOT NULL,
#             last_name TEXT NOT NULL,
#             amount_collected INTEGER NOT NULL,
#             amount_needed INTEGER NOT NULL,
#             FOREIGN KEY(student_id) REFERENCES students(id)
#         )
#     ''')
#     conn.commit()


# def InsertStudentFunding(student_id: int, amount_collected: int, amount_needed: int):
#     conn = sqlite3.connect('student_funding.db')
#     cursor = conn.cursor()

#     cursor.execute('SELECT first_name, last_name FROM students WHERE id = ?', (student_id,))
#     row = cursor.fetchone() 
#     first_name, last_name = row[0], row[1]

#     cursor.execute('''
#         INSERT INTO student_funding (student_id, first_name, last_name, amount_collected, amount_needed)
#         VALUES (?, ?, ?, ?, ?)
#     ''', (student_id, first_name, last_name, amount_collected, amount_needed))
#     conn.commit()

# def CreateStudentFundingTable():
#     conn = sqlite3.connect('students.db')
#     cursor = conn.cursor()

#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS student_funding (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             student_id INTEGER NOT NULL,
#             amount_collected INTEGER NOT NULL,
#             amount_needed INTEGER NOT NULL,
#             FOREIGN KEY(student_id) REFERENCES students(id)
#         )
#     ''')
#     conn.commit()


# def InsertStudentFunding(student_id: int, amount_collected: int, amount_needed: int):
#     conn = sqlite3.connect('students.db')
#     cursor = conn.cursor()

#     cursor.execute('SELECT first_name, last_name FROM students WHERE id = ?', (student_id,))
#     row = cursor.fetchone() 
#     first_name, last_name = row[0], row[1]

#     cursor.execute('''
#         INSERT INTO student_funding (student_id, first_name, last_name, amount_collected, amount_needed)
#         VALUES (?, ?, ?, ?, ?)
#     ''', (student_id, first_name, last_name, amount_collected, amount_needed))
#     conn.commit()

