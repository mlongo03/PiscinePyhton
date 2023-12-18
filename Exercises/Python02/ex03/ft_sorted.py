import sys
argc = len(sys.argv)
if argc < 3:
	print("Error! You must insert at least 2 numbers")
else:
	num_list = sys.argv[1:]
	if num_list == sorted(num_list, reverse=True):
		print("The inserted sequence is sorted!")
	else:
		print("The inserted sequence is not sorted!\nThe correct order is", sorted(num_list, reverse=True))
