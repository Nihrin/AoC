import numpy as np

with open('data.txt') as f:
    lines = f.read().splitlines()

for i in range(len(lines)):
    lines[i] = list(lines[i])
    for j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j])

forest = np.array(lines)
empty = forest.copy()
empty.fill(0)

rows = forest.shape[0]
cols = forest.shape[1]

for i in range(rows):
    left = -1
    right = -1
    for j in range(cols):
        if forest[i,j] > left:
            empty[i,j] = 1
            left = forest[i,j]
        if forest[rows-i-1,cols-j-1] > right:
            empty[rows-i-1,cols-j-1] = 1
            right = forest[rows-i-1,cols-j-1]

for i in range(cols):
    top = -1
    bottom = -1
    for j in range(rows):
        if forest[j,i] > top:
            empty[j,i] = 1
            top = forest[j,i]
        if forest[rows-j-1,cols-i-1] > bottom:
            empty[rows-j-1,cols-i-1] = 1
            bottom = forest[rows-j-1,cols-i-1]
        
print(empty.sum())