from utils.apiUtils import getApiData
from utils.myconfigparser import getFlaskAppBaseURL
import pytest

baseURL = getFlaskAppBaseURL()
urlPath = 'allusercount'

# Test Data should be a list of tuples
testData = [
    ('application/json', 200),
    ('application/xml', 406),
    ('application/mixed', 406),
    ('text/html', 200),
]

# This test will run 4 times, once for each testData
@pytest.mark.parametrize("type, status", testData)
def test_getAllUserCountStatus(type, status):
    url = baseURL + urlPath
    headers = {'Accept': type}
    resp = getApiData(url, headers)
    print(resp.status_code)
    assert resp.status_code == status
