def read_file(filename):
	red_tiles = []
	with open(filename, "r") as file:
		for line in file:
			red_tiles.append({"x": int(line.split(",")[0]), "y": int(line.split(",")[1])})

	return red_tiles


def compute_largest_area(red_tiles):
	largest_area = 0
	for i in range(len(red_tiles)):
		for j in range(i + 1, len(red_tiles)):
			area = (abs(red_tiles[i]["x"] - red_tiles[j]["x"]) + 1) * (abs(red_tiles[i]["y"] - red_tiles[j]["y"]) + 1)
			if area > largest_area:
				largest_area = area

	return largest_area


def main():
	red_tiles = read_file("input.txt")
	result = compute_largest_area(red_tiles)
	print(result)

if __name__ == "__main__":
	main()