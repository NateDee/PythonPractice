#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

def main():
	user_number = get_number()
	return(user_number)

def get_number():
	answer = float(raw_input("Pick a number any number: "))
	if answer == int(answer):
		return(answer)
	else:
		answer = float(raw_input("Please provide an integer: "))
		if answer == int(answer):
			return(answer)
		else: 
			print("You're being difficult, we'll use 43 as an example.")
			return(43)

main()
print(user_number)
