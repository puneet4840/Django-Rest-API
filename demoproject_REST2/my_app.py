import requests
import json

URL="http://127.0.0.1:8000/stu_create/"

data={'name':'Ram','roll':102,'city':'Delhi'}
json_data=json.dumps(data)

r=requests.post(url=URL,data=json_data)
data=r.json()
print(data)