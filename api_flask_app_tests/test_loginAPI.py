import random

import pytest
from utils.apiUtils import postApiData, deleteApiData
from utils.fileUtils import getJsonFromFile
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
regUrlPath = 'register'
loginUrlPath = 'login'
delUrlPath = 'delete'
registerJsonFile = 'registerApiValid.json'
randNum = random.randint(0, 1000)
user_email = 'automateUser@auto'+str(randNum)
user_password = '1234'

@pytest.fixture(scope='module')
def reg_user():
    print('SETUP')
    payload = getPayloadDic_RegisterAPI(user_email, user_password)
    regUrl = baseURI + regUrlPath
    regResponse = postApiData(regUrl, payload)
    assert regResponse.status_code == 201
    assert regResponse.json()['id']
    data = regResponse.json()
    yield data  # Anything after this yield statement will run after the test is executed or as part of teardown, yield data will return the response, and this data can be used in the tests
    print('TEARDOWN')
    delUrl = baseURI + delUrlPath
    loginUrl = baseURI + loginUrlPath # we need the access token to use it in delete, we will login to get it
    login_resp = postApiData(loginUrl, payload)
    token = login_resp.json()['token']
    payload = {"id" : regResponse.json()['id']} #Delete accepts userId, to know which record to delete
    headers = {'x-access-token' : token}
    del_resp = deleteApiData(delUrl, payload, headers)
    assert del_resp.status_code == 200
    assert del_resp.json()['id'] == regResponse.json()['id'] #verify is the same id created and deleted


# Pass the fixture name in the test argument, that will be called when test runs
def test_loginCorrectCredentials(reg_user):
    payload = getPayloadDic_RegisterAPI(user_email, user_password) # Gets the payload for the login request
    url = baseURI + loginUrlPath
    resp = postApiData(url, payload)
    assert resp.status_code == 200

# Existing user but provides an empty password
def test_loginEmptyPassword(reg_user):
    payload = getPayloadDic_RegisterAPI(user_email, '')
    url = baseURI+loginUrlPath
    resp = postApiData(url, payload)
    assert resp.status_code == 401

# Utils function for changing email/password, this will be used in register api
def getPayloadDic_RegisterAPI(email=None, pwd=None):
    payload = getJsonFromFile(registerJsonFile)
    payload['email'] = email
    payload['password'] = pwd
    return payload