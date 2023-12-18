n = int(input("Insert an integer: "))
with open('words.txt', 'r') as file:
	lines = file.readlines()
	lines.sort()
	with open('long_words.txt', 'w') as file2:
		print(f"The words longer than {n} have been written on \"long_words.txt\"")
		for line in lines:
			if (len(line) - 1) > n:
				file2.write(line)
