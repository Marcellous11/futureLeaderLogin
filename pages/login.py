from flask import Blueprint, render_template,redirect,request, session,flash,url_for
from backend.validate import Auth
from backend.access_db import AccessDB


login_bp = Blueprint("login",__name__)

def db_connect():
    db_path = 'backend/user_data.db'
    return  AccessDB(db_path)

@login_bp.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("userEmail")
        password = request.form.get("userPassword")

        print(email)
        print(password)

        with db_connect() as db:
            user = db.get_user_info(email)
            if not user:
                print("bad email")
                flash("Email Not Found")
                return redirect(url_for("login.login"))

            if Auth.verify_password(user,password):
                session["name"] = user["email"]
                session["admin"] = user.get("admin",0)
                print(f"Sesison after login: {session}")
                flash("Correct Password")
    
                return redirect(url_for("login.login"))
            else:
                print("BAD PASSWORD")
                flash("Incorrect Password")
                return redirect(url_for("login.login"))
        
    if session.get("name"):
        return redirect(url_for("home.home"))

    return render_template('login.html')

@login_bp.route('/logout')
def logout():
    session.pop("name",None)
    session.pop("admin",None)
    session.clear()
    flash("Logged Out")
    return redirect(url_for("login.login"))