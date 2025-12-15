def present_size(present):
	size = 0
	for i in range(3):
		for j in range(3):
			size += 1 if present[i][j] == "#" else 0
	return size


def read_file(filename):
	presents = {}
	regions = []
	with open(filename, "r") as file:
		line = file.readline()
		while line.split(":")[0].isnumeric():
			present = [file.readline().replace("\n", "") for _ in range(3)]
			presents[int(line.split(":")[0])] = present
			line = file.readline()
			line = file.readline()

		while line:
			regions.append([line.split(":")[0], list(map(int, line.split(":")[1][1:].replace("\n","").split(" ")))])
			line = file.readline()

	return presents, regions


def count_regions(presents, regions):
	count = 0
	for region in regions:
		region_size = int(region[0].split("x")[0]) * int(region[0].split("x")[1])
		presents_sum = 0
		for present_index in range(len(region[1])):
			presents_sum += region[1][present_index] * present_size(presents[present_index])

		if region_size >= presents_sum:
			count += 1

	print(":-|")

	return count


def main():

	presents, regions = read_file("input.txt")
	result = count_regions(presents, regions)
	print(result)

if __name__ == "__main__":
	main()