import requests
import pytest
import json


end_point="https://reqres.in/api/users/2"

def test_getAPI():
    response= requests.get(end_point)
    assert response.status_code==200
    #print(response.text)
    print(response.json())
    json_response=response.json()
    # test email field value
    assert 'email' in  json_response['data'],"email is missing"
    assert json_response ['data']['email'] == 'janet.weaver@reqres.in' ,'value is missing'



