import sys
argc = len(sys.argv)
if argc < 4:
	print("Error! Usage: python3 ft_max.py <x> <y> <z>")
else:
	x = float(sys.argv[1])
	y = float(sys.argv[2])
	z = float(sys.argv[3])
	if x >= y and x >= z:
		max = x
	elif y >= x and y >= z:
		max = y
	else:
		max = z
	print("The max is:", max)
