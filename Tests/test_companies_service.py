from Camomile_Meadow_.Service.companies_service import serve_post_company_request


def test_companies_when_request_is_correct():
    request_json = {"name": "prikoldesic", "image_url": "prikoldesic", "rating": "prikoldesic", }

    result = serve_post_company_request(request_json)
    print(result[0].get('result'))
    print(result)
    assert type(result) == tuple
    assert not result[0].get('result').__contains__("Bad request")
    assert result[1] == 201
    assert result[2].get('Content-Type').__contains__("application/json")


def test_companies_when_json_is_incorrect():
    incorrect_json = "incorect json"

    result = serve_post_company_request(incorrect_json)
    assert result[0].get('result').__contains__("Bad request")
    assert result[1] == 400
    assert result[2].get('Content-Type').__contains__("application/json")
    print(result)
