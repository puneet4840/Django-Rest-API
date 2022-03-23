import requests
import json

URL="http://127.0.0.1:8000/api/stu/ Authorization:Token 62f81224a17a016757bb132c14c2b4b23e3abd65/"

def read_data():
    r=requests.get(url=URL)
    data=r.json()
    print(data)

def create_data():
    data={'name':'Rohan','roll':111,'city':'Noida'}
    # json_data=json.dumps(data)
    r=requests.post(url=URL,data=data)
    data=r.json()
    print(data)

def update_data():
    data={'id':1,'name':'Puneet','roll':101,'city':'Gurgaon'}
    # json_data=json.dumps(data)
    r=requests.put(url=URL,data=data)
    data=r.json()
    print(data)

def delete_data():
    data={'id':5}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

# read_data()
create_data()
# update_data()
# delete_data()