from flask import Blueprint, render_template, redirect, session,url_for

home_bp = Blueprint("home",__name__)


@home_bp.route('/home')
def home():

    if not session.get("name"):
        return redirect(url_for("login.login"))
    return render_template('home.html')