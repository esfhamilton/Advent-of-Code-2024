with open('input.txt', 'r') as file:
    data = [map(int, line.split()) for line in file]        
    l1, l2 = zip(*data)
    l1, l2 = sorted(l1), sorted(l2)

    distance = sum(abs(item - item2) for item, item2 in zip(l1, l2))
    score = sum(item * l2.count(item) for item in l1)
   
    print(distance)
    print(score)
        
