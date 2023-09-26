import string

with open('data.txt') as f:
    lines = f.read().splitlines()

input = lines[:9]
data = lines[10:]

stacks = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}

for i in range(8):
    for s in range(9):
        if input[7-i][(s*4)+1] != " ":
            stacks[s+1] += input[7-i][(s*4)+1]

for i in range(len(data)):
    data[i] = data[i].replace("move", "")
    data[i] = data[i].replace("from", "")
    data[i] = data[i].replace("to", "")
    data[i] = data[i].split(" ")
    data[i] = list(filter(None, data[i]))
    data[i] = [int(x) for x in data[i]]

for move in data:
    stack = []
    for z in range(move[0]):
        stack.append(stacks[move[1]][-1])
        stacks[move[1]] = stacks[move[1]][:-1]
    stack.reverse()
    stacks[move[2]] += stack

print(stacks)