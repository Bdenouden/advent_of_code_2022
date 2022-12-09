import sys

forest = {}

with open(sys.path[0] + '/test.txt') as f:
    for y, line in enumerate(f):
        for x, val in enumerate(line.strip()):
            forest[(y,x)] = int(val)

print(forest)
        