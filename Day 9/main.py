from pathlib import Path

def get_disk_blocks(data):
    disk_blocks = []
    for i, val in enumerate(data):
        disk_blocks += [int(i/2)] * int(val) if i % 2 == 0 else ['.'] * int(val)
    return disk_blocks


def sort_disk_blocks(disk_blocks):
    left_pointer = 0
    right_pointer = len(disk_blocks) - 1

    while left_pointer < right_pointer:
        while left_pointer < len(disk_blocks) and disk_blocks[left_pointer] != '.':
            left_pointer += 1
        
        while right_pointer >= 0 and disk_blocks[right_pointer] == '.':
            right_pointer -= 1

        if left_pointer < right_pointer:
            disk_blocks[left_pointer], disk_blocks[right_pointer] = disk_blocks[right_pointer], '.'
            left_pointer += 1
            right_pointer -= 1


def get_checksum(disk_blocks):
    return sum(i*int(val) for i, val in enumerate(disk_blocks) if not val == '.')


def part_1(data):
    disk_blocks = get_disk_blocks(data)
    sort_disk_blocks(disk_blocks)
    print(get_checksum(disk_blocks))


def swap_spaces(left, right, block_size, disk_blocks):
    for i in range(block_size):
        disk_blocks[left+i], disk_blocks[right+i] = disk_blocks[right+i], '.'
    

def sort_without_fragmentation(disk_blocks):
    left_pointer = 0
    right_pointer = len(disk_blocks) - 1
    current_value = None

    while right_pointer > 0:
        left_pointer = 0
        while right_pointer >= 0 and disk_blocks[right_pointer] == '.':
            right_pointer -= 1
        
        block_size = 0
        current_value = disk_blocks[right_pointer]
        while right_pointer >= 0 and disk_blocks[right_pointer] == current_value:
            block_size += 1
            right_pointer -= 1
        while left_pointer < right_pointer+1:
            if all(disk_blocks[left_pointer+i] == '.' for i in range(block_size)):
                swap_spaces(left_pointer, right_pointer+1, block_size, disk_blocks)
                break
            else:
                left_pointer += 1


def part_2(data):
    disk_blocks = get_disk_blocks(data)
    sort_without_fragmentation(disk_blocks)
    print(get_checksum(disk_blocks))

data = Path("input.txt").read_text()
part_1(data)
part_2(data)
