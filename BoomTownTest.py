import requests
import json

url = "https://api.github.com/orgs/boomtownroi"
substring = "api.github.com/orgs/BoomTownROI"

def main():
    response = requests.get(url)

    body = json.loads(response.content)

    for key in body:
        value = body[key]
        if str(value).find(substring) != -1:
            response = requests.get(value)
            if response.status_code == 200: 
                page = json.loads(response.content)
                checkForID(page)
            else: 
                print("error page does not exist")
    if 


def checkForID(page):
    if isinstance(page, dict):
        for k,v in page.items():
            if isinstance(v, (dict,list)):
                checkForID(v)
            elif k == "id":
                print(k +" : " + str(v))
    elif isinstance(page, list):
        for i in page: 
            checkForID(i)
            



if __name__ == '__main__':
    main()