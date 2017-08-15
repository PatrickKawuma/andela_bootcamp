__author__ = 'patrick'


from flask import Flask, render_template

app = Flask(__name__)  # '__main__'

@app.route('/') # www.mysite.com/
def hello_method():
    return render_template('login.html')

@app.route('/shoppinglist')
def shopping_list():
    return render_template('shoppinglists.html')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/items')
def items():
    return render_template('items.html')


if __name__ == '__main__':
    app.run(port=5050)



