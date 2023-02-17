# format på output fra o.history:

[[(id1.1 ,...) , (id1.2, ...)] , [(id2.1 ,...) , (id2.2, ...)]]

# Forskjellige tips og notater gjort

print(o.get_time_array()[0][0].time()) -> hh:mm:ss
print(o.get_time_array()[0][0].date()) -> #yyyy-mm-dd
print(o.elements) -> attributtene til elementet
print(o.history[0][0:-1][0]) -> hele objektet av objekt 0 i listen

# Format på output fra print(convertToJSON(handleDataFromHistory(o.history, o.get_time_array()))):

{'allData': [
{
'id': 1,
'listPerDateTime': [
{
'dateTime': '2023-02-14 16:00:00',
'variables': {
'status': 0,
'moving': 1,
'longitude': 4.3,
'latitude': 60.0}
},
{
'dateTime': '2023-02-14 17:00:00',
'variables': {
'status': 0,
'moving': 1,
'longitude': 4.3080587,
'latitude': 60.017056
}
},
....
]
},
{
'id': 2, 'listPerDateTime': [
{
'dateTime': '2023-02-14 16:00:00',
'variables': {
'status': 0,
'moving': 1,
'longitude': 4.0,
'latitude': 61.0}
},
{
'dateTime': '2023-02-14 17:00:00',
'variables':{
'status': 0,
'moving': 1,
'longitude': 4.003296,
'latitude': 61.010338
}
}
...
]
},
....
]
}
