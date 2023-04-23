from flask import Flask, render_template,session, request, redirect, url_for, flash
from flask_socketio import SocketIO, send
import math
from tables import *

app = Flask(__name__)
app.config['SECRET_KEY']  = 'dceicjewkjj1o3u98549efuo4'
socketio = SocketIO(app, cors_allowed_origins="*")


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

        admin_conn = sqlite3.connect('atiya-e-ilm.db')
        admin_cursor = admin_conn.cursor()
        admin_cursor.execute('SELECT * FROM admins WHERE username=? AND password=?', (username, password))
        admin_conn.commit()
        admin = admin_cursor.fetchone()

        # print(f"student: {student}, sponsor: {sponsor}")
        if student:
            return redirect(url_for('student_homepage', first_name=student[1], username=student[3]))
        elif sponsor:
            return redirect(url_for('sponsor_homepage'), )
        elif admin:
            return redirect(url_for('admin'))
        else:
            flash('User doesnt exist/Incorrect Username or Password. Try Again!', category='error')
            return render_template('home.html')
    else:
        return render_template('home.html')
    

# @app.route("/message/<name>/<username>", methods=['GET', "POST"])
# def message(name, username):
#     student_conn = sqlite3.connect('atiya-e-ilm.db')
#     student_cursor = student_conn.cursor()
#     student_cursor.execute('SELECT * FROM students')
#     students = student_cursor.fetchall()
#     student_conn.close()
#     print(students)
#     return render_template("message.html", first_name=name.split()[0], username=username, students=students)


# @socketio.on("message")
# def sendMessage(message):
#     name = message["name"]
#     text = message["text"]
#     send(f"{name}: {text}", broadcast=True)



@app.route('/admin', methods=['GET', 'POST'])
def admin():
    conn = sqlite3.connect('atiya-e-ilm.db')
    c = conn.cursor()
    c.execute("SELECT * FROM applications")
    applications = [dict(name=row[0], email=row[1], phone=row[2], address=row[3], major=row[4]) for row in c.fetchall()]
    conn.close()

    conn = sqlite3.connect('atiya-e-ilm.db')
    c = conn.cursor()
    c.execute("SELECT * FROM sponsors")
    donors = [dict(name=row[0], email=row[1], phone=row[2], address=row[3], amount=row[4]) for row in c.fetchall()]
    conn.close()

    return render_template('admin.html', applications=applications, donors=donors)

# define route for sponsor signup
@app.route('/signup/sponsor', methods=['GET', 'POST'])
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
        return redirect(url_for('sponsor_homepage' ))
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
        return redirect(url_for('student_homepage', username=username, first_name=first_name))
    else:
        return render_template('student_signup.html')

@app.route('/student_homepage/<username>/<first_name>', methods=['GET', 'POST'])
def student_homepage(username, first_name):
    if request.method == 'POST':
        return redirect(url_for('start_application', username=username, first_name=first_name))
    
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
    return render_template('student_homepage.html', first_name=username, data=data)


@app.route('/donate/<student_id>' , methods=['GET', 'POST'])
def donation(student_id):
    # retrieve the row data using the student_id
    if request.method == 'POST':
        amount = request.form['amount']
        conn = sqlite3.connect('atiya-e-ilm.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE applications SET amount_collected = amount_collected + ? WHERE student_id = ?", (amount, student_id))
        conn.commit()
        conn.close()
        return render_template('testpage.html')


    #print(student_id)
    return render_template('donation.html')


# @app.route('/sponsor_homepage',  methods=['GET', 'POST'])
# def sponsor_homepage():
#     conn = sqlite3.connect('atiya-e-ilm.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         SELECT first_name, last_name, application_name, description, amount_collected, amount_needed 
#         FROM students 
#         INNER JOIN applications 
#         ON students.id = applications.student_id;
#         ''')
#     data = cursor.fetchall()
#     # print(data)
#     conn.close()

#     return render_template('sponsor_homepage.html', data=data)\
@app.route('/sponsor_homepage',  methods=['GET', 'POST'])
def sponsor_homepage():
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

    # Pagination
    per_page = 10
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_data = data[start:end]
    total_pages = math.ceil(len(data) / per_page)

    return render_template('sponsor_homepage.html', data=paginated_data, page=page, total_pages=total_pages)


# when student clicks start an application button
@app.route('/start_application/<username>/<first_name>', methods=['GET', 'POST'])
def start_application(username, first_name):
    if request.method == 'POST':
        title = request.form['fundraiser_title']
        description = request.form['description']
        amount_needed = request.form['amount_needed']

        conn = sqlite3.connect('atiya-e-ilm.db')
        InsertApplication(conn, username, title, description, amount_needed)
        conn.close()
        return render_template('application_uploaded.html', first_name = first_name)
    return render_template('start_application.html', username=username, first_name=first_name)

if __name__ == '__main__':
    app.run(debug=True)
