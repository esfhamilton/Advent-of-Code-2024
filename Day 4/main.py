letters = ['X','M','A','S']

def check_left(row, col, grid):
    return all(grid[row][col-i] == letters[i] for i in range(len(letters)))
    
def check_right(row, col, grid):
    return all(grid[row][col+i] == letters[i] for i in range(len(letters)))

def check_up(row, col, grid):
    return all(grid[row-i][col] == letters[i] for i in range(len(letters)))

def check_down(row, col, grid):
    return all(grid[row+i][col] == letters[i] for i in range(len(letters)))

def check_up_left(row, col, grid):
    return all(grid[row-i][col-i] == letters[i] for i in range(len(letters)))

def check_up_right(row, col, grid):
    return all(grid[row-i][col+i] == letters[i] for i in range(len(letters)))

def check_down_left(row, col, grid):
    return all(grid[row+i][col-i] == letters[i] for i in range(len(letters)))

def check_down_right(row, col, grid):
    return all(grid[row+i][col+i] == letters[i] for i in range(len(letters)))
            

def check_directions(row, col, grid):
    num_cols = len(grid[0])
    num_rows = len(grid)
    words_found_from_pos = 0
    if col >= 3:
        if check_left(row,col,grid):
            words_found_from_pos += 1
    if col <= num_cols-4:
        if check_right(row,col,grid):
            words_found_from_pos += 1
    if row >= 3:
        if check_up(row,col,grid):
            words_found_from_pos += 1
        if col >= 3:
            if check_up_left(row,col,grid):
                words_found_from_pos += 1
        if col <= num_cols - 4:
            if check_up_right(row,col,grid):
                words_found_from_pos += 1
    if row <= num_rows - 4:
        if check_down(row,col,grid):
            words_found_from_pos += 1
        if col >= 3:
            if check_down_left(row,col,grid):
                words_found_from_pos += 1
        if col <= num_cols - 4:
            if check_down_right(row,col,grid):
                words_found_from_pos += 1
      
    return words_found_from_pos

def part_1(grid):
    row_index = 0
    words_found = 0
    for line in grid:
        col_index = 0
        for c in line:
            words_found += check_directions(row_index, col_index, grid)
            col_index += 1
        row_index += 1
    print(words_found)

def check_x_mas(row,col,grid):
    if row == 0 or col == 0 or row == len(grid)-1 or col == len(grid[0])-1:
        return 0
    wraps = [('M','S'), ('S','M')]
    diagonal_1 = (grid[row-1][col-1], grid[row+1][col+1])
    diagonal_2 = (grid[row-1][col+1], grid[row+1][col-1])
    return int(any(diagonal_1 == wrap for wrap in wraps)
               and any(diagonal_2 == wrap for wrap in wraps))

def part_2(grid):
    row_index = 0
    x_mas_found = 0
    for line in grid:
        col_index = 0
        for c in line:
            if c == 'A':
                x_mas_found += check_x_mas(row_index, col_index, grid)
            col_index += 1
        row_index += 1
    print(x_mas_found)
    
with open('input.txt', 'r') as file:
    wordsearch = [line for line in file.readlines()]
    part_1(wordsearch)
    part_2(wordsearch)
    
        
    
        
