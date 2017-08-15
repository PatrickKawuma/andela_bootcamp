__author__ = "patrick"
import uuid

class Item:
    def __init__(self, name, quantity, price):
         self.name = name
         self.quantity = 1 #default
	 self.price = price


class ShoppingList:
    def __init__(self, list_name, items):
        self.name = name
        self.items = {}
        
    def add_item(self, item_name, quantity):
        self.items.update({item_name: quantity})
        
    def remove_item(self, item_name):
        del self.items[item_name]

    def edit_item(self, item_name):
        return items[item_name]


class User:
    def __init__(self, username, password):
        self.username = username
	self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id


    def get_user(self, username):
        #search db for username
        if user:
            return user

    @staticmethod
    def login(self, username_field, password_field):
        if self.username == username_field && self.password == password_field:
            return True
	return False

    @classmethod
    def register(self, username, password):
        user = cls.get_user(username):
        if user is None:
            new_user = cls(username, password)
	    return True
	return "user already exists"


    def can_create_shoppinglist(self, list_name, items):
	return ShoppingList(list_name, items)

    def can_add_item(self, shopping_list):
        return shopping_list.add_item()

    def can_delete_item(self, shopping_list):
	return shopping_list.remove_item()

    def can_edit_item(self, shopping_list):
        return shopping_list.edit_item()





