from flask import Blueprint, render_template,request, redirect, session, flash,url_for
from backend.validate import Auth
from backend.access_db import AccessDB
import logging
logging.basicConfig(level=logging.DEBUG)

admin_bp = Blueprint("admin",__name__)

def db_connect():
    db_path = 'backend/user_data.db'
    return  AccessDB(db_path)

@admin_bp.route('/admin',methods=["GET","POST"])
def admin():
  
    if not session.get("name"):
        return redirect(url_for("login.login"))
    
    with db_connect() as db:
        all_users = db.get_all_users()    
    
    if request.method == "POST":

        with db_connect() as db: 
            updated_users = request.form.get()
            for user in updated_users:
                db.update_admin_status()





    return render_template('admin.html',all_users=all_users)