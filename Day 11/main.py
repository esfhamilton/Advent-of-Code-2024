from pathlib import Path
from collections import deque


def blink(stone_counts):
    new_stone_counts = {}
    for stone in stone_counts.keys():
        if stone == '0':
            new_stone_counts['1'] = new_stone_counts.get('1', 0) + stone_counts[stone]
        elif len(stone) % 2 == 0:
            half = len(stone) // 2
            half_1, half_2 = str(int(stone[:half])), str(int(stone[half:]))
            new_stone_counts[half_1] = new_stone_counts.get(half_1, 0) + stone_counts[stone]
            new_stone_counts[half_2] = new_stone_counts.get(half_2, 0) + stone_counts[stone]
        else:
            key = str(int(stone) * 2024)
            new_stone_counts[key] = new_stone_counts.get(key, 0) + stone_counts[stone]
    
    return new_stone_counts


def part_1(data):
    stone_counts = {}
    for stone in data:
        stone_counts[stone] = stone_counts.get(stone,1)
    for _ in range(25):
        stone_counts = blink(stone_counts)
    print(sum(stone_counts.values()))


def part_2(data):
    stone_counts = {}
    for stone in data:
        stone_counts[stone] = stone_counts.get(stone,1)
    for _ in range(75):
        stone_counts = blink(stone_counts)
    print(sum(stone_counts.values()))

    
data = Path('input.txt').read_text().split(' ')
part_1(data)
part_2(data)