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
            updated_users = request.form.to_dict()
            admin_list = [key for key in updated_users.keys()]
            if len(admin_list) == 0:
                flash("WAIT! There must be at least 1 Admin")
                return redirect(url_for("admin.admin"))
         
            for user in all_users:
                if str(user["id"]) in admin_list:
                    db.update_admin_status(user['id'],1)
                else:
                    db.update_admin_status(user["id"],0)
        flash("Admin status updated!")
        return redirect(url_for("admin.admin"))

    return render_template('admin.html',all_users=all_users)