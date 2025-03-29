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
        return redirect(url_for("login.login"))
    return render_template('home.html')