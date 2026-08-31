import requests, json

def getApiData(url, opHeader=None):
    headers = {"Content-Type" : "application/json"}
    headers = (headers|opHeader) if isinstance(opHeader, dict) else headers
    response = requests.get(url, verify=False, headers=opHeader)
    return response