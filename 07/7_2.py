def read_file(filename):
	diagram = []
	with open(filename, "r") as file:
		for line in file:
			diagram.append(list(line.replace("\n", "")))

	return diagram

def print_nicely(diagram):
	for d in diagram:
		print("".join(d))


def find_first_splitter(diagram):
	for i in range(len(diagram)):
		for j in range(len(diagram[i])):
			if diagram[i][j] == "^":
				return [i, j]


def count_all_timelines(diagram):
	first_splitter = find_first_splitter(diagram)

	for row in range(len(diagram) - 2, 0, -1):
		for column in range(len(diagram[row])):
			if diagram[row][column] == "^":
				left_found = False
				right_found = False
				left_child = 1 if column > 0 else 0
				right_child = 1 if column < len(diagram[row]) - 1 else 0
				for i in range(row + 1, len(diagram)):
					if not left_found and column > 0 and diagram[i][column - 1].isnumeric():
						left_child = int(diagram[i][column - 1])
						left_found = True
					if not right_found and column < len(diagram[row]) - 1 and diagram[i][column + 1].isnumeric():
						right_child = int(diagram[i][column + 1])
						right_found = True
					if left_found and right_found:
						break
				diagram[row][column] = str(left_child + right_child)

	# print_nicely(diagram)

	return int(diagram[first_splitter[0]][first_splitter[1]])


def main():
	diagram = read_file("input.txt")
	result = count_all_timelines(diagram)
	print(result)

if __name__ == "__main__":
	main()