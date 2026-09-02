# Here are all the data that will be reading from a file
import json
from pathlib import Path # we need to read from a specific file

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
TEST_DATA_DIR = BASE_DIR.joinpath('TestData')

def getJsonFromFile(filename):
    filePath = TEST_DATA_DIR.joinpath(filename)
    with open(filePath, 'r') as file:
        return json.load(file) #json.load() reading from the file directly and json.loads() if you want to read from a python string

def update_user_info(filename):
    filePath = TEST_DATA_DIR.joinpath(filename)
    with open(filePath, 'r') as file:
        return json.load(file)