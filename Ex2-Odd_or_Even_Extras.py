#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

#Extras!
#	1. If the number is a multiple of 4, print out a different message.

def main():
	user_number = get_number()
	print(odd_or_even(user_number))

def get_number():
	answer = float(input("Pick a number any number: "))
	if answer == int(answer):
		return(answer)
	else:
		answer = float(input("Please provide an integer: "))
		if answer == int(answer):
			return(answer)
		else: 
			print("You're being difficult, we'll use 43 as an example.")
			return(43)

def odd_or_even(user_number):
	if (user_number % 4 == 0):
		return(str(int(user_number)) + " is even, and divisible by 4!")
	elif (user_number % 2 == 0):
		return(str(int(user_number)) + " is even!")
	else:
		return(str(int(user_number)) + " is odd!")


main()
