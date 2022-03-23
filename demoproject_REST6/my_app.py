import requests
import json

URL="http://127.0.0.1:8000/stu/"

def read(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=data)
    data=r.json()
    print(data)


def create():
    data={'name':'Arun','roll':104,'city':'Chennai'}
    json_data=json.dumps(data)
    headers={'Content-Type':'application/json'}
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

def update():
    data={'id':1,'name':'Rohit','roll':102,'city':'Jaipur'}
    json_data=json.dumps(data)
    headers={'Content-Type':'application/json'}
    r=requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

def delete():
    data={'id':1}
    json_data=json.dumps(data)
    headers={'Content-Type':'application/json'}
    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)


read()
# create()
# update()
# delete()