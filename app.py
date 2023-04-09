from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         # Handle login request
#         username = request.form['username']
#         password = request.form['password']
#         # Check if the username and password are correct
#         if username == 'myusername' and password == 'mypassword':
#             return 'Login successful!'
#         else:
#             return 'Invalid username or password'
#     else:
#         # Render the login page
#         return render_template('login.html')

# @app.route('/signup')
# def signup():
#     # Render the signup page
#     return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)

