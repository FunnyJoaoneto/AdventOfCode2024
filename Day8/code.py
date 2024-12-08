from time import perf_counter_ns
from itertools import combinations

with open("input.txt","r") as file:
    data = file.read().splitlines()

start_positions_list = perf_counter_ns()

positions = {}

maxy = len(data)
maxx = len(data[0])


y=0
while y < len(data):
    x=0
    while x < len(data[y]):
        element = data[y][x]
        if element not in positions and element != ".":
            positions[element] = [[x,y]]
        elif element in positions:
            positions[element].append([x,y])
        x+=1
    y+=1

antinodes = set()

time_positions_list = round((perf_counter_ns() - start_positions_list),2) / 1e6

def check_out_of_bounds(pos):
    if pos[0] >= maxx or pos[0] < 0:
        return False
    if pos[1] >= maxy or pos[1] < 0:
        return False
    return True

start_p1 = perf_counter_ns()


for node, nodepos in positions.items():
    combos = [pair for pair in combinations(nodepos, 2)]
    for combo in combos:
        pos1 = combo[0]
        pos2 = combo[1]
        difference = [pos1[0]-pos2[0],pos1[1]-pos2[1]]
        difference_reverse = [pos2[0]-pos1[0],pos2[1]-pos1[1]]
        antinode = (pos1[0]+difference[0], pos1[1]+difference[1])
        antinode_reverse = (pos2[0]+difference_reverse[0], pos2[1]+difference_reverse[1])
        if check_out_of_bounds(antinode):
            antinodes.add(antinode)
        if check_out_of_bounds(antinode_reverse):
            antinodes.add(antinode_reverse)

print(len(antinodes))
time_p1 = round((perf_counter_ns() - start_p1),2) / 1e6
print("Time taken:", time_p1, "ms")
print("Time taken + positions_list:", time_p1 + time_positions_list, "ms")


#-------------------Part2-------------------

start_p1 = perf_counter_ns()

antinodes = set()

for node, nodepos in positions.items():
    combos = [pair for pair in combinations(nodepos, 2)]
    if len(nodepos)>1:
        for coord in nodepos:
            antinodes.add(tuple(coord))
    for combo in combos:
        pos1 = combo[0]
        pos2 = combo[1]
        difference = [pos1[0]-pos2[0],pos1[1]-pos2[1]]
        difference_reverse = [pos2[0]-pos1[0],pos2[1]-pos1[1]]
        antinode = (pos1[0]+difference[0], pos1[1]+difference[1])
        antinode_reverse = (pos2[0]+difference_reverse[0], pos2[1]+difference_reverse[1])
        while check_out_of_bounds(antinode):
            antinodes.add(antinode)
            antinode = (antinode[0]+difference[0], antinode[1]+difference[1])
        while check_out_of_bounds(antinode_reverse):
            antinodes.add(antinode_reverse)
            antinode_reverse = (antinode_reverse[0]+difference_reverse[0], antinode_reverse[1]+difference_reverse[1])

print(len(antinodes))
time_p1 = round((perf_counter_ns() - start_p1),2) / 1e6
print("Time taken:", time_p1, "ms")
print("Time taken + positions_list:", time_p1 + time_positions_list, "ms")

