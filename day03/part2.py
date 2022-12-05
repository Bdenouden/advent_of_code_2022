import sys

lower = [c for c in range(ord('a'), ord('z')+1)]
upper = [C for C in range(ord('A'), ord('Z')+1)]

priorities =  lower + upper
d = {chr(x): i+1 for i, x in enumerate(priorities)}
output = 0
group = []
with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        group.append(line.strip())
        if len(group) == 3:
            badge = set(group[0]) & set(group[1]) & set(group[2])
            output += d[list(badge)[0]]
            group = []
print(output)
        