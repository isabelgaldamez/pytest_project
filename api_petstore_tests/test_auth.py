import requests
from requests.auth import HTTPDigestAuth, HTTPBasicAuth
url = "https://httpbin.org/digest-auth/auth/isa/123/MD5"
auth = HTTPDigestAuth('isa', '123')

def test_basicAuth():
    # use the 'auth' parameter to send the requests with HTTP Basic Auth
    headers = {'Accept' : 'application/json'}
    r = requests.get(url, auth=auth, verify=False)
    print(r.status_code)