from flask import Blueprint, render_template,request, redirect, session, flash,url_for
from backend.validate import Auth
from backend.access_db import AccessDB
import logging
logging.basicConfig(level=logging.DEBUG)

edit_email_bp = Blueprint("edit_email",__name__)

def db_connect():
    db_path = 'backend/user_data.db'
    return  AccessDB(db_path)

@edit_email_bp.route('/edit_email',methods=["GET","POST"])
def edit_email():
    
    if not session.get("name"):
        return redirect(url_for("login.logout"))
    
    with db_connect() as db:
        user = db.get_user_info(session["name"])
        
    if request.method == "POST":
        new_email = request.form.get("newEmail")
        password = request.form.get("password")

        with db_connect() as db:
            user = db.get_user_info(session["name"])
            if Auth.verify_password(user,password):
                db.update_user_email(new_email,session["id"])
                session["name"] = new_email
                flash("Email has been updated!")
                return redirect(url_for("edit_email.edit_email"))
            else:
                flash("Password Validation failed")
                return redirect(url_for("edit_email.edit_email"))
        
        
        

    return render_template('edit_email.html',user_info=user)