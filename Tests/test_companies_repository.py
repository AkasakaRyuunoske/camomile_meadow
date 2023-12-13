from flask_sqlalchemy import SQLAlchemy

from Camomile_Meadow_.Repository import companies_repository

def test_if_update_by_id_works_correctly(application):
    database = SQLAlchemy(application)
    application.app_context()
    print(companies_repository.update_by_id(1))
