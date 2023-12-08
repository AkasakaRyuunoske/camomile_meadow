from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' \
                                                '@localhost/garden'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(application)

from Camomile_Meadow_.Entity import Example
from Camomile_Meadow_.Controller import index_controller

application.register_blueprint(index_controller.api_index_controller_bp)
