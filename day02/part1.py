import sys
import numpy as np

# opponent = {'A': "rock",'B': "paper", "C":"scissors"}
# you = {'X': "rock", "Y":"paper", "Z": "scissors"}

opponent = {'A': 1,'B': 2, "C":3}
you = {'X': 1, "Y":2, "Z": 3}

finalScore = np.array([0,0])

# arguments are o = opponent hand and y = your hand.
# returns the score as [opponent, you]
def getMatchResult(o, y):
    # print(f"o = {o}, y = {y}")
    score = np.array([opponent[o], you[y]])
    if(opponent[o] == you[y]):
        return score + [3,3]
    elif ((o =='A' and y =="Y") or (o == "B" and y =="Z") or (o == 'C' and y =="X")): # you won
        return score + [0, 6]
    elif ((o =='A' and y =="Z") or (o == "B" and y =="X") or (o == 'C' and y =="Y")): # you lost
        return score + [6, 0]

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        hands = line.strip().split()
        result = getMatchResult(hands[0], hands[1])
        finalScore += result
        # print(result)
        # print()

print(finalScore)
        