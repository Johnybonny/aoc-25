def read_file(filename):
	diagram = []
	with open(filename, "r") as file:
		for line in file:
			diagram.append(list(line.replace("\n", "")))

	return diagram

def print_nicely(diagram):
	for d in diagram:
		print("".join(d))


def count_splits(diagram):
	splits = 0

	start = diagram[0].index("S")
	diagram[1][start] = '|'

	for row in range(2, len(diagram)):
		for column in range(len(diagram[row])):
			if diagram[row][column] == "^" and diagram[row - 1][column] == "|":
				if column > 0:
					diagram[row][column - 1] = "|"
				if column < len(diagram[row]) - 1:
					diagram[row][column + 1] = "|"
				splits += 1
			elif diagram[row][column] == "." and diagram[row - 1][column] == "|":
				diagram[row][column] = "|"

	# print_nicely(diagram)

	return splits


def main():
	diagram = read_file("input.txt")
	result = count_splits(diagram)
	print(result)

if __name__ == "__main__":
	main()