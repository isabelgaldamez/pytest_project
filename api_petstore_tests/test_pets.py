from utils.myutils import getAPIData

base_URI = 'https://petstore.swagger.io/v2/pet/'
petId = '6'

def test_getPetById():
    url = base_URI + petId
    data, res_status, timeTaken = getAPIData(url)
    assert len(data) > 0, 'empty response'
    assert (data['id'] == int(petId)), 'ID not found'
    assert res_status == 200
    print(timeTaken)
    assert (data['category']['name']) == 'Siyah', 'No name has been assigned'

