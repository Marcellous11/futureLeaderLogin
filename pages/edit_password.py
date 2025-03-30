from flask import Blueprint, render_template,request, redirect, session, flash,url_for
from backend.validate import Auth
from backend.access_db import AccessDB
import logging
logging.basicConfig(level=logging.DEBUG)

edit_password_bp = Blueprint("edit_password",__name__)

def db_connect():
    db_path = 'backend/user_data.db'
    return  AccessDB(db_path)

@edit_password_bp.route('/edit_password',methods=["GET","POST"])
def edit_password():
    
    if not session.get("name"):
        return redirect(url_for("login.logout"))

    with db_connect() as db:
        user = db.get_user_info(session["name"])
        
    if request.method == "POST":
        password = request.form.get("currentPassword")
        new_password = request.form.get("newPassword")

        with db_connect() as db:
            user = db.get_user_info(session["name"])
            
            if Auth.verify_password(user,password):
                new_hashed_password = Auth.hash_password(new_password)
                db.update_user_password(new_hashed_password,session["id"])

                flash("Password has been updated!")
                return redirect(url_for("user_profile.user_profile"))
            else:
                flash("Password Validation failed")
                return redirect(url_for("edit_password.edit_password"))
            
    return render_template('edit_password.html',user_info=user)