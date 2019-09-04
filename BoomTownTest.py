import requests
import json

url = "https://api.github.com/orgs/boomtownroi"
string = "api.github.com/orgs/BoomTownROI"

response = requests.get(url)

body = json.loads(response.content)

for key in body:
    value = body[key]
    if str(value).find(string) != -1:
        response = requests.get(value)
        if response.status_code == 200: 
            print(response.content) 
            break