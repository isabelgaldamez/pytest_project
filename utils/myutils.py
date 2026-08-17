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

