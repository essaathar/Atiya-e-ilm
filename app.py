from flask import Flask, render_template,session, request, redirect, url_for, flash
from tables import *

app = Flask(__name__)
app.config['SECRET_KEY']  = 'dceicjewkjj1o3u98549efuo4'

CreateSponsorsTable()
CreateStudentsTable()

# SAMPLE INSERTIONS
InsertStudent('Essa','Zuberi','echu123','abc123','essa123@gmai.com')
InsertStudent('Laiba','Jamil','libbu123','abc123','laiba123@gmai.com')
InsertStudent('Hania','Zuberi','hania123','abc123','hania123@gmai.com')
InsertStudent('Ibrahim','Haider','ibrahim123','abc123','ibrahim123@gmai.com')

InsertSponsor('Abdullah','Ahmed','abdullah123','abc123','abdullah123@tcf.pk','TCF')
InsertSponsor('Zain','Ali','zain123','abc123','zain123@ibex.pk','ibex')

create_student_funding_table()
# Update funding for Essa Zuberi
update_student_funds(1, 500, 1000)

# Update funding for Laiba Jamil
update_student_funds(2, 1000, 2000)

# Update funding for Hania Zuberi
update_student_funds(3, 750, 1500)

# Update funding for Ibrahim Haider
update_student_funds(4, 2000, 3000)

@app.route('/', methods=['GET', 'POST'])
# def home():
#     # Connect to the students database
#     student_funding_conn = sqlite3.connect('students.db')
#     student_funding_cursor = student_funding_conn.cursor()

#     # Print the table names to verify that student_funding table exists
#     student_funding_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#     print(student_funding_cursor.fetchall())

#     # Select all rows from the student_funding table
#     student_funding_cursor.execute('SELECT * FROM student_funding')
#     student_funding_rows = student_funding_cursor.fetchall()

#     # Close the connection
#     student_funding_conn.close()
#     return render_template('home.html', student_funding_rows=student_funding_rows)

def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        student_conn = sqlite3.connect('students.db')
        student_cursor = student_conn.cursor()
        student_cursor.execute('SELECT * FROM students WHERE username=? AND password=?', (username, password))
        student_conn.commit()
        student = student_cursor.fetchone()

        sponsor_conn = sqlite3.connect('sponsors.db')
        sponsor_cursor = sponsor_conn.cursor()
        sponsor_cursor.execute('SELECT * FROM sponsors WHERE username=? AND password=?', (username, password))
        sponsor_conn.commit()
        sponsor = sponsor_cursor.fetchone()
        print(f"student: {student}, sponsor: {sponsor}")
        if student:
             return render_template('student_homepage.html', first_name = student[1])
        elif sponsor:
            return render_template('sponsor_homepage.html')
            # student_funding_conn = sqlite3.connect('student_funding.db')
            # student_funding_cursor = student_funding_conn.cursor()
            # student_funding_cursor.execute('SELECT * FROM student_funding')
            # student_funding = student_funding_cursor.fetchall()
        else:
            return render_template('home.html')
    else:
        return render_template('home.html')




# define route for sponsor signup
@app.route('/signup/sponsor')
def sponsor_signup():
    if request.method == 'POST':
        # get the form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        company = request.form['company']

        InsertSponsor(first_name=first_name, last_name=last_name, 
                      username=username, password=password, email=email, company=company)
        
        return render_template('sponsor_homepage.html', first_name = first_name)
    else:
        return render_template('sponsor_signup.html')


@app.route('/signup/student', methods=['GET', 'POST'])
def student_signup():
    if request.method == 'POST':
        # get the form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        InsertStudent(first_name=first_name, last_name=last_name, username=username, password=password, email=email)

        return render_template('student_homepage.html', first_name = first_name)
    else:
        return render_template('student_signup.html')

@app.route('/account/<username>')
def account(username):
    return render_template('student_homepage.html', first_name=username)

@app.route('/donation')
def donation():
    return render_template('donation.html')

@app.route('/process_donation', methods=['POST'])
def process_donation():
    # Retrieve form data
    card_number = request.form['card_number']
    cardholder_name = request.form['cardholder_name']
    expiry_date = request.form['expiry_date']
    security_code = request.form['security_code']
    amount = request.form['amount']
    
       # Print the form data
    print(f"Card Number: {card_number}")
    print(f"Cardholder Name: {cardholder_name}")
    print(f"Expiry Date: {expiry_date}")
    print(f"Security Code: {security_code}")
    print(f"Amount: {amount}")

@app.route('/sponsor_homepage')
def sponsor_homepage():

    return render_template('sponsor_homepage.html')

if __name__ == '__main__':
    app.run(debug=True)
