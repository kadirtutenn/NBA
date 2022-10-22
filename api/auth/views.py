import email
from flask import Blueprint, redirect, render_template, request
from flask import flash, url_for, session, jsonify
from dbops.user import User

api = Blueprint("auth_api", __name__)


@api.route("/home", methods=["GET", "POST"])
def home():
    return jsonify({"status": "welcome"})


@api.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(email, password)
        if User.get_by_email(email):
            flash("Given email already exist!!!")
            return redirect(url_for("auth_api.register"))
        # newUSer = userClass(None, email, password)
        User.create({"email": email, "password": password})
        flash("successfully registered, please login")
        return redirect(url_for("auth_api.login"))

    return render_template("register.html")


@api.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username, password)
        user = User.get_by_email(username)

        if not user:
            flash("User not found!!!")
            return redirect(url_for("auth_api.login"))
        if password != user["password"]:
            flash("Wrong password!!!")
            return redirect(url_for("auth_api.login"))
        return redirect(url_for("auth_api.home"))
    return render_template("login.html")
