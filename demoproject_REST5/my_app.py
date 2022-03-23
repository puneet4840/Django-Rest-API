import requests
import json

URL="http://127.0.0.1:8000/stu/"


def read():
    r=requests.get(url=URL)
    data=r.json()
    print(data)

def create():
    data={
        'name':'Dev',
        'roll':103,
        'city':'Narora'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

def update():
    data={
        'id':1,
        'name':'Akhil',
        'city':'Jaipur'
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)


def delete():
    data={
        'id':1
    }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

# read()
create()
# update()
# delete()