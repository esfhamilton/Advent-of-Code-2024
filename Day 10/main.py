def get_trailhead_score(data, distinct_trails):
    def in_range(new_y, new_x):
        return True if 0 <= new_y < rows and 0 <= new_x < cols else False


    def get_trails_from_start_pos(y,x,trail_pos,end_positions,distinct_trails):
        trails_from_current_pos = 0
        for dy,dx in directions:
            new_y, new_x = (dy+y, dx+x)
            if in_range(new_y, new_x):
                next_trail_pos = data[new_y][new_x]
                if next_trail_pos == trail_pos + 1:
                    if next_trail_pos == 9 and ((new_y,new_x) not in end_positions or distinct_trails):
                        if not distinct_trails:
                            end_positions.add((new_y,new_x))
                        trails_from_current_pos += 1
                    else:
                        trails_from_current_pos += get_trails_from_start_pos(new_y, new_x, next_trail_pos,end_positions, distinct_trails)
        
        return trails_from_current_pos

        
    trailhead_score = 0
    rows, cols = len(data), len(data[0])
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    start_positions = [(y, x) for y in range(rows) for x in range(cols) if data[y][x] == 0]
    for y,x in start_positions:
        end_positions = set()
        trailhead_score += get_trails_from_start_pos(y,x,0,end_positions,distinct_trails)
    
    return trailhead_score


def part_1(data):
    print("Score: ", get_trailhead_score(data, False))


def part_2(data):
    print("Score: ", get_trailhead_score(data, True))

    
with open ('input.txt', 'r') as file:
    data = [[int(x) for x in line.rstrip()] for line in file.readlines()]
    part_1(data)
    part_2(data)