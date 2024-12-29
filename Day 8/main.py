
def get_satellite_positions(data):
    satellite_positions = {}
    for row_i, row in enumerate(data):
        for col_i in range(len(row)):
            node = row[col_i]
            if not node == '.':
                if node in satellite_positions.keys():
                    satellite_positions[node].append((col_i,row_i))
                else:
                    satellite_positions[node] = [(col_i,row_i)]
    return satellite_positions


def get_unique_antinodes(data):
    col_count = len(data[0])
    row_count = len(data)
    unique_antinodes = set()
    satellite_positions = get_satellite_positions(data)
    for pos_list in satellite_positions.values():
        for i, pos in enumerate(pos_list):
            next_pos_list = pos_list[i+1:]
            for next_pos in next_pos_list:
                pos_x, pos_y = pos
                next_x, next_y = next_pos
                diff_x, diff_y = (pos_x-next_x, pos_y-next_y)
                if diff_x == 0 and diff_y == 0:
                    continue

                for x,y in [(diff_x, diff_y),(-diff_x, -diff_y)]:
                    antinode = (pos_x+x, pos_y+y)
                    if antinode not in pos_list and 0 <= antinode[0] < col_count and 0 <= antinode[1] < row_count:
                        unique_antinodes.add(antinode)
                for x,y in [(diff_x, diff_y),(-diff_x, -diff_y)]:
                    antinode = (next_x+x, next_y+y)
                    if antinode not in pos_list and 0 <= antinode[0] < col_count and 0 <= antinode[1] < row_count:
                        unique_antinodes.add(antinode)

    return unique_antinodes


def get_unique_antinodes_p2(data):
    col_count = len(data[0])
    row_count = len(data)
    unique_antinodes = set()
    satellite_positions = get_satellite_positions(data)
    for pos_list in satellite_positions.values():
        for i, pos in enumerate(pos_list):
            unique_antinodes.add(pos)
            next_pos_list = pos_list[i+1:]
            for next_pos in next_pos_list:
                pos_x, pos_y = pos
                next_x, next_y = next_pos
                diff_x, diff_y = (pos_x-next_x, pos_y-next_y)
                if diff_x == 0 and diff_y == 0:
                    continue
                antinode_x, antinode_y = pos
                while 0 <= antinode_x < col_count and 0 <= antinode_y < row_count:
                    antinode_x += diff_x
                    antinode_y += diff_y
                    if 0 <= antinode_x < col_count and 0 <= antinode_y < row_count:
                        unique_antinodes.add((antinode_x, antinode_y))
                antinode_x, antinode_y = pos
                while 0 <= antinode_x < col_count and 0 <= antinode_y < row_count:
                    antinode_x -= diff_x
                    antinode_y -= diff_y
                    if 0 <= antinode_x < col_count and 0 <= antinode_y < row_count:
                        unique_antinodes.add((antinode_x, antinode_y))
    print(unique_antinodes)
    return unique_antinodes              


def part_1(data):
    print(len(get_unique_antinodes(data)))


def part_2(data):
    print(len(get_unique_antinodes_p2(data)))


with open('input.txt', 'r') as file:
    data = [line.rstrip() for line in file.readlines()]
    part_1(data)
    part_2(data)