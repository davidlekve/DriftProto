import asyncio
from opendrift.elements import LagrangianArray
from datetime import datetime
from SimulateDriftPath import simulateDriftPath
from FilterElementData import handleDataFromHistory
from ConvertFilteredElementToJson import convertToJSON

# Dummydata for development. These need to be replaced in a function
# when real data are retrieved from api.
element1 = LagrangianArray(lon = 4.1, lat = 60.5)
element2 = LagrangianArray(lon = 6.0, lat = 61.0)
allElements = [element1, element2]
time = datetime(2023,2,21,15,0,0)


# Async function that deals with timing and ordering of simulation, 
# filtering the data and converting the data to JSON. 
async def handlePredictDriftPath(listOfElements, time):

    async with asyncio.TaskGroup() as tg:
        simulate_task = tg.create_task(
            simulateDriftPath(listOfElements, time, 74)
        )
        await simulate_task
        historyData = simulate_task.result()[0]
        timeData = simulate_task.result()[1]

        filter_task = tg.create_task(
            handleDataFromHistory(historyData,timeData)
        )
        await filter_task
        filteredData = filter_task.result()

        convert_task = tg.create_task(
            convertToJSON(filteredData)
        )
        await convert_task
        jsonData = convert_task.result()
        
        print(jsonData)
        return jsonData
        
loop = asyncio.get_event_loop()
loop.run_until_complete(handlePredictDriftPath(allElements, time))