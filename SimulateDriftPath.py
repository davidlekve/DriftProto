# %%
import asyncio
from opendrift.models.leeway import Leeway
from opendrift.readers import reader_netCDF_CF_generic
from opendrift.readers import reader_global_landmask
from opendrift.readers import reader_global_landmask

async def simulateDriftPath(listOfElements, dateTime, objectType):
    
    # Model used for simulation
    simulationModel = Leeway(loglevel=50) 

    # Add readers for weather and ocean data, and for landmask
    reader_norkyst = reader_netCDF_CF_generic.Reader(
        'https://thredds.met.no/thredds/dodsC/sea/norkyst800m/1h/aggregate_be')
    reader_landmask = reader_global_landmask.Reader()
    simulationModel.add_reader([reader_landmask, reader_norkyst])

    # Seed elements that should be simulated
    for element in listOfElements:
        simulationModel.seed_elements(element.__getattribute__("lon"),
                                        lat=element.__getattribute__("lat"),
                                        object_type=objectType,
                                        time=dateTime)

    # Run simulation
    simulationModel.run()    
    
    # Returning the whetherdata (history) and the timearray from the simulation
    return([simulationModel.history, simulationModel.get_time_array()])

    


    



 