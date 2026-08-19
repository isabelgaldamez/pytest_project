import requests, json

# GET API call and returns response data
def getAPIData(url):
    headers = {'Content-Type': 'application/json'}
    print('RequestURL : ', url)
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()
    assert len(data) > 0, 'Empty GET response'
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken

def postAPIData(url, body):
    headers = {'Content-Type': 'application/json'}
    print('RequestURL : ', url)
    response = requests.post(url, json=body, verify=False, headers=headers)
    data = response.json()
    return data, response.status_code




#PUT api call
def putAPIData(url, body):
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    # print('RequestURL : ', url)
    # print("Req", json.dumps(body))

    # response = requests.put(url, verify=False, data=json.dumps(body), headers=headers)
    response = requests.put(url, verify=False, json=body, headers=headers)


    data = response.json()

    return data, response.status_code

#Delete record, API call
# The delete API has an optional 'APIkey' in header
def deletePetAPI(url, opHeader=None):
    headers = {'Content-Type': 'application/json' }
    # print('RequestURL : ', url)

    # In case the apiKey is given, then use it else pass just contentType
    # if opHeader is a dictionary then pass into headers
    headers = (headers | opHeader) if isinstance(opHeader, dict) else headers
    response = requests.delete(url, verify=False, headers=headers)
    print(response.request.headers)
    data = response.json()
    return data, response.status_code




