import io

import gladysSatellite as satellite

"""
	Student: Naomi Gong, Theanh Nguyen, Nataly Infante
	Module: gladysCompute
	Description: This module does the calculations needed to know the current distance and destination distance. 
"""


def gpsAverage(x, y):
	"""
		This calculates the average gps distance based on the coordinates given
	"""

	value = satellite.gpsValue(x, y, "altitude") + satellite.gpsValue(x,y, "longitude") + satellite.gpsValue(x,y, "latitude") + satellite.gpsValue(x,y, "time")

	average = value / 4

	return average


def distance(current, destination):
	"""
		document your function definition here. what does it do?
	"""

	"""
		delete the remaining code *in this function* and replace it with
		your own code. add more code to do what the assignment asks of you.
	"""
	distance = gpsAverage(3, 4)

	return distance
