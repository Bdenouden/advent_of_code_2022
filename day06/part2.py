import sys

line = open(sys.path[0] + '/input.txt').read().strip()
for i in range(len(line[13:])):
    if len(set(line[i:i+14])) > 13:
        print(i+14)
        exit()