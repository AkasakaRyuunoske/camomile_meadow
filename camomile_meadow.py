from flask import Flask

application = Flask(__name__)


@application.route("/")
def index_controller():
    print("Chloe was called ♥ [aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa]")
    return "camomile meadow works!"


if __name__ == '__main__':
    print("Started")
    application.run(debug=True)
