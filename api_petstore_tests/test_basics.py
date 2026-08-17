import requests
import json

base_URI = 'https://petstore.swagger.io/v2/pet/'
petId = '6'
headers = {'Content-Type': 'application/json'}

# test GET valid response
# def test_getPetById_response():
    # url = base_URI + petId
    # response = requests.get(url, verify=False, headers=headers)
    # data = response.json()
    # print(json.dumps(data, indent=3))
    # assert len(data) > 0, 'empty response'
    # assert (data['category']['name']) == 'Siyah', 'No name has been assigned'

#Test response body
def test_getPetById_id():
    url = base_URI + petId
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()

    assert data['id'] == 6

# Add a new pet to the store
def test_addNewPet():
    url = base_URI
    headers = {'Content-Type': 'application/json; ; charset=UTF-8'}
    payload = {
        'id': 51,
        "category": {
            "id": 51,
            "name": "Terrier"
        },
        "name": "Sasha",
        "photoUrls": [
            "https://breed-assets.wisdompanel.com/dog/american-staffordshire-terrier/American_Staffordshire_Terrier1.jpg"
        ],
        "status": "available"
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    assert response.status_code == 200, 'There was an error in the post request'
    assert data['id'] == 51, 'record was not created'
    assert len(data) > 0
    print(data)



