import numpy as np

with open('data.txt') as f:
    lines = f.read().splitlines()

xs = []
ys = []

for i in range(len(lines)):
    lines[i] = lines[i].split(" -> ")
    for j in range(len(lines[i])):
        lines[i][j] = lines[i][j].split(",")
        lines[i][j][0] = int(lines[i][j][0])
        lines[i][j][1] = int(lines[i][j][1])
        xs.append(lines[i][j][0])
        ys.append(lines[i][j][1])

x_range = (min(xs), max(xs))
y_range = (min(ys), max(ys))

sand_x = 500 - x_range[0]
sand_y = 0
pit = np.full(((y_range[1] + 1), (x_range[1] - x_range[0] + 1)), ".")
pit[sand_y, sand_x] = "+"

for line in lines:
    for i in range(len(line)-1):
        x_rock = line[i][0] - x_range[0]
        y_rock = line[i][1]
        if line[i+1][0] != line[i][0]:
            for z in range(abs(line[i+1][0] - line[i][0])+1):
                p = int(z * ((line[i+1][0] - line[i][0]) / abs(line[i+1][0] - line[i][0])))
                pit[y_rock, x_rock + p] = "#"
        elif line[i+1][1] != line[i][1]:
            for a in range(abs(line[i+1][1] - line[i][1])+1):
                q = int(a * ((line[i+1][1] - line[i][1]) / abs(line[i+1][1] - line[i][1])))
                pit[y_rock + q, x_rock] = "#"

overflowing = False
counter = 0
while not overflowing:
    x = sand_x
    y = sand_y
    while True:
        if y + 1 > y_range[1]:
            overflowing = True
            break
        elif pit[y+1, x] == ".":
            y += 1
        elif x - 1 < 0:
            overflowing = True
            break
        elif pit[y+1, x-1] == ".":
            y += 1
            x -= 1
        elif x + 1 > x_range[1] - x_range[0] + 1:
            overflowing = True
            break
        elif pit[y+1, x+1] == ".":
            y += 1
            x += 1
        else:
            pit[y,x] = "o"
            counter += 1
            break
print(pit, counter)