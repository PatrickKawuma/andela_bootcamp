__author__ = "patrick"
import uuid
import datetime

'''
class Item:
    def __init__(self, name, quantity, price):
         self.name = name
         self.quantity = 1 #default
	 self.price = price
'''

class ShoppingList:
    def __init__(self, list_name, budget, user): #takes arguments of list_name(str), budget(float) and a user object
        self.name = name
        self.budget = budget
        self.items = {}
        self.created = datetime.datetime.today().strftime('%Y-%m-%d')
        self.id = uuid.uuid4().hex
        self.user_id = user.id

    def add_item(self, item_name, quantity, price):
        if isinstance(item_name, str) and isinstance(quantity, int):
            self.items.update({item_name : {'quantity' :quantity, 'price': price}})


    def remove_item(self, item_name):
        del self.items[item_name]


    def edit_item_data(self, item_name, quantity, price):
            self.items[item_name]['quantity'] = quantity
            self.items[item_name]['price'] = price


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.created = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.id = uuid.uuid4().hex

    def get_user(self, username):
        #search db for username
        if user:
            return user

    @staticmethod
    def login_valid(self, username_field, password_field):
        if self.username == username_field and self.password == password_field:
            return True
        return False

    @staticmethod
    def login(username):
       #login_valid is called
        session['email'] = username


    @classmethod
    def register(cls, username, password):
        user = cls.get_user(username)
        if user is None:
            new_user = cls(username, password)
            #new_user.save()
            session['username'] = username
            return True
        return "user already exists"

    @staticmethod
    def logout():
        session['email'] = None

    def json(self):
        return {
            "username": self.username,
            "_id": self.id,
            "password": self.password
        }


    def can_create_shoppinglist(self, list_name, items):
        return ShoppingList(list_name, budget, cls.id)

    def add_item(self, item_name, quantity, shopping_list):
        return shopping_list.add_item(item_name, quantity, price)

    def delete_item(self, item_name, shopping_list):
        return shopping_list.remove_item(item_name)

    def edit_item(self, shopping_list, data): #data expected as item_name, quantity and price
        return shopping_list.edit_item_data(**data)





