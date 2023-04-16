from flask import Flask, render_template,session, request, redirect, url_for, flash
from tables import *

app = Flask(__name__)
app.config['SECRET_KEY']  = 'dceicjewkjj1o3u98549efuo4'



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        student_conn = sqlite3.connect('atiya-e-ilm.db')
        student_cursor = student_conn.cursor()
        student_cursor.execute('SELECT * FROM students WHERE username=? AND password=?', (username, password))
        student_conn.commit()
        student = student_cursor.fetchone()

        sponsor_conn = sqlite3.connect('atiya-e-ilm.db')
        sponsor_cursor = sponsor_conn.cursor()
        sponsor_cursor.execute('SELECT * FROM sponsors WHERE username=? AND password=?', (username, password))
        sponsor_conn.commit()
        sponsor = sponsor_cursor.fetchone()
        # print(f"student: {student}, sponsor: {sponsor}")
        if student:
             return render_template('student_homepage.html', first_name = student[1])
        elif sponsor:
            return redirect(url_for('sponsor_homepage'))
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

        conn = sqlite3.connect('atiya-e-ilm.db')
        InsertSponsor(conn, first_name=first_name, last_name=last_name, 
                      username=username, password=password, email=email, company=company)
        conn.close()
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

        conn = sqlite3.connect('atiya-e-ilm.db')
        InsertStudent(conn, first_name=first_name, last_name=last_name, username=username, 
                      password=password, email=email)
        conn.close()
        return render_template('student_homepage.html', first_name = first_name)
    else:
        return render_template('student_signup.html')

@app.route('/account/<username>')
def account(username):
    return render_template('student_homepage.html', first_name=username)

@app.route('/donation',  methods=['GET', 'POST'])
def donation():
    return render_template('donation.html')

# @app.route('/process_donation', methods=['POST'])
# def process_donation():
#     # Retrieve form data
#     card_number = request.form['card_number']
#     cardholder_name = request.form['cardholder_name']
#     expiry_date = request.form['expiry_date']
#     security_code = request.form['security_code']
#     amount = request.form['amount']
    
#        # Print the form data
#     print(f"Card Number: {card_number}")
#     print(f"Cardholder Name: {cardholder_name}")
#     print(f"Expiry Date: {expiry_date}")
#     print(f"Security Code: {security_code}")
#     print(f"Amount: {amount}")

@app.route('/sponsor_homepage',  methods=['GET', 'POST'])
def sponsor_homepage():
    if request.method == 'POST':
        return redirect(url_for('donation'))
    conn = sqlite3.connect('atiya-e-ilm.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT first_name, last_name, application_name, description, amount_collected, amount_needed 
        FROM students 
        INNER JOIN applications 
        ON students.id = applications.student_id;
        ''')
    data = cursor.fetchall()
    # print(data)
    conn.close()
    return render_template('sponsor_homepage.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
