from typing import Tuple, Dict

from Camomile_Meadow_.Repository import companies_repository


def serve_post_company_request(request_json: dict[str, str]) -> tuple[dict[str, str], int, dict[str, str]]:
    if not isinstance(request_json, dict):
        return {"result": "Bad request", "details": "Request body doesn't seem to be of JSON type"}, \
            400, \
            {'Content-Type': 'application/json'}

    if not request_json.keys().__contains__("name") & \
            request_json.keys().__contains__("image_url") & \
            request_json.keys().__contains__("rating"):
        return {"result": "Bad request", "details": "Request body doesn't contain one or more necessary keys"},\
            400,\
            {'Content-Type': 'application/json'}

    # companies_repository.insert_from_json({"name": "sample name", "image_url": "https://fvck.you", "rating": "1"})
    # companies_repository.insert_from_json(request_json)

    return {"result": "created"}, 201, {'Content-Type': 'application/json'}
