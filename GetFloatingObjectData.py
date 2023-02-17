import json 

# This model is meant to retrieve data, filter the unrelevant data, sort data by
# elementId and time, then produce a JSON object ready to be sent to API.

# Class to create a dictionary consisting of several FloatingDataPerTime
# dictionaries. These objects/dicts are used to produce the "master" - dictionary 
# in createFloatingVariableDictionary.
class FloatingDataPerId:
    def __init__(self, id):
        self.id = int(id)
        self.dict = {}
        self.dict["id"] = self.id

    def addToDictionary(self, key, listOfVariables):
        self.dict[str(key)] = listOfVariables

# Class to create a dictionary per timeDate. These objects are
# insertet into FloatingDataPerId.
class FloatingDataPerTime:

    def __init__(self, dateTime, status, moving, ageInSeconds, longitude, latitude):
        self.dateTime = str(dateTime)
        self.status = int(status)
        self.moving = int(moving)
        self.ageInSeconds =float(ageInSeconds)
        self.longitude = float(longitude)
        self.latitude = float(latitude)

    def createFloatingVariablesDictionary(self):
        dict = {"dateTime" : self.dateTime,
                "status" : self.status,
                "moving" : self.moving,
                "ageInSeconds" : self.ageInSeconds,
                "longitude" : self.longitude,
                "latitude" : self.latitude}
        return dict

# Method to retrieve a filtered data from a dataset of the format of o.history from
# containerDriv (See .md-ile to view format). Returns a python dictionary consisting of
# the specified data from the time set in containerDriv.
def handleDataFromHistory(wetherData, timeData):
    masterDict = {}
    masterList = []

    for ArrayPerId in wetherData:
        startDateTimeNumber = 0
        dictPerId = FloatingDataPerId(ArrayPerId[startDateTimeNumber][0])
        listOfDifferentDateTime = []
        
        for ArrayOfVariables in ArrayPerId[slice(0,2)]: #Slice er kun med for å ikke ha med all dataen
            variables = FloatingDataPerTime(timeData[0][startDateTimeNumber], #yyyy-mm-dd hh:mm:ss
                                            ArrayOfVariables[1],
                                            ArrayOfVariables[2],
                                            ArrayOfVariables[3],
                                            ArrayOfVariables[5],
                                            ArrayOfVariables[6])
            listOfDifferentDateTime.append(variables.createFloatingVariablesDictionary())
            startDateTimeNumber +=1
    
        dictPerId.addToDictionary("listOfVariablesPerDateTime", listOfDifferentDateTime) 
        masterList.append(dictPerId.dict)
  
    masterDict["allData"] = masterList
    return masterDict.get("allData")

# Method to convert a python dictionary/object to JSON
def convertToJSON(pythonObject):
    jsonObject = json.dumps(pythonObject)
    return jsonObject