import pytest

from utils.fileUtils import getCsvDataAsDict, getDataAsTuple
from utils.apiUtils import postApiData
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
dataFile = 'registerApiData.csv'
dataFileWithStatus = 'registerApiDataWithStatus.csv'
urlPath = 'register'

#Datadriven test from datafile, inserting all data in single test
def test_dataDrivenRegApi():
    url = baseURI + urlPath
    payloadList = getCsvDataAsDict(dataFile)
    for dataLines in payloadList:
        print(dataLines)
        resp = postApiData(url, dataLines)
        assert resp.status_code == 201
        data = resp.json()
        print(data)
        assert data['id']

#datadriven test from datafile, uses Pytest parameterization,
# it will generate separate test for each row in datafile
getData = getDataAsTuple(dataFileWithStatus) #get data first, it contains all the datasets
@pytest.mark.parametrize("input,respStatus", getData)
def test_dataDrivenParametrized(input, respStatus):
    url = baseURI + urlPath
    keys = ['email', 'password']
    reqDict = dict(zip(keys, input))
    # print('Req Dic : ',reqDict, respStatus)
    resp = postApiData(url, reqDict)
    assert resp.status_code == int(respStatus)
