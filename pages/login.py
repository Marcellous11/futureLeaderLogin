from flask import Blueprint, render_template

login_pb = Blueprint("login",__name__)


@login_pb.route('/login')
def login():
    return render_template('login.html')