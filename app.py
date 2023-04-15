from flask import Flask, render_template, request, redirect, url_for, flash
from tables import *

app = Flask(__name__)
app.config['SECRET_KEY']  = 'dceicjewkjj1o3u98549efuo4'

CreateStudentsTable()
CreateSponsorsTable()

# SAMPLE INSERTIONS
InsertStudent('Essa','Zuberi','echu123','abc123','essa123@gmai.com')
InsertStudent('Laiba','Jamil','libbu123','abc123','laiba123@gmai.com')
InsertStudent('Hania','Zuberi','hania123','abc123','hania123@gmai.com')
InsertStudent('Ibrahim','Haider','ibrahim123','abc123','ibrahim123@gmai.com')

InsertSponsor('Abdullah','Ahmed','abdullah123','abc123','abdullah123@tcf.pk','TCF')
InsertSponsor('Zain','Ali','zain123','abc123','zain123@ibex.pk','ibex')


@app.route('/', methods=['GET', 'POST'])
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
            return render_template('testpage.html', first_name = sponsor[1])
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
        
        return render_template('testpage.html', first_name = first_name)
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


if __name__ == '__main__':
    app.run(debug=True)
