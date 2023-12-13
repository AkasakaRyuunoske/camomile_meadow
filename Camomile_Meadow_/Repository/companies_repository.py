from Camomile_Meadow_.Entity import Companies
from Camomile_Meadow_ import database

def select_all():
    query_results = Companies.Companies.query.all()

    return [query_result.serialized for query_result in query_results]

def select_by_id(id):
    query_results = Companies.Companies.query.filter_by(id=id)

    return [query_result.serialized for query_result in query_results]


def select_by_name(name):
    query_results = Companies.Companies.query.filter_by(name=name)

    return [query_result.serialized for query_result in query_results]


def insert_from_json(json: dict) -> None:
    # print(json.get("name") + json.get("image_url") + json.get("rating"))
    company = Companies.Companies(json.get("name"), json.get("image_url"), json.get("rating"))

    database.session.add(company)
    database.session.commit()


def update_by_id(id: int) -> None:
    query_result = Companies.Companies.query.filter_by(id=id).first()

    query_result.name = "new name"
    database.session.commit()
