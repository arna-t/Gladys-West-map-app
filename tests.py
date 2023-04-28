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
