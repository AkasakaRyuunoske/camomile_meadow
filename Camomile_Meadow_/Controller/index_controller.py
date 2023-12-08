from flask import Blueprint
from Camomile_Meadow_.Entity import Example

api_index_controller_bp = Blueprint('api_index_controller', __name__)
print("api_index_controller_bp entity: ready")


@api_index_controller_bp.route("/api/v1/index")
def api_index_controller():
    print(str(Example.Example1.query.all()))
    return "@"
