import requests
import jsonschema

from os import environ

URL = environ["INGRESS_URL"]

def test_status():
    status_code = requests.get(f"{URL}/dev/api/api/status/").status_code
    assert status_code == 200

def test_body():
    schema = {
        "type": "object",
        "properties": {
            "request_uuid": {
                "type": "string"
            }, 
            "time": {
                "type": "string"
            }
        },
        "required": ["request_uuid", "time"]
    }
    validator = jsonschema.Draft7Validator(schema)
    body = requests.get(f"{URL}/dev/api/api/status/").json()
    assert validator.is_valid(body)
    