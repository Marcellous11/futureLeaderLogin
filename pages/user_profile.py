from flask import Blueprint, render_template,request, redirect, session, flash,url_for
from backend.validate import Auth
from backend.access_db import AccessDB
import logging
logging.basicConfig(level=logging.DEBUG)

user_profile_bp = Blueprint("user_profile",__name__)

def db_connect():
    db_path = 'backend/user_data.db'
    return  AccessDB(db_path)

@user_profile_bp.route('/signup',methods=["GET","POST"])
def signup():
    if request.method == "POST":
     
        email = request.form.get("userEmail")
        password = request.form.get("userPassword")
        confirmPassword = request.form.get("confirmPassword")

        if password != confirmPassword:
            flash("Passwords did not match")
            return redirect(url_for("signup.signup"))

       
        with db_connect() as db:
            user = db.get_user_info(email)
            if  user:
                flash("Email Already Registered")
                return redirect(url_for("login.login"))
        
            hashed_password = Auth.hash_password(password)
        
          
            if db.add_new_user(email,hashed_password):
                flash("Registration Successful")
                return redirect(url_for("login.login"))
            else:
                flash("Registration Failed")
                return redirect(url_for("signup.signup"))

   
    if session.get("name"):
        return redirect(url_for("home.home"))

    return render_template('signup.html')