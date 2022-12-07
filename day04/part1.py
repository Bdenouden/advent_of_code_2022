import sys

overlappingPairs = 0
with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        elf = line.strip().split(',')
        s1 = [int(elf[0].split('-')[0]), int(elf[0].split('-')[1])]
        s2 = [int(elf[1].split('-')[0]), int(elf[1].split('-')[1])] 
        if(s1[0]>=s2[0] and s1[1]<=s2[1]):
            overlappingPairs += 1
        elif(s2[0]>=s1[0] and s2[1]<=s1[1]):
            overlappingPairs += 1

print(overlappingPairs)

        