from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging as log

log.warning("Initialisation started.")

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' \
                                                '@localhost/garden'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://akasaka:__s4nm4nd3fu4nt31n4k0n0s3k41k4kum31h00k0s' \
#                                                 '@garden.c3nppvyztw1w.eu-north-1.rds.amazonaws.com/garden'

database = SQLAlchemy(application)

log.info("trying to create database schema")


from Camomile_Meadow_.Entity import Example
from Camomile_Meadow_.Controller import index_controller, debug_controller, companies_controller

# index_controller
application.register_blueprint(index_controller.api_index_controller_bp)

# debug_controller
application.register_blueprint(debug_controller.debug_index_controller_bp)

# companies_controller
application.register_blueprint(companies_controller.get_companies_controller_bp)
application.register_blueprint(companies_controller.get_company_by_id_controller_bp)
application.register_blueprint(companies_controller.get_company_by_name_controller_bp)
