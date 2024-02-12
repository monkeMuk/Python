from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', Aircraft='A220')




if __name__ == '__main__':
    app.run(debug=True)



'''
redirect = links
render_template = webpages

'''