from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def homeFunction():
    return 'Hello World'

@app.route('/2')
def testFunction2():
    return redirect(url_for('goToSecondPage'))

@app.route('/3')
def testFunction3():
    return redirect(url_for('goToThirdPage'))

@app.route('/second')
def goToSecondPage():
    return 'Second Page'

@app.route('/third')
def goToThirdPage():
    return 'Third Page'


if __name__ == '__main__':
    app.run(debug=True)