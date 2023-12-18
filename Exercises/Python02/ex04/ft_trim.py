def trim(list):
	list[:] = list[1:-1]
	return None

def main():
	import sys
	argc = len(sys.argv)
	if argc < 3:
		print("Error! You must insert at least 2 values")
	else:
		trim_list = sys.argv[1:]
		trim(trim_list)
		print("The new list is:", trim_list)


if __name__ == "__main__":
	main()

