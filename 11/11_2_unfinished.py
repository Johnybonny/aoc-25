def read_file(filename):
	devices = {}
	with open(filename, "r") as file:
		for line in file:
			devices[line.split(":")[0]] = line.replace("\n","").split(":")[1][1:].split(" ")

	return devices


def count_paths(device, end, all_devices):
	# if device != end:
	# 	print(device, all_devices[device])
	if device == end:
		return 1
	elif len(all_devices[device]) == 0:
		return 0
	else:
		new_paths = 0
		for child in all_devices[device]:
			new_paths += count_paths(child, end, all_devices)
		return new_paths


def find_paths(device, end, all_devices):
	if device != end:
		print(device, all_devices[device])
	if device == end:
		return 1
	elif len(all_devices[device]) == 0:
		return 0
	else:
		new_paths = 0
		for child in all_devices[device]:
			new_paths += count_paths(child, end, all_devices)
		return new_paths


def count_correct_paths(device, end, all_devices):
	return 0


def main():
	devices = read_file("input.txt")
	result = count_paths("svr", "out", devices)
	print(result)

if __name__ == "__main__":
	main()