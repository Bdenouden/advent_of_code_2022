import sys

highest = 0

with open(sys.path[0] + '/input.txt') as f:
    cal = []
    for line in f:
        if line == "\n":
            highest = max(highest, sum(cal))
            cal=[]
        else:
            cal.append(int(line.strip()))

print(highest)