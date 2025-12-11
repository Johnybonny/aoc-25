def read_file(filename):
	lights = []
	buttons = []
	with open(filename, "r") as file:
		for line in file:
			machine_lights = list(line.split("]")[0][1:])
			for i in range(len(machine_lights)):
				machine_lights[i] = machine_lights[i] == "#"

			lights.append(machine_lights)
			buttons.append([list(map(int, x[1:-1].split(","))) for x in line.split("]")[1].split("{")[0][1:-1].split(" ")])

	return lights, buttons


def generate_sequences(number):
	sequences_priorities = []
	for i in range(2 ** number):
		sequence = list(format(i, f'0{number}b'))
		sequences_priorities.append([sequence, sum(list(map(int, list(sequence))))])
	sequences_priorities.sort(key=lambda x: x[1])
	sequences = [list(map(int, sp[0])) for sp in sequences_priorities]
	return sequences


def is_combination_correct(buttons, sequence, goal):
	lights = [False] * len(goal)
	for press in range(len(sequence)):
		if sequence[press]:
			for light in buttons[press]:
					lights[light] = not lights[light]

	return lights == goal


def fewest_button_presses(lights, buttons):
	sequences = generate_sequences(len(buttons))
	for sequence in sequences:
		if is_combination_correct(buttons, sequence, lights):
			return sum(sequence)


def count_total_button_presses(all_lights, all_buttons):
	presses = 0
	for machine_index in range(len(all_lights)):
		presses += fewest_button_presses(all_lights[machine_index], all_buttons[machine_index])

	return presses


def main():
	all_lights, all_buttons = read_file("input.txt")
	result = count_total_button_presses(all_lights, all_buttons)
	print(result)

if __name__ == "__main__":
	main()