from Camomile_Meadow_ import application
from flask import Blueprint

debug_index_controller_bp = Blueprint('debug_index_controller_bp', __name__)


@application.route("/")
def index_controller():
    print("Chloe was called ♥ [aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa]")
    return "camomile meadow works!"
