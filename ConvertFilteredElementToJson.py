import json 

# Method to convert a python dictionary/object to JSON
async def convertToJSON(pythonDictionary):
    jsonObject = json.dumps(pythonDictionary)
    return jsonObject