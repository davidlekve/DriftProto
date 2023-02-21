# __________________________________________________________________________________________
# This model is meant to retrieve data, filter the unrelevant data, sort data by
# elementId and time.
# __________________________________________________________________________________________

import numpy

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
    def __init__(self, dateTime, status, moving, longitude, latitude):
        self.dateTime = str(dateTime)
        self.status = int(status)
        self.moving = int(moving)
        self.longitude = float(longitude)
        self.latitude = float(latitude)
        self.dict = {"dateTime" : self.dateTime,
                "status" : self.status,
                "moving" : self.moving,
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
# the specified data from the time set in HanslePredictDriftPath.
async def handleDataFromHistory(wetherData, timeData):
    objectMaster = FloatingDataMaster()
    masterList = []

    for ArrayPerId in wetherData:
        initialDateTimeNumber = 0
        objectPerId = FloatingDataPerId(ArrayPerId[initialDateTimeNumber][0])
        listPerDateTime = []
        for ArrayOfVariables in ArrayPerId[slice(len(ArrayPerId))]:
            # This is to check if the element is stranded. If that is the case, there is only empty data that is returned and no need to continue loop.
            if type(ArrayOfVariables[1]) == numpy.ma.core.MaskedConstant:
                break
            objectPerDateTime = FloatingDataPerDateTime(timeData[0][initialDateTimeNumber], # format: yyyy-mm-dd hh:mm:ss
                                            ArrayOfVariables[1],
                                            ArrayOfVariables[2],
                                            ArrayOfVariables[5],
                                            ArrayOfVariables[6])
            listPerDateTime.append(objectPerDateTime.getFloatingVariablesDictionary())
            initialDateTimeNumber +=1
        objectPerId.addToDictionary("listOfVariablesPerDateTime", listPerDateTime) 
        masterList.append(objectPerId.dict)
    objectMaster.addToDctionary("masterData", masterList)
    return objectMaster.getMasterDictionary("masterData")

