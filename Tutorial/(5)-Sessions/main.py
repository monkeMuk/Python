from flask import Flask, render_template, redirect,url_for, request, session

app = Flask(__name__)
# need secret key for session
app.secret_key = 'wooski'

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['POST','GET'])
def login():
    
    if request.method == 'POST':
        user = request.form['formName']
        session['user'] = user 
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        
        return render_template('login.html')

@app.route('/user')
def user():
    if 'user' in session: 
        user = session['user']
        return f'<h1>{user}</h1>'
    else:
        return redirect(url_for('login'))
    

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)



'''
from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'wooski'

# Route for login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        entered_username = request.form['formName']
        session['logged_in_user'] = entered_username  # Storing the entered username in the session
        return redirect(url_for('user_dashboard'))
    else:
        return render_template('login.html')

# Route for displaying user information
@app.route('/user-dashboard')
def user_dashboard():
    # Checking if 'logged_in_user' key is in the session
    if 'logged_in_user' in session:
        username = session['logged_in_user']  # Retrieving the entered username from the session
        return f'<h1>Hello, {username}! Welcome to your dashboard.</h1>'
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

'''