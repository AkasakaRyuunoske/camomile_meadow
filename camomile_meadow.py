from Camomile_Meadow_ import application, database
import logging as log


@application.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response


if __name__ == '__main__':
    print("Started")

    with application.app_context():
        log.info("trying to create database schema")
        database.create_all()

    application.run(debug=True)
