import logging as log

from flask import Blueprint, request

from Camomile_Meadow_.Repository import companies_repository

# todo implement necessary validation logic as services
# todo add documentation
# todo test whole module
API_V1_URL_PREFIX = "/api/v1"

get_companies_controller_bp = Blueprint("get_companies_controller_bp", __name__)


@get_companies_controller_bp.route(API_V1_URL_PREFIX + "/companies", methods=['GET'])
def get_companies() -> dict:
    return {"companies": companies_repository.select_all()}


get_company_by_id_controller_bp = Blueprint("get_company_by_id_controller_bp", __name__)


@get_company_by_id_controller_bp.route(API_V1_URL_PREFIX + "/company/<int:id>", methods=['GET'])
def get_companies(id: int) -> dict:
    log.info("id: " + str(id))
    print("id: " + str(id))
    return {"companies": companies_repository.select_by_id(id)}


get_company_by_name_controller_bp = Blueprint("get_company_by_name_controller_bp", __name__)


@get_company_by_name_controller_bp.route(API_V1_URL_PREFIX + "/company/<string:name>", methods=['GET'])
def get_companies(name: str) -> dict:
    log.info("id: " + str(name))
    print("name: " + str(name))
    return {"companies": companies_repository.select_by_name(name)}


post_company_controller_bp = Blueprint("post_company_controller_bp", __name__)


@post_company_controller_bp.route(API_V1_URL_PREFIX + "/company", methods=['POST'])
def post_company() -> dict:
    data = request.get_json()
    print(data)

    # companies_repository.insert_from_json({"name": "sample name", "image_url": "https://fvck.you", "rating": "1"})
    companies_repository.insert_from_json(data)
    return {"status": "200 OK"}


put_company_by_id_controller_bp = Blueprint("put_company_by_id_controller_bp", __name__)


@put_company_by_id_controller_bp.route(API_V1_URL_PREFIX + "/company/<int: id>")
def put_company_by_id(id: int) -> tuple[dict[str, str], int, dict[str, str]]:  # lol
    companies_repository.update_by_id(id)
    return {"result": "not yet ready"}, 200, {'Content-Type': 'application/json'}
    # 405 coz this guy said that: https://stackoverflow.com/a/32890136
    # ᓚᘏᗢ
