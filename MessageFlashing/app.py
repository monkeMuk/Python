from flask import Flask,render_template, flash

app = Flask(__name__)
#flash uses cookie, gotta set a secret key
app.secret_key = 'TEST'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/flash')
def flash_message():
    flash('this is a flashed message')
    return render_template('flash.html')

if __name__ == '__main__':
    app.run(debug=True)

'''
https://www.youtube.com/watch?v=DFCKWhoiHZ4&t=216s&pp=ygUfVXNpbmcgTWVzc2FnZSBGbGFzaGluZyBpbiBGbGFzaw%3D%3D

Using Message Flashing in Flask
'''