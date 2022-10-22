from flask import Blueprint

api = Blueprint("teams_api", __name__)


@api.route("/get", methods=["POST", "GET"])
def getTeams():
    return True

    # html dosyası dönmemiz alzım


@api.route("/update", methods=["POST", "GET"])
def updateTeams():
    return True


@api.route("/delete", methods=["POST", "GET"])
def deleteTeam():
    return True


@api.route("/create", methods=["POST", "GET"])
def createTeam():
    return True
