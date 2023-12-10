from Camomile_Meadow_.Entity import Companies

def select_all():
    query_results = Companies.Companies.query.all()

    return [query_result.serialized for query_result in query_results]

def select_by_id(id):
    query_results = Companies.Companies.query.filter_by(id=id)

    return [query_result.serialized for query_result in query_results]


def select_by_name(name):
    query_results = Companies.Companies.query.filter_by(name=name)

    return [query_result.serialized for query_result in query_results]
