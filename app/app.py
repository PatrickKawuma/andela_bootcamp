__author__ = 'patrick'

from models.models import User, ShoppingList
from flask import Flask, render_template, request


SHOPPING_LISTS = []
USERS = []

app = Flask(__name__)  # '__main__'

@app.route('/') # www.mysite.com/
def hello_method():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if User.login_valid(username, password):
            User.login(username)
            return render_template('shoppinglists.html')
        return "Invalid Login"
    return render_template('login.html')


@app.route('/shoppinglist', methods=['GET', 'POST'])
def shopping_list():

    if request.method == "POST":
        name = request.form['listname']
        budget = request.form['budget']

        shop_list = ShoppingList(name, budget)
        SHOPPING_LISTS.append(shop_list)
        print (list(x.name for x in SHOPPING_LISTS))  #check that my lists are stored until server restart
 
        #result = [{'name':name, 'budget':budget},]
        result = SHOPPING_LIST
        return render_template('shoppinglists.html', result=result)
    return render_template('shoppinglists.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    #print("inside function")
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        new_user = User(username, password)
        USERS.append(new_user)

        print (list(y.username for y in USERS))   #check that users are stored until server restart
        return "registering..."    
    return render_template('registration.html')



@app.route('/items')
def items():
    return render_template('items.html')


#app.config['DEBUG'] = True
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://DB_USER:PASS@HOST/DB'
'''
POSTGRES = {
    'user': 'postgres',
    'password': '',
    'host': 'localhost',
    'port': '5432',
    'db': 'dev',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{password}@{host}:{port}/{db}'.format(**POSTGRES)


if __name__ == '__main__':
    app.run(port=5050)



