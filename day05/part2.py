import sys
import re

numStacks = 9
stackHeight = 8
stacks = { i:[] for i in range(numStacks) } # stacks[i][0] contains the topmost crate, stacks[]

def move(num, From, to):
    crates = stacks[From-1][0:num] + stacks[to-1]
    stacks[to-1] = crates
    stacks[From-1] = stacks[From-1][num:]

    # for i in range(num):
    #     crate = stacks[From-1].pop(0)
    #     stacks[to-1].insert(0,crate)

def printStacks():
    for i in range(numStacks):
        print(f"{i+1}: {stacks[i]}")
    print()

with open(sys.path[0] + '/input.txt') as f:
    for n, line in enumerate(f):
        if n < stackHeight: # buildup of the stacks
            line = line.strip("\n")
            # crates = [line[4*i+1] for i in range(numStacks)]
            for stack in range(numStacks):
                c = line[4*stack+1]
                if c != ' ' : stacks[stack].append(c)
            # print(stacks)
        elif n > stackHeight and line != "\n": # movement
            nums = [int(i) for i in re.findall("\d+", line)]
            # print(f"-> {line.strip()} = {nums}")
            # print("before:")
            # printStacks()
            move(nums[0], nums[1], nums[2])
            # print("after")
            # printStacks()
            # print('----------------')

# print(stacks)
print("".join([stacks[i][0] for i in range(numStacks)]))


        