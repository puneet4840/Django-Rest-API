import requests
import json

URL="http://127.0.0.1:8000/stu/"

def read_data():
    r=requests.get(url=URL)
    data=r.json()
    print(data)

def create_data():
    data={'name':'Rohit','roll':103,'city':'Delhi'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

def update_data():
    data={'id':1,'name':'Puneet','roll':101,'city':'Gurgaon'}
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

def delete_data():
    data={'id':3}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

# read_data()
create_data()
# update_data()
# delete_data()