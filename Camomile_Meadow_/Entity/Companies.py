from Camomile_Meadow_ import database


class Companies(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(255))
    image_url = database.Column(database.String(255))
    rating = database.Column(database.Integer)

    def __init__(self, id, name, image_url, rating):
        self.id = id
        self.name = name
        self.image_url = image_url
        self.rating = rating

    @property
    def serialized(self):
        """Return object data in serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'image_url': self.image_url,
            'rating': self.rating
        }
