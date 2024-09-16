import requests
import pytest
import json

URL="https://gorest.co.in/public/v2/users"

parameter={
    'page':1,
    'per_page':20
}

def test_get_user_by_param():
    response=requests.get(URL,params=parameter)
    print(response.json())
