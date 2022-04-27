import requests

from os import environ

URL = environ["INGRESS_URL"]

def test_status():
    status_code = requests.get(f"{URL}/dev/front/").status_code
    assert status_code == 200
