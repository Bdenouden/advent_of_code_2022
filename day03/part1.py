import sys

lower = [c for c in range(ord('a'), ord('z')+1)]
upper = [C for C in range(ord('A'), ord('Z')+1)]

priorities =  lower + upper
d = {chr(x): i+1 for i, x in enumerate(priorities)}
print(d)
output = 0
with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        rucksack = line.strip()
        comp1 = rucksack[0:int(len(rucksack)/2)]
        comp2 = rucksack[int(len(rucksack)/2):]
        intersect = set(comp1) & set(comp2)
        output += d[list(intersect)[0]]
print(output)
        