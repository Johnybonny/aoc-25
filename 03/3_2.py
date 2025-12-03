def read_file(filename):
	banks = []
	with open(filename, "r") as file:
		for line in file:
			banks.append(list(map(int, list(line.split()[0]))))
	return banks


def output_joltage(num_of_batteries, banks):
	total_output = 0
	for bank in banks:
		joltage = ''

		batteries_positions = [-1] * num_of_batteries
		for battery_no in range(len(batteries_positions)):

			if battery_no > 0:
				left = batteries_positions[battery_no - 1] + 1
			else:
				left = 0
			right = len(bank) - num_of_batteries + battery_no + 1


			for i in range(9, 0, -1): # 9, 8, .., 2, 1
				for j in range(left, right):
					if bank[j] == i:
						joltage += str(bank[j])
						batteries_positions[battery_no] = j
						break
				if batteries_positions[battery_no] >= 0:
					break

		total_output += int(joltage)

	return total_output


def main():
	banks = read_file("input.txt")
	result = output_joltage(12, banks)
	print(result)

if __name__ == "__main__":
	main()