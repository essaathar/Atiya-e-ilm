import sqlite3

def CreateStudentsTable(conn):
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


def CreateSponsorsTable(conn):
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


def InsertStudent(conn, first_name: str, last_name: str, username: str, password: str, email: str):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO students (first_name, last_name, username, password, email)
        VALUES (?, ?, ?, ?, ?)
    ''', (first_name, last_name, username, password, email))
    conn.commit()


def InsertSponsor(conn, first_name: str, last_name: str, username: str, password: str, email: str, company: str):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO sponsors (first_name, last_name, username, password, email, company)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, username, password, email, company))
    conn.commit()


def create_student_funding_table(conn):
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            application_name TEXT NOT NULL,
            description TEXT NOT NULL,
            amount_collected INTEGER NOT NULL,
            amount_needed INTEGER NOT NULL,
            FOREIGN KEY(student_id) REFERENCES students(id)
        )
    ''')

    conn.commit()


def InsertApplication(conn, student_id: str, application_name: str, description: str, amount_needed: int, amount_collected: int):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO applications (student_id, application_name, description, amount_collected, amount_needed)
        VALUES (?, ?, ?, ?, ?)
        ''', (student_id, application_name, description, amount_collected, amount_needed))
    conn.commit()




'''UNCOMMENT THE BELOW CODE BEFORE RUNNING THE PROJECT!'''

conn = sqlite3.connect('atiya-e-ilm.db')

CreateSponsorsTable(conn)
CreateStudentsTable(conn)
create_student_funding_table(conn)

# SAMPLE INSERTIONS
InsertStudent(conn, 'Essa','Zuberi','echu123','abc123','essa123@gmai.com')
InsertStudent(conn, 'Laiba','Jamil','libbu123','abc123','laiba123@gmai.com')
InsertStudent(conn, 'Hania','Zuberi','hania123','abc123','hania123@gmai.com')
InsertStudent(conn, 'Ibrahim','Haider','ibrahim123','abc123','ibrahim123@gmai.com')

InsertSponsor(conn, 'Abdullah','Ahmed','abdullah123','abc123','abdullah123@tcf.pk','TCF')
InsertSponsor(conn, 'Zain','Ali','zain123','abc123','zain123@ibex.pk','ibex')



# Update funding for Essa Zuberi
InsertApplication(conn, 1, 'Harvard Program Funds', 'I got into Harvard program. Really need the money.', 500, 1000)

# Update funding for Laiba Jamil
InsertApplication(conn, 2, "UCBP Funding", "I got into UCBerkley, really need the funding. Once in a life time opportunity.", 1000, 2000)

# Update funding for Hania Zuberi
InsertApplication(conn, 3, "Princeton program funds", "I got selected for Princeton Summer Program. I've done immense hardwork. Please help.", 750, 1500)

# Update funding for Ibrahim Haider
InsertApplication(conn, 4, "Brown University ST Program 2023", "Got into Brown Uni's summer tech program. Please really need the funds.", 2000, 3000)

conn.close()
