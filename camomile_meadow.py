from Camomile_Meadow_ import application
# application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://akasaka:__s4nm4nd3fu4nt31n4k0n0s3k41k4kum31h00k0s' \
#                                                 '@garden.c3nppvyztw1w.eu-north-1.rds.amazonaws.com/garden'


@application.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response


if __name__ == '__main__':
    print("Started")
    application.run(debug=True)
