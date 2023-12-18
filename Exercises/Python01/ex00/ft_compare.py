import sys
if float(sys.argv[1]) > float(sys.argv[2]):
	print(float(sys.argv[1]), "is greater than", float(sys.argv[2]))
elif float(sys.argv[1]) < float(sys.argv[2]):
	print(float(sys.argv[1]), "is less than", float(sys.argv[2]))
else:
	print(float(sys.argv[1]), "is equal to", float(sys.argv[1]))
