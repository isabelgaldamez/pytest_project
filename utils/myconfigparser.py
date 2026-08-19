import configparser
from pathlib import Path

configFile = 'petsqa.ini' #ini file
configFileDir='config' #directory name

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
# (__file__) refers to this current file 'myconfigparser.py'
# resolve() and then go to parent folder, we need to reach config folder
print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(configFileDir).joinpath(configFile)
config.read(CONFIG_FILE)

#Now that we have the variable config, we will be able to read the info from the .ini file
def getPetAPIURL():
    return config['pet']['url']

def getStoreAPIURL():
    return config['store']['url']

print(getPetAPIURL())
