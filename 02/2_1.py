def read_file(filename):
	ranges = []
	with open(filename, "r") as file:
		line = file.readline().split(",")
		for i in line:
			ranges.append([int(i.split("-")[0]), int(i.split("-")[1])])
	return ranges


def compute_invalid_sum(ranges):
	sum = 0
	for r in ranges:
		for i in range(r[0], r[1] + 1):
			id = str(i)
			if len(id) % 2 == 0 and id[:len(id)//2] == id[len(id)//2:]:
				sum += i
	return sum


def main():
	ranges = read_file("input.txt")
	result = compute_invalid_sum(ranges)
	print(result)

if __name__ == "__main__":
	main()