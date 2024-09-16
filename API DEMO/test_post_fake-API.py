import requests
import json


endpoint="https://fakerestapi.azurewebsites.net/api/v1/Activities"

payload={
  "id": 150,
  "title": "Arnob",
  "dueDate": "2024-09-16T01:22:15.988Z",
  "completed": True
}

def test_post_fakeAPI():
    response=requests.post(endpoint,json=payload)
    response_capture_in_json=response.json()
    print(response_capture_in_json)
    # print based on JSON data
    print(response_capture_in_json["id"])
    print(response_capture_in_json["title"])
    print(response_capture_in_json['dueDate'])
    print(response_capture_in_json['completed'])
    # example test assertion

    assert response_capture_in_json["id"]==150 ,"test case failed"
    assert response_capture_in_json["title"]=="Arnob","test case failed"





