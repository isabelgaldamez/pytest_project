from utils.apiUtils import postApiData, patchApiData
from utils.fileUtils import getJsonFromFile, update_user_info
from utils.myconfigparser import getFlaskAppBaseURL

baseURL = getFlaskAppBaseURL()
urlPath = 'register'
getUser = 'users?id='
registerJsonFile = 'registerApiValid.json' # file name where we have the body for the POST request
updatedInfoFile = 'user_info.json'
#Testing register API with body from json file
def test_registerAPI():
    url = baseURL + urlPath
    payload = getJsonFromFile(registerJsonFile)
    resp = postApiData(url, payload)
    print(resp.json())
    assert resp.status_code == 201

def test_updateuserInfo():
    url = baseURL + getUser + "5"
    payload = update_user_info(updatedInfoFile)
    print(url)
    resp = patchApiData(url, payload)
    print(resp.status_code)


