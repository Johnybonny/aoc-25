def read_file(filename):
	diagram = []
	with open(filename, "r") as file:
		for line in file:
			diagram.append(list(line.split()[0]))
	return diagram


def remove_rolls(diagram, rolls_to_remove):
	for roll in rolls_to_remove:
		diagram[roll[0]][roll[1]] = '.'
	return diagram


def count_rolls(diagram):
	rolls_count = 0
	rolls_to_remove = []

	while True:
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
						rolls_to_remove.append([row, column])
						rolls_count += 1

		if len(rolls_to_remove) == 0:
			break
		else:
			diagram = remove_rolls(diagram, rolls_to_remove)
			rolls_to_remove = []

	return rolls_count


def main():
	diagram = read_file("input.txt")
	result = count_rolls(diagram)
	print(result)

if __name__ == "__main__":
	main()