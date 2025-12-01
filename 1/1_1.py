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
		current = (current + rot["direction"] * rot["value"]) % circle_size
		if current == 0:
			password += 1
	return password


def main():
	rotations = read_file("input.txt")
	result = compute_password(50, 100, rotations)
	print(result)

if __name__ == "__main__":
	main()