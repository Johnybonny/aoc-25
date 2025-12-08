from itertools import groupby

def read_file(filename):
	junction_boxes = []
	with open(filename, "r") as file:
		for line in file:
			junction_boxes.append(list(map(int, line.split(","))))

	return junction_boxes


def create_distances_list(junction_boxes):
	distances_list = []
	for i in range(len(junction_boxes)):
		for j in range(i + 1, len(junction_boxes)):
			distance = ((junction_boxes[i][0] - junction_boxes[j][0]) ** 2 + (junction_boxes[i][1] - junction_boxes[j][1]) ** 2 + (junction_boxes[i][2] - junction_boxes[j][2]) ** 2) ** 1/2
			distances_list.append({"a": i, "b": j, "distance": distance})
	distances_list.sort(key=lambda x: x["distance"])

	return distances_list


def connect_junction_boxes(a, b, circuit_index, connected_matrix, circuit_participation):
	if circuit_participation[a] > 0 and circuit_participation[b] == 0:
			circuit_participation[b] = circuit_participation[a]
			for i in range(len(circuit_participation)):
				if circuit_participation[i] == circuit_participation[b]:
					connected_matrix[i][b] = 1
					connected_matrix[b][i] = 1

	elif circuit_participation[a] == 0 and circuit_participation[b] > 0:
		circuit_participation[a] = circuit_participation[b]
		for i in range(len(circuit_participation)):
			if circuit_participation[i] == circuit_participation[a]:
				connected_matrix[i][a] = 1
				connected_matrix[a][i] = 1

	elif circuit_participation[a] == 0 and circuit_participation[a] == 0:
		circuit_participation[a] = circuit_index
		circuit_participation[b] = circuit_index
		connected_matrix[a][b] = 1
		connected_matrix[b][a] = 1
		circuit_index += 1

	else:
		to_change = circuit_participation[a]
		for i in range(len(circuit_participation)):
			if circuit_participation[i] == to_change:
				circuit_participation[i] = circuit_participation[b]
		for i in range(len(circuit_participation)):
			if circuit_participation[i] == circuit_participation[a]:
				connected_matrix[i][a] = 1
				connected_matrix[a][i] = 1

	return circuit_index, connected_matrix, circuit_participation


def one_circuit_only(circuits):
	if circuits[0] == 0:
		return False
	g = groupby(circuits)
	return next(g, True) and not next(g, False)


def find_last_junction_product(junction_boxes):
	connected_matrix = [[0] * len(junction_boxes) for _ in range(len(junction_boxes))]
	distances_list = create_distances_list(junction_boxes)
	circuit_participation = [0] * len(junction_boxes)

	circuit_index = 1
	while not one_circuit_only(circuit_participation):
		shortest_connection = distances_list.pop(0)
		a = shortest_connection["a"]
		b = shortest_connection["b"]
		if not connected_matrix[a][b]:
			circuit_index, connected_matrix, circuit_participation = connect_junction_boxes(a, b, circuit_index, connected_matrix, circuit_participation)

	return junction_boxes[a][0] * junction_boxes[b][0]


def main():
	junction_boxes = read_file("input.txt")
	result = find_last_junction_product(junction_boxes)
	print(result)

if __name__ == "__main__":
	main()