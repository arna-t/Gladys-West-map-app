import io
import math

import gladysSatellite as satellite

"""
	Student: Naomi Gong, Theanh Nguyen
	Module: gladysCompute
	Description: This module does the calculations needed to know the current distance and destination distance. 
"""

# start of code by Naomi Gong
def gpsAverage(x, y):
	"""
		This calculates the average gps distance based on the coordinates given
	"""

	value = satellite.gpsValue(x, y, "altitude") + satellite.gpsValue(x,y, "longitude") + satellite.gpsValue(x,y, "latitude") + satellite.gpsValue(x,y, "time")

	average = value / 4

	return average
# end of code by Naomi Gong

# start of code by Theanh Nguyen
def distance(current, destination):
	"""
		This calculates the distance between the current location and the destination location
	"""
	xCurrent = current[0]
	yCurrent = current[1]
	xDestination = destination[0]
	yDestination = destination[1]

	distance = math.sqrt(gpsAverage(xCurrent, yCurrent)**2 + gpsAverage(xDestination, yDestination)**2)
	return distance
# end of code by Theanh Nguyen