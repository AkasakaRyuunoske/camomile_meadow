from Camomile_Meadow_ import database


class Example1(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "{\"name\":\"" + self.name + "\", \"id\":" + str(self.id) + "}"
