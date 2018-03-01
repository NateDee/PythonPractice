#Ask the user for a string and print out whether this string is a palindrome or not.
#(A palindrome is a string that reads the same forwards and backwards.)

def main_func():
	user_word = get_user_word()
	rev_word = p_check(user_word)
	if (user_word == rev_word):
		print("Your word: " + str(user_word) + " is a palindrome! " + str(user_word) + " = " + str(rev_word))
	else:
		print("Your word: " + str(user_word) + " is not a palindrome! " + str(user_word) + " != " + str(rev_word))

def get_user_word():
	word = str(input("Give me a word, I'll tell you if it's a palindrome: "))
	return(word.lower()) #make sure all lowercase

def p_check(word):
	rev_word = str()
	rev_word = word[::-1]
	return(rev_word)

main_func()