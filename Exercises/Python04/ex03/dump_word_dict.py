def main():
	import pickle
	with open('words.txt', 'r') as file:
		lines = file.readlines()
		dct = dict()
		for line in lines:
			dct[len(line.replace("\n", ""))] = dct.get(len(line.replace("\n", "")), 0) + 1
		with open('word_count.pickle', 'wb') as file2:
			pickle.dump(dct, file2)

if __name__ == "__main__":
	main()
