import requests
import pytest
import json

endpoint="https://gorest.co.in/public/v2/users/6940785"



header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 888c20c8dc5aee573c561bdcab5cbc67cd29fb1853c6a11feff1c6ff1a4447da"
}
def test_auth():
    response=requests.get(endpoint,headers=header)
    print(response.json())
    response.status_code == 200



