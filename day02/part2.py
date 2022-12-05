import sys
import numpy as np

# opponent = {'A': "rock",'B': "paper", "C":"scissors"}
# you = {'X': "rock", "Y":"paper", "Z": "scissors"}

opponent = {'A': 1,'B': 2, "C":3}
keys = list(opponent.keys())
# goal = {'X': 'lose', "Y":'draw', "Z": 'win'}
goal = {'X': 1, "Y":2, "Z": 3}

finalScore = np.array([0,0])

# arguments are o = opponent hand and g = goal of the match.
# returns the score as [opponent, you]
def getMatchResult(o, g):
    opIndex = keys.index(o)
    if(g =="X"): # lose
        y = keys[opIndex-1]
        score = np.array([6,0])
    elif(g=="Y"): #draw
        y = o
        score = np.array([3,3])
    elif(g=="Z"): # win
        y = keys[(opIndex+1)%3]
        score = np.array([0, 6])
    # No else to catch errors
    return score + [opponent[o], opponent[y]]

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        hands = line.strip().split()
        result = getMatchResult(hands[0], hands[1])
        finalScore += result
        # print(result)
        # print()

print(finalScore)
        