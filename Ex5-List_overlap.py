#Take two lists of numbers, and write a program that returns a list that contains only the elements 
#that are common between the lists (without duplicates). 
#Make sure your program works on two lists of different sizes.

#Create 2 random lists, say length 10 and 12
import random
rand_list1 = random.sample(range(20), 10)
rand_list2 = random.sample(range(20), 12)

def check_lists(rand_list1, rand_list2):
	result = []
	for i in range(0, len(rand_list1)):
		if rand_list1[i] in rand_list2:
			result.append(rand_list1[i])
	print("List #1: " + str(rand_list1))
	print("List #2: " + str(rand_list2))
	print("The following are common between List #1 and #2: " + str(result))

check_lists(rand_list1, rand_list2)