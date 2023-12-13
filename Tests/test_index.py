from ast import literal_eval

import requests

"""
Either me being fool or I am really supposed to write an entire application to unit-test
endpoints. For now, easiest way is to run the application and using request lab perform 
requests on it.
"""


#
# def test_request_debug_index(client):
#     response = client.get("/api/v1/index")
#
#     assert response.status_code == 200
#
#     print(response)


# def test_request_debug_index_requests():
#     response = requests.get("http://localhost:5000/api/v1/index")
#
#     assert response.status_code == 200
#     assert response.content is not None
#
#     converted_response = response.content.decode()
#
#     assert not converted_response.__contains__("null")
#     converted_response = literal_eval(response.content.decode())
#
#     assert 'result' in converted_response
#
#     objects_in_response = converted_response.get("result", [])
#     for item in objects_in_response:
#         assert 'name' in item, 'nope'
#         assert 'id' in item, 'nope'
#
#
# def test_request_debug_index__should_fail_when_method_is_post():
#     response = requests.post("http://localhost:5000/api/v1/index")
#
#     assert response.status_code == 405
#     assert response.content is not None
#
#     converted_response = response.content.decode()
#
#     assert not converted_response.__contains__("null")
#     converted_response = literal_eval(response.content.decode())
#
#     assert 'result' in converted_response is "Method is not allowed"
