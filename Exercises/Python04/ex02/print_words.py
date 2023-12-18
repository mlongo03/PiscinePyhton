file_name = input("Insert file name: ")
n = int(input("Insert an integer: "))
try:
	with open(file_name, 'r') as file:
		lines = file.readlines()
		lines.sort()
		print(f"The words longer than {n} are the following:")
		for line in lines:
			if (len(line) - 1) > n:
				print(line.replace("\n", ""))
except FileNotFoundError:
	print("Error! The specified file does not exist!")
