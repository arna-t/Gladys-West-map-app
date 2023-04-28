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

	xCurrent = -1
	yCurrent = -1
	xDestination = -1
	yDestination = -1
	destination = [-1,-1]
	dist = 0.00

	def menu():

		print("-- Welcome to the Gladys West Map App --")
		print("----------------------------------------")
		print(f"user - {userName}")
		print()
		print(f"Current position:     x = {xCurrent}, y = {yCurrent}")
		print(f"Destination position: x = {xDestination}, y = {yDestination}")
		print(f"Distance: {dist}")
		print()
		print("[c] to set current position")
		print("[d] to set destination position")
		print("[m] to map, which tells the distance")
		print("[t] to run module tests")
		print("[q] to quit")
		print()


	# loop until user types q
	userQuit = False
	while (not userQuit):

		#calling the menu function
		print()
		menu()

		# get first character of input
		userInput = input("Enter a command: ")
		lowerInput = userInput.lower()
		firstChar = lowerInput[0:1]
		
		
		# menu choices, use a switch-like if-elif control structure


		if firstChar == 'c':

			#is_valid = True
			#while not is_valid:

			xCurrent = int(input("Please enter a x coordinate (between 0-99): "))
			yCurrent = int(input("Please enter a y coordinate (between 0-99): "))
			if (xCurrent > 99 or xCurrent < 0) or (yCurrent > 99 or yCurrent < 0):
				print("The values you entered are outside of range 0-99")	
			else: 
				current = []
				current.append(xCurrent)
				current.append(yCurrent)
				dist = compute.distance(current, destination)
				
			
					#print(f"distance {dist}")
			
		elif firstChar == 'd':
			
				xDestination = int(input("Please enter a x coordinate (between 0-99): "))
				yDestination = int(input("Please enter a y coordinate (between 0-99): "))
				if (xDestination > 99 or xDestination < 0) or (yDestination > 99 or yDestination < 0):
					print("The values you entered are outside of range 0-99")	
				else: 
					destination = []
					destination.append(xDestination)
					destination.append(yDestination)
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

		print()
		menu()
		userInput = input("Enter a command: ")
		lowerInput = userInput.lower()
		firstChar = lowerInput[0:1]

	print("\n")
	print("Thank you for using the Gladys West Map App!")
	print("\n")
