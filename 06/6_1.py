def read_file(filename):
	lines = []
	with open(filename, "r") as file:
		for line in file:
			lines.append(line.split())

	problem_numbers = []
	for line in lines[:-1]:
		problem_numbers.append(list(map(int, line)))
	operations = lines[-1]

	return problem_numbers, operations


def compute_grand_total(problem_numbers, operations):
	grand_total = 0
	for problem_index in range(len(problem_numbers[0])):
		if operations[problem_index] == "+":
			problem_total = 0
			for number_index in range(len(problem_numbers)):
				problem_total += problem_numbers[number_index][problem_index]
		else:
			problem_total = 1
			for number_index in range(len(problem_numbers)):
				problem_total *= problem_numbers[number_index][problem_index]

		grand_total += problem_total

	return grand_total


def main():
	problem_numbers, operations = read_file("input.txt")
	result = compute_grand_total(problem_numbers, operations)
	print(result)

if __name__ == "__main__":
	main()