# Creating a User Class

import sqlite3

class Users:
    
    TABLE_NAME = 'users'

    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password


    def find_by_username(self,username):

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query= "SELECT * FROM {table} WHERE username = ?".format(table = self.TABLE_NAME)

        cursor.execute(query, (username,))


class UserRegister:

    def getUserNameByMapping():
        userlist = ['A','B']
        for user in userlist:
            if user.name == "key":
            # Replacing the user password and user name
            
                user.password = 'something else'
