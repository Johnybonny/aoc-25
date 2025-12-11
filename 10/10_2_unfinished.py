def read_file(filename):
	joltages = []
	buttons = []
	with open(filename, "r") as file:
		for line in file:
			joltages.append(list(map(int, list(line.split("{")[1][:-2].split(",")))))
			buttons.append([list(map(int, x[1:-1].split(","))) for x in line.split("]")[1].split("{")[0][1:-1].split(" ")])

	return joltages, buttons


def fewest_button_presses(lights, buttons):
	print(lights, buttons)
	print("Not finished")
	return 0
	sequences = generate_sequences(len(buttons))
	for sequence in sequences:
		if is_combination_correct(buttons, sequence, lights):
			return sum(sequence)


def count_total_button_presses(all_joltages, all_buttons):
	presses = 0
	for machine_index in range(len(all_joltages)):
		presses += fewest_button_presses(all_joltages[machine_index], all_buttons[machine_index])

	return presses


def main():
	all_joltages, all_buttons = read_file("test.txt")
	result = count_total_button_presses(all_joltages, all_buttons)
	print(result)

if __name__ == "__main__":
	main()