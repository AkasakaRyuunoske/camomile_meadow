from Camomile_Meadow_ import database


class Companies(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(255))
    image_url = database.Column(database.String(255))
    rating = database.Column(database.Integer)
