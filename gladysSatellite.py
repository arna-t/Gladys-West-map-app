import io
import json

"""
    Student: Joel Alvarado
    Module: gladysSatellite
    Description: This module provides gps data from satellites.
"""


def readSat(satelliteName, pathToJSONDataFiles):
    """
        reads satellite data from a json file. Throws IOError if the data file for
        satelliteName cannot be opened.
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

    # read the file
    data = json.load(fileHandle)

    return data


def gpsValue(x, y, satelliteName):
    """
        Searches the data from satelliteName for the numerical gps value at coordinates x and y and returns that value.

        Returns 0 if the coordinates are not found in the satellite's data. Throws IOError if the data file for
        satelliteName cannot be opened.
    """

    # path to satellite data files
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
    return 0