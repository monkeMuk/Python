from flask import Flask, render_template, redirect,url_for, request, session, flash

app = Flask(__name__)
# need secret key for session
app.secret_key = 'wooski'

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    
    if request.method == 'POST':
        user = request.form['formName']

        session['user'] = user 
        flash('Login successful')
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            flash('Already logged in!')
            return redirect(url_for('user'))
        
        return render_template('login.html')

@app.route('/user')
def user():
    if 'user' in session: 
        user = session['user']
        flash('You are logged in')
        return render_template('user.html', user=user)
    else:
        flash('You are not logged in')
        return redirect(url_for('login'))
    

@app.route('/logout')
def logout():
    if 'user' in session: 
        user = session['user']
        session.pop('user',None)
    flash(f'You have logged out, {user}', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)



