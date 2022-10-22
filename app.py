from crypt import methods
from flask import Flask, jsonify, request, render_template, flash
from schemas import RegistrationForm
from api.auth.views import api as auth_api
from api.teams.views import api as teams_api
from api.players.views import api as players_api


app = Flask(__name__)

app.register_blueprint(blueprint=auth_api, url_prefix="/api/auth")
app.register_blueprint(blueprint=teams_api, url_prefix="/api/teams")
app.register_blueprint(blueprint=players_api, url_prefix="/api/players")


# @app.route("/homepage")
# def homepage():
#     return jsonify({"status": "success"})


# @app.route("/register", methods=["GET", "POST"])
# def register():
#     form = RegistrationForm(request.form)
#     if request.method == "POST" and form.validate():
#         flash("Thanks for registering")

#     return render_template("register.html", form=form)


# @app.route("/login", methods=["GET", "POST"])
# def login():

#     msg = ""
#     if (
#         request.method == "POST"
#         and "username" in request.form
#         and "password" in request.form
#     ):
#         username = request.form["username"]
#         password = request.form["password"]

#     return render_template("login.html", msg=msg)


if __name__ == "__main__":
    app.run(debug=True)
