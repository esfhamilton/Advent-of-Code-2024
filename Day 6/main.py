from itertools import product

def parse_map(map_lines):
    directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
    grid = []
    guard_position = None
    guard_direction = None

    for y, line in enumerate(map_lines):
        row = []
        for x, char in enumerate(line):
            if char in directions:
                guard_position = (x, y)
                guard_direction = directions[char]
                row.append(".")  
            else:
                row.append(char)
        grid.append(row)

    return grid, guard_position, guard_direction


def turn_right(direction):
    dx, dy = direction
    return (-dy, dx)


def move(position, direction):
    x, y = position
    dx, dy = direction
    return x + dx, y + dy


def is_outside_grid(position, grid):
    x, y = position
    return y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0])


def get_distinct_positions(map_lines):
    grid, position, direction = parse_map(map_lines)

    distinct_positions = set()
    distinct_positions.add(position)
    
    while True:
        next_position = move(position, direction)
        if is_outside_grid(next_position, grid):
            break

        x, y = next_position
        if grid[y][x] == "#":
            direction = turn_right(direction)
        else:
            position = next_position
            distinct_positions.add(position)

    return distinct_positions


def part_1(data):
    print(len(get_distinct_positions(data)))


def get_looping_obstacle_positions(map_lines):
    looping_obstacle_positions = set()
    map_rows = len(map_lines)
    map_cols = len(map_lines[0])

    for row, col in list(product(range(map_rows), range(map_cols))):
        grid, position, direction = parse_map(map_lines)
        if not grid[row][col] == '.':
            continue
        else:
            grid[row][col] = '#'
        pos_vectors = set()
        loop_test_count = map_rows if map_rows > map_cols else map_cols
        while True:
            next_position = move(position, direction)
            if (position,direction) in pos_vectors:
                looping_obstacle_positions.add((row,col))
                break
            
            if is_outside_grid(next_position, grid):
                break
            
            x, y = next_position
            if grid[y][x] == "#":
                direction = turn_right(direction)
            else:
                pos_vectors.add((position,direction))
                position = next_position
                

    return looping_obstacle_positions


def part_2(data):
    print(len(get_looping_obstacle_positions(data)))
    
    
with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]
    part_1(data)
    part_2(data)
    
