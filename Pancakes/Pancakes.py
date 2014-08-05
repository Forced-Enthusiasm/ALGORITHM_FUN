"""keeps track of list slices to search through for largest elements as we move bottom up"""


def list_slicer(input_list, term):

	if term == 0:

		return input_list

	else:

		return input_list[:-term]


"""Customizable function for finding the largest 

list element, to be adjusted for pancakes later"""



def largest_in_slice(input_list):

	index = 0

	biggest = input_list[0]

	for i in input_list:

		if i > biggest:

			biggest = i

			index = input_list.index(i)

	return biggest




"""pancake sorter"""



def pancake(input_list):

	bottom = 0

	bottom_index = len(input_list) - bottom

	running_list = input_list

	sorted_list = input_list

	while bottom_index > 0 :



		running_list = list_slicer(sorted_list, bottom)

		L = largest_in_slice(running_list)



		if running_list[len(running_list) - 1] != L and running_list[0] != L:

			split_list_1 = [sorted_list[:sorted_list.index(L)+1],sorted_list[sorted_list.index(L)+1:]]

			split_list_1[0].reverse()

			split_list_1[0].extend(split_list_1[1])

			sorted_list = split_list_1[0]

			print "choosing from: " + str(running_list) + "\n"

			print "first flip: " + str(sorted_list) + "\n"

			split_list_2 = [sorted_list[:bottom_index],sorted_list[bottom_index:]]

			split_list_2[0].reverse()

			split_list_2[0].extend(split_list_2[1])

			sorted_list = split_list_2[0]

			print "final: " + str(sorted_list) + "\n" + "\n" + "\n"


			bottom += 1

			bottom_index = len(input_list) - bottom


			print "BOTTOM: " + str(bottom)



		elif running_list[0] == L:

			split_list = [sorted_list[:bottom_index],sorted_list[bottom_index:]]

			split_list[0].reverse()

			split_list[0].extend(split_list[1])

			sorted_list = split_list[0]

			bottom += 1

			bottom_index = len(input_list) - bottom


		elif L == running_list[len(running_list) - 1]:

			sorted_list = sorted_list

			bottom += 1

			bottom_index = len(input_list) - bottom

			print "final: " + str(sorted_list) + "\n" + "\n" + "\n"

			print "BOTTOM: " + str(bottom)




	print "HERE IS THE FINAL SORTED STACK OF PANCAKES, GO FUCK YOURSELF: " + "\n" +str(sorted_list)






a = [73,5,7,676,251,821,1,0,69,723,4603,126,1020,0,59]


print pancake(a)

# split_list = [a[:len(a)-1],a[len(a)-1:]]

# split_list[0].reverse()

# split_list[0].extend(split_list[1])

# split_list = split_list[0]

# print split_list
