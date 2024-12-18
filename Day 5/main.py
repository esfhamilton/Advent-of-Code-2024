def get_valid_or_invalid_updates(rules, data, invalid_flag=False):
    valid_updates = []
    invalid_updates = []
    for update in data:
        update = update.replace('\n','')
        invalid_update = False
        seen_numbers = []
        for number in update.split(','):
            number = int(number)
            for rule in rules:
                rule = rule.replace('\n','')
                rule_split = rule.split('|')
                if number == int(rule_split[0]) and int(rule_split[1]) in seen_numbers:
                    invalid_update = True
            seen_numbers.append(number)
        if not invalid_update:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    if invalid_flag:
        return invalid_updates
    return valid_updates
    

def part_1(rules, data):
    print(sum(int(update.split(',')[len(update.split(','))//2])
              for update in get_valid_or_invalid_updates(rules, data)))


def swap_required(numbers, index, rules):
    if index == len(numbers):
        return False

    current_num = numbers[index]
    remaining_nums = numbers[index+1:]
    
    invalid_remaining_nums = [int(rule.replace('\n','').split('|')[0]) for rule in rules if int(rule.replace('\n','').split('|')[1]) == current_num]
    return any(num in remaining_nums for num in invalid_remaining_nums)


def swap_with_next_element(numbers, index):
    numbers[index], numbers[index+1] = numbers[index+1], numbers[index]


def fix_updates(rules, updates):
    fixed_updates = []
    for update in updates:
        numbers = list(map(int,update.split(',')))
        for i in range(len(numbers)-1):
            for j in range(len(numbers)-1):
                if swap_required(numbers, j, rules):
                    swap_with_next_element(numbers, j)

        fixed_updates.append(numbers)
    return fixed_updates

     
def part_2(rules, data):
    invalid_updates = get_valid_or_invalid_updates(rules, data, True)
    print(sum(int(update[len(update)//2]) for update in fix_updates(rules, invalid_updates)))

    
with open('input.txt', 'r') as file:
    rules = []
    inputs = []
    for line in file.readlines():
        if '|' in line:
            rules.append(line)
        elif ',' in line:
            inputs.append(line)
    
    part_1(rules, inputs)
    part_2(rules, inputs)
