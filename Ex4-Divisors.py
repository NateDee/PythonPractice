#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
#(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def main_func():
	user_number = user_choose()
	divisor_list = find_divisors(user_number)
	print("You chose the number " + str(user_number))
	print("Your number is divisible by: " + str(divisor_list))

def user_choose():
	user_number = float(input("Please choose a number, any number: "))	
	if user_number != int(user_number):
		print("You choose a non whole number, your number has been rounded to: " + str(int(user_number)))
	return(int(user_number))

def find_divisors(number):
	result = []
	for i in range(1, number+1):
		if number % i == 0: result.append(i)
	return(result)

main_func()