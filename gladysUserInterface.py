import io

import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

"""
	Student: Gabriel Solomon
	Module: gladysUserInterface
	Description: This module does …
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

	dist = None
	currentValue = None
	destinationValue = None

	# loop until user types q
	userQuit = False
	while (not userQuit):

		# menu
		"""
			here student needs to print their own menu. or, to do better, 
			create a function to print your menu and simply call it here.
		"""
		print("-- Welcome to the Gladys West Map App --")
		#print("Type t to run tests or q to quit")
		print("[c] to set current position")
		print("[d] to set destination position")
		print("[m] to map, which tells the distance")
		print("[t] to run module tests")
		print("[q] to quit")
		print()

		# get first character of input
		userInput = input("Enter a command:")
		lowerInput = userInput.lower()
		firstChar = lowerInput[0:1]

		# menu choices, use a switch-like if-elif control structure

		"""
			here students need to change and add to this code to
			handle their menu options
		"""

		if firstChar == 'c':
			# here function needs to be called
			x = input("Please enter the x coordinate ")
			y = input("Please enter the y coordinate ")
			# sat = 
			currentValue = satellite.gpsValue(x, y, sat)
			# print(f"current position: {current}")
			
			if currentValue is None: 
				print("Returned no value")
			else:
				if destinationValue is None:
					print("Please enter for the destination")
				else:
					print("Please enter m to calculate distance")
					#dist = compute.distance(currentValue, destinationValue)
					#print(f"distance {dist}")
			
		elif firstChar == 'd':
			# here another function that sets destination
			x = input("Please enter the x coordinate ")
			y = input("Please enter the y coordinate ")
			destinationValue = satellite.gpsValue(x, y, sat)
			# print(f"destination position: {destination}")

			if destinationValue is None: 
				print("Returned no value")
			else:
				if currentValue is None:
					print("Please enter for the current position")
				else:
					print("Please enter m to calculate distance")
					#print(f"distance {dist}")
					#dist = compute.distance(current, destination)
			
		elif firstChar == 'm':
			dist = compute.distance(currentValue, destinationValue)
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
