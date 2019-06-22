#! /usr/bin/python3

while True:
	# string stores the raw_input
	# str() converts raw_input into a string
	string = str(raw_input("\n\nType something that you want reversed:\n\n"))
	# string stores the result of the right side
	# reversed() reverses variable string
	# the join() method returns a string concatenated with the elements of iterable 
	# "" is the condition which will be join. 
	#          If dashes (-) inside, each letter will be separated by a dash
	string = "".join(reversed(string))
	# print the reversed string to the user
	print("\n\nYour reversed thing is: \n\n" + string)

	# Asks the user if they would like to continue
	another_game = raw_input("\n\nContinue? (y/n)\n")

	# If the raw_input is anything other than "y",
	#           Then the program will print "Thank you for playing!", then break
	if another_game != "y":
		print("\n\nThank you for playing!\n\n")
		break
