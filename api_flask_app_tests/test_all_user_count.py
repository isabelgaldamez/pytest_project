from utils.apiUtils import getApiData
from utils.myconfigparser import getFlaskAppBaseURL

baseURL = getFlaskAppBaseURL()
urlPath = 'allusercount'

# Testing endpoint /allusercount
def test_getAllUserCountStatus200():
    url = baseURL + urlPath
    headers = {'accept':'application/json'}
    data = getApiData(url, headers)
    assert data.status_code==200

def test_getAllUserCountStatus406():
    url = baseURL + urlPath
    data = getApiData(url)
    assert data.status_code==406

def test_getAllUserCountBody():
    url = baseURL + urlPath
    headers = {'Accept' : 'application/json'}
    resp = getApiData(url, headers)
    data = resp.json()
    assert data['count'] #asserts the object returned has the ket 'count'
    assert data['status']
    assert data['status']['message'] == 'success'

def test_getAllUserCountTimeTaken():
    url = baseURL + urlPath
    headers = {'Accept': 'application/json'}
    resp = getApiData(url, headers)
    print(resp.elapsed.total_seconds())
    assert resp.elapsed.total_seconds() < 1 # takes less than a second to run

