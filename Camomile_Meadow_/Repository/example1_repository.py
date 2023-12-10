from Camomile_Meadow_.Entity import Example

def select_all():
    query_results = Example.Example1.query.all()

    return [query_result.serialized for query_result in query_results]
