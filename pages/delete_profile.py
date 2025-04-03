from flask import Blueprint, render_template,request, redirect, session, flash,url_for
from backend.validate import Auth
from backend.access_db import AccessDB
import logging
logging.basicConfig(level=logging.DEBUG)

delete_profile_bp = Blueprint("delete_profile",__name__)

def db_connect():
    db_path = 'backend/user_data.db'
    return  AccessDB(db_path)

@delete_profile_bp.route('/delete_profile',methods=["GET","POST"])
def delete_profile():
    
    if not session.get("name"):
        return redirect(url_for("login.logout"))
    
    with db_connect() as db:
        user = db.get_user_info(session["name"])
        
    if request.method == "POST":

        password = request.form.get("password")

        with db_connect() as db:
            user = db.get_user_info(session["name"])
            if Auth.verify_password(user,password):
                db.delete_account(session["id"])
                
                flash("Account has been deleted!")
                return redirect(url_for("login.logout"))
            else:
                flash("Password Validation failed")
                return redirect(url_for("delete_profile.delete_profile"))
        
        
        

    return render_template('delete_profile.html',user_info=user)