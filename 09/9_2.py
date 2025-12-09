def read_file(filename):
	red_tiles = []
	with open(filename, "r") as file:
		for line in file:
			red_tiles.append({"x": int(line.split(",")[0]), "y": int(line.split(",")[1])})

	return red_tiles


def find_green_borders(red_tiles):
	vertical_borders = []
	horizontal_borders = []
	for tile_index in range(len(red_tiles) - 1):
		a = red_tiles[tile_index]
		b = red_tiles[tile_index + 1]
		if a["x"] == b["x"]:
			vertical_borders.append({"line_pos": a["x"], "start": min(a["y"], b["y"]), "end": max(a["y"], b["y"])})
		else: # a["y"] == b["y"]
			horizontal_borders.append({"line_pos": a["y"], "start": min(a["x"], b["x"]), "end": max(a["x"], b["x"])})

	# Last and first tiles
	a = red_tiles[-1]
	b = red_tiles[0]
	if a["x"] == b["x"]:
		vertical_borders.append({"line_pos": a["x"], "start": min(a["y"], b["y"]), "end": max(a["y"], b["y"])})
	else: # a["y"] == b["y"]
		horizontal_borders.append({"line_pos": a["y"], "start": min(a["x"], b["x"]), "end": max(a["x"], b["x"])})

	return vertical_borders, horizontal_borders


def is_tile_green(point, vertical_borders, horizontal_borders):
	for border in horizontal_borders:
		if border["line_pos"] == point["y"] and border["start"] <= point["x"] and border["end"] >= point["x"]:
			return True  # on horizontal border

	count_vertical = 0
	for border in vertical_borders:
		if border["line_pos"] == point["x"] and border["start"] <= point["y"] and border["end"] >= point["y"]:
			return True # on vertical border
		elif border["line_pos"] < point["x"] and border["start"] <= point["y"] and border["end"] > point["y"]:
			count_vertical += 1

	return count_vertical % 2 == 1


def are_all_tiles_green(a, b, vertical_borders, horizontal_borders):
	for v in vertical_borders:
		if min(a["x"], b["x"]) < v["line_pos"] < max(a["x"], b["x"]):
			if min(a["y"], b["y"]) < v["end"] and v["start"] < max(a["y"], b["y"]):
				return False

	for h in horizontal_borders:
		if min(a["y"], b["y"]) < h["line_pos"] < max(a["y"], b["y"]):
			if min(a["x"], b["x"]) < h["end"] and h["start"] < max(a["x"], b["x"]):
				return False

	# Is actually any tile green?
	middle_point = {"x": (min(a["x"], b["x"]) + max(a["x"], b["x"])) // 2, "y": (min(a["y"], b["y"]) + max(a["y"], b["y"])) // 2}
	return is_tile_green(middle_point, vertical_borders, horizontal_borders)


def all_areas(red_tiles):
	areas = []
	for i in range(len(red_tiles)):
		for j in range(i + 1, len(red_tiles)):
			area = (abs(red_tiles[i]["x"] - red_tiles[j]["x"]) + 1) * (abs(red_tiles[i]["y"] - red_tiles[j]["y"]) + 1)
			areas.append({"area": area, "a": red_tiles[i], "b": red_tiles[j]})

	return areas


def compute_largest_area(red_tiles):
	vertical_borders, horizontal_borders = find_green_borders(red_tiles)

	areas = all_areas(red_tiles)
	areas_sorted = sorted(areas, key=lambda x: -x["area"])

	for area in areas_sorted:
		if are_all_tiles_green(area["a"], area["b"], vertical_borders, horizontal_borders):
			return area["area"]

	return -1


def main():
	red_tiles = read_file("input.txt")
	result = compute_largest_area(red_tiles)
	print(result)

if __name__ == "__main__":
	main()