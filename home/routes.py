from flask import Flask, Blueprint, render_template

app = Flask(__name__)
home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def index():
    return render_template("home/index.html", title="Dashboard", balance=1500)


if __name__ == "__main__":
    app.run(debug=True)