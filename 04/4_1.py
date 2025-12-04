def read_file(filename):
	diagram = []
	with open(filename, "r") as file:
		for line in file:
			diagram.append(list(line.split()[0]))
	return diagram


def count_rolls(diagram):
	rolls = 0

	for row in range(len(diagram)):
		for column in range(len(diagram[0])):
			if diagram[row][column] == '@':
				up = max(row - 1, 0)
				left = max(column - 1, 0)
				down = min(row + 1, len(diagram) - 1)
				right = min(column + 1, len(diagram[0]) - 1)

				count = 0
				for i in range(up, down + 1):
					for j in range(left, right + 1):
						if diagram[i][j] == '@' and (i, j) != (row, column):
							count += 1

				if count < 4:
					rolls += 1

	return rolls


def main():
	diagram = read_file("input.txt")
	result = count_rolls(diagram)
	print(result)

if __name__ == "__main__":
	main()