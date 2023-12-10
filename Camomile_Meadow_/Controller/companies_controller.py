from flask import Blueprint
from Camomile_Meadow_.Entity import Companies

companies_controller_bp = Blueprint("companies_controller_bp", __name__)


@companies_controller_bp.route("/api/v1/companies", methods=['GET'])
def get_companies():
    print(str(Companies.Companies.query.all()))
    return {"companies": "GREENFIELD"}
