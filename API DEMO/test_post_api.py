from http.client import responses

import requests
import pytest
import json


payload={
    "name": "Arnob",
    "job": "tester"
}
##
endpoint="https://reqres.in/api/users"
def test_post_api():
    response =requests.post(endpoint,json=payload)
    assert response.status_code == 201,"response code is not 201 test failed"
    assert response.json() ["name"]=="Arnob"
    print(response.json())
