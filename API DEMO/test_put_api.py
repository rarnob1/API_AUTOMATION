from http.client import responses

import requests
import pytest
import json

endpoint="https://reqres.in/api/users/2"
payload={
    "name": "morpheus",
    "job": "zion resident"
}

def test_put_api():
    response=requests.put(endpoint,json=payload)
    assert response.status_code==200
    response_json=response.json()
    print(response_json)
    assert 'morpheus' in response_json ["name"],"name is missing"
    assert 'zion resident' in response_json ["job"] , "job is missing"


