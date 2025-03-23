from flask import Flask, redirect,url_for,session,flash

from flask_cors import CORS
from pages.signup import signup_bp
from pages.home import home_bp
from pages.login import login_bp
from pages.auth.admin import admin_bp
from pages.user_profile import user_profile_bp
from pages.edit_email import edit_email_bp
from pages.edit_password import edit_password_bp
from flask_session import Session

app = Flask(__name__)
app.config.from_pyfile("config.py")
CORS(app)
Session(app)


app.register_blueprint(home_bp)
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(user_profile_bp)
app.register_blueprint(edit_email_bp)
app.register_blueprint(edit_password_bp)


@app.route("/")
def base():
    return redirect(url_for("home.home"))


@app.route('/clear_session')
def clear_session():
    session.clear()
    # flash("Session cleared!")
    return redirect(url_for("home.home"))


if __name__ == "__main__":
    app.run(port=3000,debug=True)
