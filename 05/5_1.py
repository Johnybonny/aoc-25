def read_file(filename):
	ranges = []
	ingredients = []
	with open(filename, "r") as file:
		reading_ranges = True
		for line in file:
			if line.split() == []:
				reading_ranges = False
			elif reading_ranges:
				ranges.append(list(map(int, line.split("-"))))
			else:
				ingredients.append(int(line))
	return ranges, ingredients


def count_fresh(ranges, ingredients):
	fresh_count = 0
	for i in ingredients:
		for r in ranges:
			if r[0] <= i and r[1] >= i:
				fresh_count += 1
				break

	return fresh_count


def main():
	ranges, ingredients = read_file("input.txt")
	result = count_fresh(ranges, ingredients)
	print(result)

if __name__ == "__main__":
	main()