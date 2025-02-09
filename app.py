from flask import Flask, render_template, redirect
from pages.home import home_pb
from pages.login import login_pb
from pages.signup import signup_pb
from backend.api import api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(home_pb)
app.register_blueprint(login_pb)
app.register_blueprint(signup_pb)
app.register_blueprint(api)

@app.route("/")
def base():
    return redirect("/home")

if __name__ == "__main__":
    app.run(port=5005,debug=True)