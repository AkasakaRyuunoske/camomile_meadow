from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://akasaka:__s4nm4nd3fu4nt31n4k0n0s3k41k4kum31h00k0s' \
                                                '@garden.c3nppvyztw1w.eu-north-1.rds.amazonaws.com/garden'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(application)


class example1(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "{\"name\":\"" + self.name + "\", \"id\":" + str(self.id) + "}"


@application.route("/api/v1/index")
def api_index_controller():
    print(str(example1.query.all()))
    return "@"


@application.route("/")
def index_controller():
    print("Chloe was called ♥ [aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa]")
    return "camomile meadow works!"


if __name__ == '__main__':
    print("Started")
    application.run(debug=True)
