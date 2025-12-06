def read_file(filename):
	lines = []
	with open(filename, "r") as file:
		lines = file.readlines()

	numbers = []
	for line in lines[:-1]:
		numbers.append(line.replace("\n", ""))

	operations = lines[-1].split()

	return numbers, operations


def translate_to_human_math(numbers):
	longest_line = 0
	for line in numbers:
		if len(line) > longest_line:
			longest_line = len(line)

	all_problem_numbers = []
	problem_numbers = []
	for column in range(longest_line):
		new_number = ""
		for row in range(len(numbers)):
			if column < len(numbers[row]):
				new_number += numbers[row][column]
		if new_number.replace(" ", "" ) != "":
			problem_numbers.append(int(new_number))
		else:
			all_problem_numbers.append(problem_numbers)
			problem_numbers = []
	all_problem_numbers.append(problem_numbers)

	return all_problem_numbers


def compute_grand_total(numbers, operations):

	all_problem_numbers = translate_to_human_math(numbers)

	grand_total = 0
	for problem_index in range(len(all_problem_numbers)):
		if operations[problem_index] == "+":
			problem_total = 0
			for number in all_problem_numbers[problem_index]:
				problem_total += number
		else:
			problem_total = 1
			for number in all_problem_numbers[problem_index]:
				problem_total *= number
		grand_total += problem_total

	return grand_total


def main():
	numbers, operations = read_file("input.txt")
	result = compute_grand_total(numbers, operations)
	print(result)

if __name__ == "__main__":
	main()