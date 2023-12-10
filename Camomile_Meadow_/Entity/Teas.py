# from sqlalchemy import ForeignKey
#
# from Camomile_Meadow_ import database
#
#
# class Teas(database.Model):
#     id = database.Column(database.Integer, primary_key=True)
#     name = database.Column(database.String(255))
#     rating = database.Column(database.Integer)
#     image_url = database.Column(database.String(255))
#     tea_company_id_fk = database.Column(database.Integer, ForeignKey("companies.id", ondelete='CASCADE', onupdate='CASCADE'))
#     tea_collection_id_fk = database.Column(database.Integer, ForeignKey("collections.id", ondelete='CASCADE', onupdate='CASCADE'))
#     tea_type_id_fk = database.Column(database.Integer, ForeignKey("types.id", ondelete='CASCADE', onupdate='CASCADE'))
