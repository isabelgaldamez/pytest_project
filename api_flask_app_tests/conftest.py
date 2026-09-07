import json

import pytest

from utils.fileUtils import getJsonFromFile
from utils.apiUtils import postApiData, getApiData
from utils.myconfigparser import getFlaskAppBaseURL
import pytest

loginJsonFile = 'loginValid.json'
baseURI = getFlaskAppBaseURL()
loginURLPath = 'login'
userURLPath = 'users' # gets all users from the system
oneUserURLPath = 'users?id=4'
@pytest.fixture
def get_token():
    loginURL = baseURI + loginURLPath
    payload = getJsonFromFile(loginJsonFile)
    resp = postApiData(loginURL, payload)
    # token = resp.json()['token']
    # print(resp.json()['token'])
    token = resp.json()['token']
    yield token