from flask import Blueprint
from Camomile_Meadow_.Entity import Example
import time

api_index_controller_bp = Blueprint('api_index_controller', __name__)
print("api_index_controller_bp entity: ready")


@api_index_controller_bp.route("/api/v1/index")
def api_index_controller():
    print(str(Example.Example1.query.all()))

    time.sleep(5)

    return {'message': 'I love you so much'}
