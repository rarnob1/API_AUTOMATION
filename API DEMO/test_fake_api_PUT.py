from http.client import responses

import requests
import json

endpoint="https://fakerestapi.azurewebsites.net/api/v1/Activities/3"

payload={
  "id": 1289,
  "title": "Arnob",
  "dueDate": "2024-09-16T02:12:45.536Z",
  "completed": True
}

header={
"accept": "text/plain",
"Content-Type" : "application/json"
}
response=requests.put(endpoint,json=payload,headers=header)

def test_put_fakeAPI():
    #response=requests.put(endpoint,json=payload,headers=header)
    print(response.json())

def test_name_assertion():
    #response = requests.put(endpoint, json=payload, headers=header)
    assert response.json() ["title"]=="Arnob"

def test_ID_assertion():
    #response = requests.put(endpoint, json=payload, headers=header)
    assert response.json() ["id"]==1289