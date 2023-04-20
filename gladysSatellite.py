import io
import json

"""
    Student: Joel Alvarado
    Module: gladysSatellite
    Description: This module provides gps data from satellites.
"""


def readSat(satelliteName, pathToJSONDataFiles):
    """
        reads satellite data from a json file
    """

    # data file path
    fileName = satelliteName + "-satellite.json"
    filePath = pathToJSONDataFiles + "/" + fileName

    # open the file
    try:
        fileHandle = open(filePath)
    except IOError:
        print("ERROR: Unable to open the file " + filePath)
        raise IOError

    # print("filePath = ", filePath)

    # read the file
    data = json.load(fileHandle)

    return data


def gpsValue(x, y, satelliteName):
    """
        Searches the data from satelliteName for the numerical value at coordinates x and y and returns that value.

        If the coordinates are not found in the satellite's data, None is returned.
    """

    pathToJSONDataFiles = "./data/"

    # read the satellite data
    satelliteData = readSat(satelliteName, pathToJSONDataFiles)

    # loop through the data
    for coordinatesInfo in satelliteData:
        # if the coordinates match, return the value
        if coordinatesInfo["x"] == x and coordinatesInfo["y"] == y:
            value = coordinatesInfo["value"]
            return value

    # The coordinates were not found
    return None
