from flask import Blueprint, render_template,request, redirect, session, flash,url_for
from backend.validate import Auth
from backend.access_db import AccessDB
import logging
logging.basicConfig(level=logging.DEBUG)

user_profile_bp = Blueprint("user_profile",__name__)

def db_connect():
    db_path = 'backend/user_data.db'
    return  AccessDB(db_path)

@user_profile_bp.route('/user_profile',methods=["GET","POST"])
def user_profile():
    if request.method == "POST":
        pass

    if not session.get("name"):
        return redirect(url_for('login.logout'))
    
    with db_connect() as db:
        user = db.get_user_info(session.get('name'))
 

    print(session.get('name'))
    return render_template('user_profile.html',user_info=user)