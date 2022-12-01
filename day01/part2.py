import sys

highest = [0,0,0]
def checkHighest(val):
    if(cal > min(highest)):
        highest[highest.index(min(highest))] = val

with open(sys.path[0] + '/input.txt') as f:
    cal = 0
    for line in f:
        if line == "\n":
            checkHighest(cal)
            cal=0
        else:
            cal+=int(line.strip())

checkHighest(cal)
print(highest)
print(sum(highest))