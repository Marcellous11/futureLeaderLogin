from flask import Blueprint, render_template, redirect
home_pb = Blueprint("home",__name__)


@home_pb.route('/home')
def home():
    logged_in = True

    if not logged_in:
        return redirect("login")
    
    return render_template('home.html',logged_in=True)