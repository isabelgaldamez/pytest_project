import json

import pytest

from utils.fileUtils import getJsonFromFile
from utils.apiUtils import postApiData, getApiData
from utils.myconfigparser import getFlaskAppBaseURL


# loginJsonFile = 'loginValid.json'
baseURI = getFlaskAppBaseURL()
# loginURLPath = 'login'
userURLPath = 'users' # gets all users from the system
oneUserURLPath = 'users?id=4'

# write the fixture that will get the token for us
# we do not need to write this code for every single test that needs a token
# @pytest.fixture
# def get_token():
#     loginURL = baseURI + loginURLPath
#     payload = getJsonFromFile(loginJsonFile)
#     resp = postApiData(loginURL, payload)
#     # token = resp.json()['token']
#     # print(resp.json()['token'])
#     token = resp.json()['token']
#     yield token

# test get users with fixtures, pass the fixture as an argument
def test_getUsers(get_token):
    token = get_token
    userURL = baseURI + userURLPath
    headers = {'x-access-token': token}
    resp_users = getApiData(userURL, headers)
    print(json.dumps(resp_users.json(), indent=4))
    assert resp_users.json()['users'][0]['email'] is not ""

def test_getSingleUserDemo(get_token):
    usersURL = baseURI + oneUserURLPath
    headers = {"x-access-token": get_token}
    userResp = getApiData(usersURL, headers)
    print(json.dumps(userResp.json(), indent=4))


