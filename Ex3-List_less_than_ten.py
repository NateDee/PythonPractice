#Instructions:
#  Take a list, say for example this one:
#
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  and write a program that prints out all the elements of the list that are less than 5.

import random
#Create random list:
def main_func():
	list_random = random.sample(range(20), 10)
	print("The current list is: " + str(list_random))
	print("Here are the numbers in the list less than 5: " + str(loop_check(list_random)))

#Loop through list, print
def loop_check(list_random):
	#Create empty result_list to hold new list
	result_list = []
	for i in range(len(list_random)):
		if list_random[i] < 5:
			result_list.append(list_random[i])
	return(result_list)

main_func()