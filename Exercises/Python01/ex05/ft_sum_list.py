def sum_list(lst):
	sum = 0
	for number in lst:
		sum += number
	return sum


def main():
	n = int(input("Insert integer: "))
	lst = []
	while n != 0:
		lst.append(n)
		n = int(input("Insert integer: "))
	print("The sum is:", sum_list(lst))


if __name__ == "__main__":
	main()
