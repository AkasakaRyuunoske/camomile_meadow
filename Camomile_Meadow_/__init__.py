import logging as log

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

log.warning("Initialisation started.")


def create_application():
    application = Flask(__name__)

    application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' \
                                                    '@localhost/garden'
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://akasaka:__s4nm4nd3fu4nt31n4k0n0s3k41k4kum31h00k0s' \
    #                                                 '@garden.c3nppvyztw1w.eu-north-1.rds.amazonaws.com/garden'

    return application


application = create_application()
database = SQLAlchemy(application)


@application.errorhandler(404)
def not_found(error):
    print(request.headers.get('User-Agent').__contains__("Chrome"))

    if request.headers.get('User-Agent').__contains__("Chrome"):
        return render_template("error_404.html")
    else:
        return {'result': 'End-point does not exist(yet)', 'detailed_message': str(error)}, \
            404, \
            {'Content-Type': 'application/json'}


@application.errorhandler(405)
def method_not_allowed(error):
    print(request.headers.get('User-Agent'))

    if request.headers.get('User-Agent').__contains__("Chrome"):
        return render_template("error_405.html")
    else:
        return {'result': 'Method is not allowed', 'detailed_message': str(error)}, \
            405, \
            {'Content-Type': 'application/json'}


@application.errorhandler(500)
def method_not_allowed(error):
    print(request.headers.get('User-Agent'))

    if request.headers.get('User-Agent').__contains__("Chrome"):
        return render_template("error_405.html")
    else:
        return {'result': 'Method is not allowed', 'detailed_message': str(error)}, \
            405, \
            {'Content-Type': 'application/json'}


# @application.errorhandler(400)
# def bad_request(e):
#     print(e)
#     return {"result": "Bad Request"}


log.info("trying to create database schema")

from Camomile_Meadow_.Controller import index_controller
from Camomile_Meadow_.Controller import debug_controller
from Camomile_Meadow_.Controller import companies_controller

# index_controller
application.register_blueprint(index_controller.api_index_controller_bp)

# debug_controller
application.register_blueprint(debug_controller.debug_index_controller_bp)

#   companies_controller
# GET endpoints
application.register_blueprint(companies_controller.get_companies_controller_bp)
application.register_blueprint(companies_controller.get_company_by_id_controller_bp)
application.register_blueprint(companies_controller.get_company_by_name_controller_bp)

application.register_blueprint(companies_controller.post_company_controller_bp)
