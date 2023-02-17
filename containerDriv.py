# %%
from opendrift.models.leeway import Leeway
from opendrift.readers import reader_netCDF_CF_generic
from opendrift.readers import reader_global_landmask
from pprint import pprint

# %% [markdown]
# Det finnes mange modeller i opendrift. Her har eg brukt leeway (avdrift) siden det har egen type objekt for containere.
# Mer info om leeway her https://opendrift.github.io/autoapi/opendrift/models/leeway/index.html#module-opendrift.models.leeway

# %%
o = Leeway(loglevel=50) #Loglevel er kor mye som ska printes ut i konsollen. 0 er alt 50 er ingenting
""" print(o) """

# %%
""" pprint(Leeway.required_variables) """

# %% [markdown]
# Printene over viser ting som må vær med for at modellen ska fungere. Man får tak i disse gjennom en "reader". 

# %%
reader_norkyst = reader_netCDF_CF_generic.Reader(
    'https://thredds.met.no/thredds/dodsC/sea/norkyst800m/1h/aggregate_be')

# %% [markdown]
# Den over (reader_norkyst) virke som en bra. Kanskje me burde spør om anbefalinger fra bouvet. Under viser at den har mange av de nødvendige atributtene (alle utenom land_binary_mask). Me ser og at den har endtime fram i tid (ca 5 dager), så den kan brukes for prediksjoner

# %%
""" print(reader_norkyst.variables)
print(reader_norkyst.start_time)
print(reader_norkyst.end_time) """

# %%
""" reader_norkyst.plot() """

# %% [markdown]
# Får noe rar error, men den ska se sånn ut (Henta fra nettsiden deres) ![image.png](attachment:image.png)

# %%
from opendrift.readers import reader_global_landmask
reader_landmask = reader_global_landmask.Reader()
""" print(reader_landmask) """

# %%
""" reader_landmask.plot() """

# %% [markdown]
# Me har alt me trenge for å modellere og legge derfor til disse readersene.

# %%
o.add_reader([reader_landmask, reader_norkyst])

# %%
""" print(o) """

# %% [markdown]
# Burde og se på laze readers for når me ska bruke dette i produksjon: https://opendrift.github.io/tutorial.html#lazy-readers

# %% [markdown]
# Siste å gjør før me kjøre modellen er å legge til element (kontainere). Dette kalles seeding.
# 
# Eg fant ut av rett object_type ved hjelp av dette:
# The Leeway model is based on empirically determined coefficients as tabulated in https://github.com/OpenDrift/opendrift/blob/master/opendrift/models/OBJECTPROP.DAT
# Sånn eg ser det så har me to valg for container. Dette er enten:
# 
# CONTAINER-1                 73
#  Scaled down (1:3) 40-ft Container (70% submerged)
#        1.78     1.44      2.99      0.27     -2.44      2.31     -0.27      2.44      2.31
# 
# CONTAINER-2                 74
#  20-ft Container (80% submerged)
#        1.25     3.96      2.81      0.19      1.14      4.36     -0.19     -1.14      4.36
# 
# Litt usikker på ka de tallene står for, men kanskje det er verdt å se inn i å endre de.

# %%
from datetime import datetime
#datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

""" o.elements.add_variables( ) """
o.seed_elements(lon=4.3, lat=60, object_type=74, time=datetime(2023,2,16,5,0,0))
o.seed_elements(lon=4.0, lat=61, object_type=74, time=datetime(2023,2,16,5,0,0))

# %%
o.elements_scheduled

# %%
o.run()

#_______________________________________________________________________________________________

# All kode er tilsvarende som når David slapp, har kun kommentert ut alt som
# kjører animasjon etc. Ved å kjøre programmet printes data fra tidspunkter
# satt i seedingen.

# PS: Har satt grense s.a den kun skriver ut for 2 tidspunkter fra starttid.
# Dette kan endres i GetFloatingObjectData

from GetFloatingObjectData import convertToJSON, handleDataFromHistory

print(convertToJSON(handleDataFromHistory(o.history, o.get_time_array())))

#_______________________________________________________________________________________________


# %%
""" print(o) """

# %%
""" o.plot() """

# %%



