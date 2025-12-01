def read_file(filename):
	instructions = []
	with open(filename, "r") as file:
		lines = file.readlines()
		for line in lines:
			instructions.append({"direction": -1 if line[0] == "L" else 1, "value": int(line[1:])})
	return instructions


def compute_password(current, circle_size, rotations):
	password = 0
	for rot in rotations:
		full_rotations = rot["value"] // circle_size
		password += full_rotations

		extra = rot["direction"] * rot["value"] - full_rotations * rot["direction"] * circle_size
		next_position = current + extra
		if next_position == 0 or next_position > 99 or (current != 0 and next_position < 0):
			password += 1

		current = next_position % circle_size
	return password


def main():
	rotations = read_file("input.txt")
	result = compute_password(50, 100, rotations)
	print(result)

if __name__ == "__main__":
	main()