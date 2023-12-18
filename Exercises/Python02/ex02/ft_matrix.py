import sys
argc = len(sys.argv)
if argc < 3:
	print("Error! Usage: python3 ft_matrix.py <n> <m>")
else:
	matrix = [[0] * int(sys.argv[2]) for _ in range(int(sys.argv[1]))]
	for y in range(0, int(sys.argv[1])):
		for x in range(0, int(sys.argv[2])):
			matrix[y][x] = float(input("Insert the element in position (" + str(y) + ", " + str(x) + "): "))
	print("The inserted matrix is:")
	for y in range(0, int(sys.argv[1])):
		print(matrix[y])
	print("The sum over rows is:")
	sumList = []
	for y in range(0, int(sys.argv[1])):
		sum = 0
		for x in range(0, int(sys.argv[2])):
			sum += float(matrix[y][x])
		sumList.append(sum)
	print(sumList)
	print("The sum over columns is:")
	sumList = []
	for x in range(0, int(sys.argv[2])):
		sum = 0
		for y in range(0, int(sys.argv[1])):
			sum += float(matrix[y][x])
		sumList.append(sum)
	print(sumList)
