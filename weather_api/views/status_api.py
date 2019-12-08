from flask import Blueprint

status_api = Blueprint('status_api', __name__)

@status_api.route("/")
def get_status():
    return "API is running"
