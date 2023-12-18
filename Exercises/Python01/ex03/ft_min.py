def my_min(x: float=None, y: float=None, z: float=None):
	if x is None or y is None or z is None:
		return 0
	else:
		if x <= y and x <= z:
			return x
		elif y <= x and y <= z:
			return y
		else:
			return z

def main():
	import sys
	argc = len(sys.argv)
	if argc < 4:
		print("Error! Usage: python3 ft_min.py <x> <y> <z>")
	else:
		x = float(sys.argv[1])
		y = float(sys.argv[2])
		z = float(sys.argv[3])
		print("The min is:", my_min(x, y, z))

if __name__ == "__main__":
	main()
