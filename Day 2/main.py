def is_safe(report):
    incrementing = False
    decrementing = False
    previous_level = report[0]

    for level in report[1:]:
        if level > previous_level:
            incrementing = True
        if level < previous_level:
            decrementing = True
        if not (1 <= abs(level-previous_level) <= 3):
            return False
        previous_level = level
    return not(incrementing and decrementing)

def part_1(reports):
    print(sum(1 for report in reports if is_safe(report)))

def get_tolerated_reports(report):
    reports = [[level for index, level in enumerate(report) if index != i] for i in range(len(report))]
    reports.append(report)
    return reports

def part_2(reports):
    print(sum(1 for report in reports if any(is_safe(r) for r in get_tolerated_reports(report))))
    
with open('input.txt', 'r') as file:
    reports = [list(map(int,line.split())) for line in file]
    part_1(reports)
    part_2(reports)
    
        
        
    
        
