s = input("Insert a string: ")
n = int(input("Insert an integer: "))
if n >= len(s):
	print("Error: index out of range")
else:
	print(s[n], s[-n])
