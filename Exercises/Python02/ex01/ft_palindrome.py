def is_palindrome(name):
	no_spaces = name.replace(" ", "")
	i = 0
	while i < len(no_spaces):
		if no_spaces[i] != no_spaces[len(no_spaces) - i - 1]:
			return False
		i += 1
	return True

def main():
	import sys
	argc = len(sys.argv)
	if argc != 2:
		print("Error! Insert just 1 string!")
	else:
		if is_palindrome(sys.argv[1]) == True:
			print("The string", sys.argv[1] ,"is palindrome")
		else:
			print("The string", sys.argv[1] ,"is not palindrome")


if __name__ == "__main__":
	main()
