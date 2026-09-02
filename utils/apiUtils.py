import requests, json

def getApiData(url, opHeader=None):
    headers = {"Content-Type" : "application/json"}
    headers = (headers|opHeader) if isinstance(opHeader, dict) else headers
    response = requests.get(url, verify=False, headers=opHeader)
    return response

def postApiData(url, body):
    headers = {"Content-Type" : "application/json"}
    print('\nReqURL: ' + url)
    print('\nReqBody: ' + json.dumps(body))
    return requests.post(url, verify=False, headers = headers, json = body)

def patchApiData(url, payload):
    headers = {"Content-Type": "application/json"}
    return requests.put(url, verify=False, headers=headers, json=payload)


