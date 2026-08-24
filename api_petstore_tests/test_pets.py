from utils.myconfigparser import *

import utils.myutils as apiReq
# from utils.myutils import getAPIData, postAPIData, putAPIData, deletePetAPI
import logging
logger = logging.getLogger(__name__)

# base_URI = 'https://petstore.swagger.io/v2/pet/'
base_URI = getPetAPIURL()
petId = '51'
payloadPost = {
        'id': int(petId),
        "category": {
            "id": int(petId),
            "name": "Terrier"
        },
        "name": "Sasha",
        "photoUrls": [
            "https://breed-assets.wisdompanel.com/dog/american-staffordshire-terrier/American_Staffordshire_Terrier1.jpg"
        ],
        "status": "available"
    }

payloadPut = {
      "id": int(petId),
      "category": {
        "id": int(petId),
        "name": "Husky"
      },
      "name": "Blue",
      "photoUrls": [
        "https://www.pinterest.com/pin/682999099726074401/"
      ],
      "tags": [
        {
          "id": int(petId),
          "name": "string"
        }
      ],
      "status": "pending"
    }

def test_getPetById():
    url = base_URI + petId
    data, res_status, timeTaken = apiReq.getAPIData(url)
    assert len(data) > 0, 'empty response'
    assert (data['id'] == int(petId)), 'ID not found'
    assert res_status == 200
    print(timeTaken)
    # assert (data['name']) == 'Sasha', 'No name has been assigned'

def test_postPet():
    logger.info('POST request')
    url = base_URI
    data, res_status = apiReq.postAPIData(url, payloadPost)
    assert len(data) > 0, 'empty response'
    assert res_status == 200


# PUT updates and completly replace an excisting resorce, or creates a new resource at a specific known URL
def test_updatePet():
    url = base_URI
    data, status_code = apiReq.putAPIData(url, payloadPut)
    assert status_code == 200
    assert data['category']['name'] == 'Husky'
    assert data['name'] == 'Blue'
    print(data)

def test_deletePet():
    url = base_URI + petId
    apiKey = {'api_key': 'key1'}
    data, status_code = apiReq.deletePetAPI(url, apiKey)
    assert status_code == 200
    assert data['code'] == 200
    assert data['message'] == '51'
