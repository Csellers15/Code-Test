import requests
import json

url = "https://api.github.com/orgs/boomtownroi"
string = "api.github.com/orgs/BoomTownROI"

def main():
    response = requests.get(url)

    body = json.loads(response.content)

    for key in body:
        value = body[key]
        if str(value).find(string) != -1:
            response = requests.get(value)
            if response.status_code == 200: 
                page = json.loads(response.content)
                checkForID(page)
        else:
            print("whoops")

def checkForID(jsonlist):
    for i in jsonlist:
        print('here')
        if i == "id":
            print(i + ':' + str(jsonlist[i]))
        elif isinstance(i, dict):
            #for j in i:
                #if j == "id":
                #    print(j + ':' +str(i[j]))
            checkForID(i)


if __name__ == '__main__':
    main()

