import re

def find_digit(part):
    return int(re.search('\d+', part).group())

def multiply_parts(mul):
    split = mul.split(',')
    return find_digit(split[0]) * find_digit(split[1])

def part_1(data):
    muls = re.findall(r'mul\(\d+,\d+\)', data)
    print(sum(multiply_parts(mul) for mul in muls))

def part_2(data):
    new_data = re.sub(r'don\'t\(\).*?do\(\)', 'do\(\)', data, flags=re.DOTALL)
    new_data = re.sub(r'don\'t\(\).*', '', new_data, flags=re.DOTALL)
    muls = re.findall(r'mul\(\d+,\d+\)', new_data)
    print(sum(multiply_parts(mul) for mul in muls))

with open('input.txt', 'r') as file:
    data = file.read()
    part_1(data)
    part_2(data)
    
        
    
        
