import json

dataDict = {
    "sampleString": "Great Automation Framework",
    "sampleList": ["Good", "Better", "Best"],
    "sampleTuple": ("Python", "Pytest", "Automation"),
    "sampleObject": {"platform": "Udemy", "Valuable": True},
    "sampleInteger": 555,
    "booleanValue": True,
    "noneValue": None
}
print("Convert python dictionary to JSON")
resultJSON = json.dumps(dataDict, sort_keys=True, indent=4) # converts a dictionary to JSON
print(resultJSON)
print(type(resultJSON) == str)

# ====== DESIRIALIZATION ======
print("====== DESIRIALIZATION ======")
data_dict = json.loads(resultJSON) # converts a JSON into a dictionary
print(data_dict)
print(type(data_dict))

with open("example.json", 'r') as file:
    data = json.load(file)
    print(data)
    print(type(data))
    print(data.keys())
    print(data['address'])

    # traverse the dictionary
    for key, value in data.items():
        print(key , ':', value )

def validateJSON(jsonStr):
    try:
        json.loads(jsonStr)
    except ValueError as err:
        return False
    return True

JsonStr = """{"name": "Benjamin", "salary": 2500, "email": "benji@myemail.com"}"""
isValid = validateJSON(JsonStr)
print("JSON string is valid? ",isValid )