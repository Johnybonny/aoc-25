import copy

def read_file(filename):
	ranges = []
	with open(filename, "r") as file:
		for line in file:
			if line.split() == []:
				break
			else:
				range_arr = list(map(int, line.split("-")))
				ranges.append({"left": range_arr[0], "right": range_arr[1]})
	return ranges


def are_overlapping(range1, range2):
	return not (range1["right"] < range2["left"] or range2["right"] < range1["left"])


def combine_overlapping_ranges(range1, range2):
	if range1["left"] <= range2["left"]:
		if range1["right"] >= range2["right"]: # [1,5] + [2,4]
			return range1
		else: # [1,5] + [4,7]
			return {"left": range1["left"], "right": range2["right"]}
	else:
		if range2["right"] >= range1["right"]: # [2,4] + [1,5]
			return range2
		else: # [4,7] + [1,5]
			return {"left": range2["left"], "right": range1["right"]}


def test_ranges():
	print("\"Testy\"")
	print("[1,5] + [2,4]:", combine_overlapping_ranges({"left": 1, "right": 5}, {"left": 2, "right": 4}))
	print("[2,4] + [1,5]:", combine_overlapping_ranges({"left": 2, "right": 4}, {"left": 1, "right": 5}))
	print("[1,5] + [4,7]:", combine_overlapping_ranges({"left": 1, "right": 5}, {"left": 4, "right": 7}))
	print("[4,7] + [1,5]:", combine_overlapping_ranges({"left": 4, "right": 7}, {"left": 1, "right": 5}))
	print("[1,5] + [2,4] overlapping:", are_overlapping({"left": 1, "right": 5}, {"left": 2, "right": 4}))
	print("[2,4] + [1,5] overlapping:", are_overlapping({"left": 2, "right": 4}, {"left": 1, "right": 5}))
	print("[1,5] + [4,7] overlapping:", are_overlapping({"left": 1, "right": 5}, {"left": 4, "right": 7}))
	print("[4,7] + [1,5] overlapping:", are_overlapping({"left": 4, "right": 7}, {"left": 1, "right": 5}))
	print("[1,5] + [6,7] overlapping:", are_overlapping({"left": 1, "right": 5}, {"left": 6, "right": 7}))
	print("[6,8] + [1,4] overlapping:", are_overlapping({"left": 6, "right": 8}, {"left": 1, "right": 4}))


def combine_ranges(ranges):
	combined = [ranges[0]]
	for r in ranges[1:]:
		overlapping_ranges = []
		for c in combined:
			if are_overlapping(c, r):
				overlapping_ranges.append(c)

		new_range = r
		new_combined = []
		for o_r in overlapping_ranges:
			new_range = combine_overlapping_ranges(new_range, o_r)

		for c in combined:
			if c not in overlapping_ranges:
				new_combined.append(c)

		new_combined.append(new_range)

		combined = copy.deepcopy(new_combined)

	return combined



def count_fresh(ranges):
	combined = combine_ranges(ranges)
	fresh = 0
	for c in combined:
		fresh += c["right"] - c["left"] + 1

	return fresh


def main():
	# test_ranges()
	ranges = read_file("input.txt")
	result = count_fresh(ranges)
	print(result)

if __name__ == "__main__":
	main()