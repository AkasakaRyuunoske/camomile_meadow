from Camomile_Meadow_ import application, database
import logging as log
from Camomile_Meadow_.Entity import Example, Companies

""" 
    Adds after each request these headers. Access-Control-Allow-Origin & Access-Control-Allow-Headers
    are needed to prevent CORS issues when the request source is not the same application 
"""


@application.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response


if __name__ == '__main__':
    print("Started")

    """ When the application context is created, the database schema will be automatically created. 
        But the tables from entities will be created as they are needed, unlike Java's hibernate where the whole 
        schema is created when the application is ran."""
    with application.app_context():
        log.info("trying to create database schema")
        database.create_all()

        # todo create a service to read queries from file and execute them if they weren't yet.

        # example = Example.Example1(11, "Mythical Jasmine")
        # company = Companies.Companies(1, "Greenfield", "none for now", 10)
        # company2 = Companies.Companies(2, "Lipton", "none for now", 6)
        #
        # database.session.add(example)
        # database.session.add(company)
        # database.session.add(company2)
        # database.session.commit()

    application.run(debug=True, use_reloader=False)
