import json 

# __________________________________________________________________________________________
# This model is meant to retrieve data, filter the unrelevant data, sort data by
# elementId and time, then produce a JSON object ready to be sent to API.
# __________________________________________________________________________________________

# Class to create a dictionary consisting of several FloatingDataPerTime
# dictionaries. These objects/dicts are used to produce the "master" - dictionary 
# in createFloatingVariableDictionary.
class FloatingDataPerId:
    def __init__(self, id):
        self.id = int(id)
        self.dict = {}
        self.dict["id"] = self.id

    def addToDictionary(self, key, value):
        self.dict[str(key)] = value

# Class to create a dictionary per timeDate. These objects are
# insertet into FloatingDataPerId.
class FloatingDataPerDateTime:

    def __init__(self, dateTime, status, moving, ageInSeconds, longitude, latitude):
        self.dateTime = str(dateTime)
        self.status = int(status)
        self.moving = int(moving)
        self.ageInSeconds =float(ageInSeconds)
        self.longitude = float(longitude)
        self.latitude = float(latitude)
        self.dict = {"dateTime" : self.dateTime,
                "status" : self.status,
                "moving" : self.moving,
                "ageInSeconds" : self.ageInSeconds,
                "longitude" : self.longitude,
                "latitude" : self.latitude}
    def getFloatingVariablesDictionary(self):
        return self.dict
    
class FloatingDataMaster:
    def __init__(self):
        self.dict = {}
    def addToDctionary(self, key, value):
        self.dict[str(key)] = value
    def getMasterDictionary(self, key):
        return self.dict.get(key)


# Method to retrieve a filtered data from a dataset of the format of o.history from
# containerDriv (See .md-ile to view format). Returns a python dictionary consisting of
# the specified data from the time set in containerDriv.
def handleDataFromHistory(wetherData, timeData):
    objectMaster = FloatingDataMaster()
    masterList = []

    for ArrayPerId in wetherData:
        initialDateTimeNumber = 0
        objectPerId = FloatingDataPerId(ArrayPerId[initialDateTimeNumber][0])
        listPerDateTime = []
        for ArrayOfVariables in ArrayPerId[slice(0,2)]: #Slice is only ment for development to avoid retreiving massive sets of data
            objectPerDateTime = FloatingDataPerDateTime(timeData[0][initialDateTimeNumber], # format: yyyy-mm-dd hh:mm:ss
                                            ArrayOfVariables[1],
                                            ArrayOfVariables[2],
                                            ArrayOfVariables[3],
                                            ArrayOfVariables[5],
                                            ArrayOfVariables[6])
            listPerDateTime.append(objectPerDateTime.getFloatingVariablesDictionary())
            initialDateTimeNumber +=1
        objectPerId.addToDictionary("listOfVariablesPerDateTime", listPerDateTime) 
        masterList.append(objectPerId.dict)
    objectMaster.addToDctionary("masterData", masterList)
    return objectMaster.getMasterDictionary("masterData")

# Method to convert a python dictionary/object to JSON
def convertToJSON(pythonDictionary):
    jsonObject = json.dumps(pythonDictionary)
    return jsonObject