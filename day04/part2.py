import sys

overlappingPairs = 0
with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        elf = line.strip().split(',')
        r1 = [int(elf[0].split('-')[0]), int(elf[0].split('-')[1])]
        r2 = [int(elf[1].split('-')[0]), int(elf[1].split('-')[1])] 
        if(set([i for i in range(r1[0],r1[1]+1)]) & set([i for i in range(r2[0],r2[1]+1)])):
            overlappingPairs += 1

print(overlappingPairs)