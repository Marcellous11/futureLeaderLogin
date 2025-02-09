from flask import Blueprint, render_template

signup_pb = Blueprint("signup",__name__)


@signup_pb.route('/signup')
def signup():
    return render_template('signup.html')