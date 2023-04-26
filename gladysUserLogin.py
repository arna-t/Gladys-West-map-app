import io
import re

"""
	Student: Tu D.Vu
	Module: gladysUserLogin
	Description: This module asks the user for their login and password. It will only accept a valid email address as login and will accept
    any password. If the user provides an invalid login, it will print an error statement. The "while True" loop makes the function ask
    for the user's login and password again until it receives a valid entry. In that case, it will break the loop and allow the user to 
    access the app. 
"""

def login():

    while True:
        # Ask user for login and password
        login = input("Please enter your login: ")
        password = input("Please enter your password: ")
        
        # This statement ensures that the user enters a valid email address as login. 
        # A valid email address contains 1 or more character before and after "@" 
        # A "." after "@" followed by 1 or more character. 
        # If the login is not a valid email, it will prompt the user to enter a valid email address again.
        if not re.match(r"[^@]+@[^@]+\.[^@]+", login):
            print ("ERROR: Please provide a valid email address.")
        else:
            # Return login if valid email and any password is provided
            return login
            break
