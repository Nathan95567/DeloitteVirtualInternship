import json, unittest, datetime

with open("./data-1.json","r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json","r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json","r") as f:
    jsonExpectedResult = json.load(f)

"""
In this project, I created two function to convert the format from data-1 and data-2 to data-result. 
Function convertFromFormat1 is used to convert data-1 and the other function is used to convert data-2.
"""


def convertFromFormat1 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    newLocation = jsonObject["location"].split('/')

    jsonObject = {
        "deviceID" : jsonObject['deviceID'],
        "deviceType" : jsonObject["deviceType"],
        "timestamp" : jsonObject["timestamp"],
        "location" : {
            "country": newLocation[0],
            "city": newLocation[1],
            "area": newLocation[2],
            "factory": newLocation[3],
            "section": newLocation[4]
        },
        "data" : {
            "status" : jsonObject["operationStatus"],
            "temperature" : jsonObject["temp"]
        }
    }

    return jsonObject


def convertFromFormat2 (jsonObject):

    # IMPLEMENT: Conversion From Type 1

    time = jsonObject['timestamp']
    date = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ')
    timestamp = round((date - datetime.datetime(1970, 1, 1)).total_seconds()*1000)

    jsonObject = {
        "deviceID" : jsonObject['device']['id'],
        "deviceType" : jsonObject['device']['type'],
        "timestamp" : timestamp,
        "location" : {
            "country": jsonObject['country'],
            "city": jsonObject['city'],
            "area": jsonObject['area'],
            "factory": jsonObject['factory'],
            "section": jsonObject['section']
        },
        "data" : {
            "status" : jsonObject['data']["status"],
            "temperature" : jsonObject['data']["temperature"]
        }
    }

    return jsonObject


def main (jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):

        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):

        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    unittest.main()
