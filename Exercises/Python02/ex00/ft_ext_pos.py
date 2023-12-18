import sys
argc = len(sys.argv)
if argc < 2:
	print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
else:
	list = sys.argv[1:]
	i = 0
	min = 0
	max = 0
	pos = 0
	while i < len(list):
		if int(list[i]) < min:
			min = int(list[i])
			pos = i
		i += 1
	print("The min is", min, "and its position is", pos)
	i = 0
	while i < len(list):
		if int(list[i]) > max:
			max = int(list[i])
			pos = i
		i += 1
	print("The max is", max, "and its position is", pos)
