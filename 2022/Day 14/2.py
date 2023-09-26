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
y_range = (min(ys), max(ys) + 2)

sand_x = 500 - x_range[0]
sand_y = 0
pit = np.full(((y_range[1] + 1), (x_range[1] - x_range[0] + 1)), ".")
empty_col = np.array([["."]]*(y_range[1] + 1))
empty_col[-1][0] = "#"
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

for a in range(pit.shape[1]):
    pit[-1, a] = "#"

full = False
counter = 0
while not full:
    x = sand_x
    y = sand_y
    while True:
        if x == 0:
            pit = np.append(empty_col, pit, axis=1)
            x += 1
            sand_x += 1
        if x == pit.shape[1] - 1:
            pit = np.append(pit, empty_col, axis=1)

        if y + 1 > y_range[1]:
            print("Hole in ground...")
            full = True
            break
        elif pit[y+1, x] == ".":
            y += 1
        elif pit[y+1, x-1] == ".":
            y += 1
            x -= 1            
        elif pit[y+1, x+1] == ".":
            y += 1
            x += 1
        else:
            pit[y,x] = "o"
            counter += 1
            if x == sand_x and y == sand_y:
                full = True
            break
print(counter)