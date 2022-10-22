from flask import Flask, jsonify, request, render_template, flash
from schemas import RegistrationForm
from api.auth.views import api as auth_api
from api.team.views import api as team_api
from api.player.views import api as player_api
from api.user.views import api as user_api


app = Flask(__name__)
app.config["SECRET_KEY"] = "somesecretkey"


app.register_blueprint(blueprint=auth_api, url_prefix="/api/auth")
app.register_blueprint(blueprint=team_api, url_prefix="/api/team")
app.register_blueprint(blueprint=player_api, url_prefix="/api/player")
app.register_blueprint(blueprint=user_api, url_prefix="/api/user")


if __name__ == "__main__":
    app.run(debug=True)


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
