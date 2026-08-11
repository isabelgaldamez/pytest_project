import requests

# url = 'https://www.google.com/search?q=pytest'
# response = requests.get(url)
# print(response.text)

url = 'https://httpbin.org/get'
r = requests.get(url)
print(r.status_code)
print(r.headers)
print(r.request.headers)
print(r.text)
print(r.json())
print(r.headers['Content-Type'])
print('==================')

URL = 'https://httpbin.org/get'
myparams = {'key1' : 'value1', 'key2' : 'value2'}
r = requests.get(URL,params=myparams)
print(r.url)

for key, value in r.json().items():
    print(key, ":", value)

print(r.json()["headers"]["Host"])

print('========POST=========')
post_url = 'https://httpbin.org/post'
payload = {'key1':'value1', 'key2':'value2'}
post_response = requests.post(post_url, json=payload)
print(post_response.url)
print(post_response.status_code)
print(post_response.text)

print('========POST custom header=========')
post_url = 'https://httpbin.org/post'
payload = {'key1':'value1', 'key2':'value2'}
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
post_response = requests.post(post_url, json=payload, headers=headers)
print(post_response.url)
print(post_response.status_code)
print(post_response.text)
print(post_response.request.headers)
print(post_response.headers)
