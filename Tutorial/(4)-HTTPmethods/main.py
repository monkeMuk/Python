from flask import Flask, render_template, redirect,url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['POST','GET'])
def login():
    
    if request.method == 'POST':
        user = request.form['formName']
        age = request.form['formAge']
        return redirect(url_for('user',usr=user, ae=age))
        #url_for('route',arguments)

    return render_template('login.html')

@app.route('/<usr>/<ae>')
def user(usr,ae):
    return f'<h1>{usr}</h1> <br> <h1>{ae}</h1>'
    

if __name__ == '__main__':
    app.run(debug=True)