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

def check_col(i, j):
    if i == cols-1 or i == 0:
        return 0
    else:
        height = forest[i,j]
        top = 0
        bot = 0
        for x in range(i):
            top += 1
            if forest[i-x-1,j] >= height:
                break
        for x in range(i+1, rows):
            bot += 1
            if forest[x,j] >= height:
                break
    return top*bot

def check_row(i, j):
    if j == cols-1 or j == 0:
        return 0
    else:
        height = forest[i,j]
        left = 0
        right = 0
        for x in range(j):
            left += 1
            if forest[i,j-x-1] >= height:
                break
        for x in range(j+1, cols):
            right += 1
            if forest[i,x] >= height:
                break
    return right*left

for i in range(rows):
    for j in range(cols):
        total = check_col(i,j) * check_row(i,j)
        empty[i,j] = total
    
print(empty.max())