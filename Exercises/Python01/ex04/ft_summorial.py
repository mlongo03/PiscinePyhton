import sys
argc = len(sys.argv)
if argc < 2:
	print("Error! Usage: python3 ft_summorial.py <n>")
else:
	n = int(sys.argv[1])
	if n < 0:
		print("Error! n must be >=0")
	else:
		sum = 0
		while n > 0:
			sum += n
			n = n - 1
		print("The sum is:", sum)
