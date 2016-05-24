def count_hits(position):
	"""find maximum hits possible for the given direction"""
	hits = (len(hit_positions.intersection(get_all_hit_pos(position, direction))) 
			for direction in DIRECTIONS)
	return max(hits)

def get_all_hit_pos(position, direction):
	"""generator that returns all positions hit by a beam"""
	current_pos = list(position)

	while 0 <= current_pos[0] <= max_y and 0 <= current_pos[1] <= max_x:

		yield tuple(current_pos)
		for side_direction in DIRECTIONS:
			yield current_pos[0] + side_direction[0], current_pos[1] + side_direction[1]

		if tuple(current_pos) in hit_positions: # stop when laser hits a zombie
			break

		current_pos[0] += direction[0]
		current_pos[1] += direction[1]

with open('input.txt') as file:
	max_y, max_x = next(file).split()
	max_y, max_x = int(max_y), int(max_x)
	hit_positions = {(int(y), int(x)) for y, x in (line.split() for line in file)}

# max(position, key = number of hits)
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1))
all_pos = ((y,x) for y in range(max_y) for x in range(max_x) if (y, x) not in hit_positions)
max_pos = max(all_pos, key = count_hits)

print ("{0} hits at position {1}".format(count_hits(max_pos), max_pos))
