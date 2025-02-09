from flask import Flask, request, jsonify, Blueprint,redirect
import sqlite3
from backend.validate import Auth
from backend.access_db import AccessDB

api = Blueprint("api",__name__)


def db_connect():
    db_path = 'backend/user_data.db'
    return  AccessDB(db_path)


@api.route('/signup', methods=['POST'])
def signup():
    print(request.data)
    email = request.form.get("userEmail")
    password = request.form.get("userPassword")

    db = db_connect()
    user = db.get_user_info(email)
    if user:
        print("User already exist")
        return redirect("login")
    
    print("----->",email)
    print("----->",password)
    hash_password = Auth.hash_password(password=password)
 
    if db.add_new_user(email,hash_password):
        db.close_connection()
        print("New user added successfully")
        return redirect("login")
        
    else:
         db.close_connection()
         print("New user not edded successfully")
         return redirect("signup")
         
        




@api.route('/login', methods=['POST'])
def login():

    print(request.data)
    email = request.form.get("userEmail")
    password = request.form.get("userPassword")

    db = db_connect()  

    user = db.get_user_info(email)
    if not user:
        print("Email Not Found")
        return redirect("login")

    if Auth.verify_password(user,password):
        print("Correct Password")
        return redirect("home")

    else:
        print("Incorrect Password")
        return redirect("login")
   




# {
#   "email":"newWorld.e@example.com", 
#   "password":"Thisismypassword"
# }
# newWorld.e@example.com
# Thisismypassword

# application/x-www-form-urlencoded