#! /usr/bin/python3

while True:
	string = str(raw_input("\n\nType something that you want reversed:\n\n"))
	string = "".join(reversed(string))
	print("\n\nYour reversed thing is: \n\n" + string)
	another_game = raw_input("\n\nAnother word? (y/n)\n")
	if another_game != "y":
		print("\n\nThank you for playing!\n\n")
		break