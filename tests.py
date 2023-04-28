import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

"""
    Student: Joel Alvarado
    Module: tests
    Description: This module provides tests for functions defined in compute, satellite, and userLogin modules.
"""


# Test naming convention is objectUnderTest_situationOrTrigger_expectedResult

def runTests():
    runTest(gpsAverage_integerInput_equalsExpected)
    runTest(login_whenCalled_logsUserIn)
    runTest(readSat_validSatelliteName_returnsIterableData)
    runTest(gpsValue_validInput_equalsExpected)


def runTest(test):
    try:
        test()
    except Exception as e:
        print(f'test failed with error: {e}\n')


def gpsAverage_integerInput_equalsExpected():
    print("running gpsAverage test")

    # arguments
    x = 0
    y = 0

    average = compute.gpsAverage(x, y)

    # from satellite files
    # (473 + 366 + 692 + 694) / 4
    expected = 556.25

    if average == expected:
        print("test passed")
        print(f'gpsAverage(0, 0) = {average}')
    else:
        print("test failed")
        print(f'arguments: x = {x} y = {y}')
        print(f'expected average: {expected} actual average: {average}')

    print()


def login_whenCalled_logsUserIn():
    print("running user login test")

    userName = userLogin.login()

    print("test passed")
    print(f'userName: {userName}')
    print()


def readSat_validSatelliteName_returnsIterableData():
    print("running readSat test")

    # arguments
    satelliteName = "longitude"
    pathToJSONDataFiles = "./data/"

    # get data
    data = satellite.readSat(satelliteName, pathToJSONDataFiles)

    # data should be iterable
    try:
        satelliteData = iter(data)
    except TypeError as typeError:
        print("test failed. no suitable satellite data found. data should be iterable.\n")
        return

    totalDataEntries = 0

    for _ in satelliteData:
        totalDataEntries += 1

    print("test passed")
    print(f'total coordinates entries: {totalDataEntries}')
    print()


def gpsValue_validInput_equalsExpected():
    print("running gpsValue test")

    # arguments
    x = 75
    y = 50
    satelliteName = "time"

    # get value
    value = satellite.gpsValue(x, y, satelliteName)

    # from time-satellite.json
    expected = 581

    if expected == value:
        print("test passed")
        print(f'gpsValue({x}, {y}, {satelliteName}) = {value}')
    else:
        print(f'test failed')
        print(f'arguments: x = {75} y = {50} satelliteName = {satelliteName}')
        print(f'expected value: {expected} actual value: {value}')

    print()
