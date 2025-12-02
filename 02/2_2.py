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
			id_len = len(id)
			for seq_len in range(1, id_len//2 + 1):
				if id_len % seq_len == 0:
					num_of_seq = id_len // seq_len
					are_equal = True
					start = 0
					for _ in range(num_of_seq - 1):
						if id[start : start + id_len//num_of_seq] != id[start + id_len//num_of_seq : start + id_len//num_of_seq + id_len//num_of_seq]:
							are_equal = False
							break
						else:
							start += id_len//num_of_seq

					if are_equal:
						sum += i
						break
	return sum


def main():
	ranges = read_file("input.txt")
	result = compute_invalid_sum(ranges)
	print(result)

if __name__ == "__main__":
	main()