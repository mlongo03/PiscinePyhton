n = int(input("Insert an integer: "))
with open('words.txt', 'r') as file:
	lines = file.readlines()
	lines.sort()
	print(f"The words longer than {n} are the following:")
	for line in lines:
		if (len(line) - 1) > n:
			print(line.replace("\n", ""))
