from flask import Blueprint
from Camomile_Meadow_.Repository import example1_repository

api_index_controller_bp = Blueprint('api_index_controller', __name__)
print("api_index_controller_bp entity: ready")


@api_index_controller_bp.route("/api/v1/index")
def api_index_controller():
    # time.sleep(5)

    return {'message': example1_repository.select_all()}
