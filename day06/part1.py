import sys

line = open(sys.path[0] + '/input.txt').read().strip()
for i in range(len(line[3:])):
    if len(set(line[i:i+4])) > 3:
        print(i+4)
        exit()