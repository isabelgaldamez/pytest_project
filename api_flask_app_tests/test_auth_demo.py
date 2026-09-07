from utils.fileUtils import getJsonFromFile
from utils.apiUtils import postApiData, getApiData
from utils.myconfigparser import getFlaskAppBaseURL

loginJsonFile = 'loginValid.json'
baseURI = getFlaskAppBaseURL()
loginURLPath = 'login'
userURLPath = 'users' # gets all users from the system
oneUserURLPath = 'users?id=4'

#demo test with token
def test_getUsersDemo():
    # To do:
    #   * Login with an existing user to get the token
    #   * Extract the token from the response and use it in the header for  api/users
    #   * Make a GET request for the /users api to get all users in the system
    loginURL = baseURI + loginURLPath
    payload = getJsonFromFile(loginJsonFile)
    resp = postApiData(loginURL, payload)
    print(resp.json())
    token = resp.json()['token']
    usersURL = baseURI + userURLPath
    headers = {"x-access-token": token}
    userResp = getApiData(usersURL, headers)
    print(userResp.json())


def test_getSingleUserDemo():
    loginURL = baseURI + loginURLPath
    payload = getJsonFromFile(loginJsonFile)
    resp = postApiData(loginURL, payload)
    print(resp.json())
    token = resp.json()['token']
    usersURL = baseURI + oneUserURLPath
    headers = {"x-access-token": token}
    userResp = getApiData(usersURL, headers)
    print(userResp.json())