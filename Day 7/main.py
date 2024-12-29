import operator
import itertools
from itertools import product


def get_calibration_results(equation, operators):
    eq_split = equation.replace(':', '').split(' ')
    target_result = int(eq_split[0])
    values = list(map(int, eq_split[1:]))
    num_operators = len(values) - 1
    
    OPERATORS = {'+': operator.add, '*': operator.mul}
    
    for combination in product(operators, repeat=num_operators):
        result = values[0]
        for num, op in zip(values[1:], combination):
            result = int(f"{result}{num}") if op == '|' else OPERATORS[op](result, num)
        
        if result == target_result:
            return target_result

    return 0


def part_1(data):
    operators = ['+', '*']
    print(sum(get_calibration_results(line, operators) for line in data))


def part_2(data):
    operators = ['+', '*', '|']
    print(sum(get_calibration_results(line, operators) for line in data))


with open('input.txt', 'r') as file:
    data = [line.rstrip() for line in file.readlines()]
    part_1(data)
    part_2(data)