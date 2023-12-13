import pytest
from flask_sqlalchemy import SQLAlchemy
from Camomile_Meadow_ import create_application
from Camomile_Meadow_.Controller.index_controller import api_index_controller_bp


@pytest.fixture()
def application():
    application = create_application()
    application.config.update({
        "TESTING": True
    })

    application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' \
                                                    '@localhost/garden'
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    yield application


# @pytest.fixture()
# def database(application):
#
#     yield database

@pytest.fixture()
def client(application):
    # application.register_blueprint(api_index_controller_bp)

    return application.test_client()


@pytest.fixture()
def runner(application):
    return application.test_cli_runner()
