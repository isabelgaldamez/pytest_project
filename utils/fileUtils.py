# Here are all the data that will be reading from a file
import csv
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

#function to read data from file
def getCsvDataAsDict(filename):
    filePath = TEST_DATA_DIR.joinpath(filename)
    with open(filePath, 'r') as file:
        csvFile = csv.DictReader(file)
        dictList = list(csvFile)
    return dictList

#function to read data from the csv opened file as a Listt
def getCsvDataAsList(filename):
    filePath = TEST_DATA_DIR.joinpath(filename)
    with open(filePath, 'r') as csvFile:
        csvFileReader = csv.reader(csvFile)
        next(csvFileReader) #skip the first lines which are the column names
        lines = list(csvFileReader)
    return lines

#return a List of Tuples, within Tuples its 'list of inputs' and a scalar value for output-status
def getDataAsTuple(filename):
    dataList = getCsvDataAsList(filename)
    newlist= []
    for lines in dataList:
        newlist.append((lines[:2], lines[2])) #append(()) put a tuple inside the list,

    # To replace the prev 3 lines of code, you can write it into a single line
    # syntax: of List Comprenhension
    # [expression(element) for element in oldList if condition]
    # newList2 = [(x[:2],x[2]) for x in dataList]
    return newlist

# We can create a dict with a list of zipped keys and values
# keys = ['a', 'b', 'c', 'd']
# values = ['alpha', 'beta', 'delta']
# d = dict(zip(keys, values))
# print(d)
# print(getCsvDataAsDict('registerApiData.csv'))
#
# print(getCsvDataAsList('registerApiDataWithStatus.csv'))