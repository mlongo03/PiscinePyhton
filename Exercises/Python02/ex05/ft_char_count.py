import sys
argc = len(sys.argv)
if argc < 2:
	print("Error! No string given")
else:
	str = sys.argv[1].lower()
	list = [char for char in str]
	list.sort()
	dct = dict()
	for char in list:
		dct[char] = dct.get(char, 0) + 1
	for key, value in dct.items():
		print(key, "=", value)
