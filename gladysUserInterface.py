import io

import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

"""
	Student: Arna Togayeva
	Module: gladysUserInterface
	Description: This module presents a text-based menu for users and asks for their input to perform some operations. 
	This is a main module that calls functions and glues other modules together. 
"""


def runTests():
	"""
		tests some module functions
	"""
	
	print("running a few tests")

	average = compute.gpsAverage(4, 5)
	print("average = ", average)

	# delete the remaining code *in this function* and replace it with
	# your code. add more code to do what the assignment asks you to do.
	# add 3 more tests of different functions in different modules
	print("hello!")


def start():
	"""
		logs the user in, and runs the app
	"""

	userName = userLogin.login()

	runApp(userName)


def runApp(userName):
	"""
		runs the app
	"""

	currentValue = None
	destinationValue = None
	xCurrent = -1
	yCurrent = -1
	xDestination = -1
	yDestination = -1
	destination = [-1,-1]

	dist = 0.00

	# loop until user types q
	userQuit = False
	while (not userQuit):

		# menu
		"""
			here student needs to print their own menu. or, to do better, 
			create a function to print your menu and simply call it here.
		"""
		print("-- Welcome to the Gladys West Map App --")
		print("----------------------------------------")
		print("[c] to set current position")
		print("[d] to set destination position")
		print("[m] to map, which tells the distance")
		print("[t] to run module tests")
		print("[q] to quit")
		print()

		print(f"Current position: x = {xCurrent}, y = {yCurrent}")
		print(f"Destination position: x = {xDestination}, y = {yDestination}")
		print(f"Distance: {dist}")

		# get first character of input
		userInput = input("Enter a command: ")
		lowerInput = userInput.lower()
		firstChar = lowerInput[0:1]

		# menu choices, use a switch-like if-elif control structure

		"""
			here students need to change and add to this code to
			handle their menu options
		"""

		if firstChar == 'c':

			while True:

			# here function needs to be called
				xCurrent = input("Please enter a x coordinate (between 0-99) ")
				yCurrent = input("Please enter a y coordinate (between 0-99) ")
				if (xCurrent > 99 or xCurrent < 0) or (yCurrent > 99 or yCurrent < 0):
					print("The values you entered are outside of range 0-99")	
				else: 
					break

			#currentValue = satellite.gpsValue(xCurrent, yCurrent, "altitude")  # do we need the value?
			# print(f"current position: {current}")
			
			
			#if currentValue is None: 
			#	print("Values you entered are not found in Satelite data")
			#else:
				#if destinationValue is None:
				#	print("")
				#else:

			current = []
			current.append[xCurrent]
			current.append[yCurrent]
			# dist = compute.distance(current, destination)
					
					#print(f"distance {dist}")
			
		elif firstChar == 'd':
			while True:
			# here another function that sets destination
				xDestination = input("Please enter a x coordinate (between 0-99) ")
				yDestination = input("Please enter a y coordinate (between 0-99) ")
				if (xDestination > 99 or xDestination < 0) or (yDestination > 99 or yDestination < 0):
					print("The values you entered are outside of range 0-99")	
				else: 
					break
			
			# destinationValue = satellite.gpsValue(xDestination, yDestination, sat)
			# print(f"destination position: {destination}")
			
			#if destinationValue is None: 
			#	print("No value found. Please enter a valid number")
			#else:
			#	if currentValue is None:
			#		print("No value found. Please enter a valid number")
			#	else:

			destination = []
			destination.append[xDestination]
			destination.append[yDestination]
			dist = compute.distance(current, destination)
			
		elif firstChar == 'm':
			dist = compute.distance(current, destination)
			print(f"distance: {dist}")

		# quit
		elif firstChar == 'q':
			userQuit = True

		# run some tests (this is part 1 of 2)
		elif firstChar == 't':
			runTests()

		else:
			print("ERROR: " + firstChar + " is not a valid command")


	print("\n")
	print("Thank you for using the Gladys West Map App!")
	print("\n")
