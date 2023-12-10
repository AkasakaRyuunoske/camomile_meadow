from flask import Blueprint
from Camomile_Meadow_.Repository import companies_repository

import logging as log


get_companies_controller_bp = Blueprint("get_companies_controller_bp", __name__)
@get_companies_controller_bp.route("/api/v1/companies", methods=['GET'])
def get_companies():
    return {"companies": companies_repository.select_all()}


get_company_by_id_controller_bp = Blueprint("get_company_by_id_controller_bp", __name__)
@get_company_by_id_controller_bp.route("/api/v1/company/<int:id>", methods=['GET'])
def get_companies(id):
    log.info("id: " + str(id))
    print("id: " + str(id))
    return {"companies": companies_repository.select_by_id(id)}


get_company_by_name_controller_bp = Blueprint("get_company_by_name_controller_bp", __name__)
@get_company_by_name_controller_bp.route("/api/v1/company/<string:name>", methods=['GET'])
def get_companies(name):
    log.info("id: " + str(name))
    print("name: " + str(name))
    return {"companies": companies_repository.select_by_name(name)}
