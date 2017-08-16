__author__ = "patrick"

import datetime
import uuid
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



class Item:
    def __init__(self, name, quantity, price):
         self.name = name
         self.quantity = 1 #default
	 self.price = price

    def json(self):
        return {
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }


class ShoppingList:
    def __init__(self, list_name, items, budget):
        self.name = name
        self.items = {}
        self.date = datetime.datetime.utcnow()
        self.budget = budget


    def add_item(self, item_name, quantity, price):
        if isinstance(item_name, str) and isinstance(quantity, int) and isinstance(price, int):
            if item_name in self.items:
                self.items.update({item_name: quantity})
            '''
            item = Item(name=item_name,
                    quantity=quantity,
                    price=price
               )
            '''

    def remove_item(self, item_name):
        del self.items[item_name]

    def edit_item(self, item_name, quantity):
        if item_name in self.items:
            return item_name, items[item_name]


class User:
    def __init__(self, username, password):
        self.username = username
	self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_user(cls, username):
        #search db for username
        if user:
            return user

    @staticmethod #doesnt need self(dynamic instance)
    def login_valid(username_field, password_field):
        #if self.username == username_field && self.password == password_field:
        user = User.get_user(username_field)
        if user is not None:
            return user.password == password_field
	return False

    @staticmethod
    def login(username):
       #login_valid is called
        session['email'] = username

    #@staticmethod
    @classmethod 
    def register(cls, username, password):
        #user = User.get_user(username):
        user = cls.get_user(username):
        if user is None:
            new_user = cls(username, password)
            #new_user.save()
            #return session['username'] = username
            return True           
	return False #"user already exists"

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
	return ShoppingList(list_name, items)

    def can_add_item(self, shopping_list):
        return shopping_list.add_item()

    def can_delete_item(self, shopping_list):
	return shopping_list.remove_item()

    def can_edit_item(self, shopping_list):
        return shopping_list.edit_item()





