import numpy as np

with open('data.txt') as f:
    lines = f.read().splitlines()

for i in range(len(lines)):
    lines[i] = lines[i].split(" ")
    lines[i][1] = int(lines[i][1])

direction = {"U":[0,1], "D":[0,-1], "L":[-1,0], "R":[1,0]}

head = [0,0]
tail = [0,0]

def tail_movement(t, h):
    t_x = t[0]
    t_y = t[1]
    h_x = h[0]
    h_y = h[1]
    x_ = h_x - t_x
    y_ = h_y - t_y
    if abs(x_) <= 1 and abs(y_) <= 1:
        return 0, 0
    elif x_ == 0:
        y = (y_) / abs(y_)
        return 0, y
    elif y_ == 0:
        x = (x_) / abs(x_)
        return x, 0
    else:
        x = (x_) / abs(x_)
        y = (y_) / abs(y_)
        return x, y    


positions = [(0,0)]

for i in lines:
    for n in range(i[1]):
        head[0] += direction[i[0]][0]
        head[1] += direction[i[0]][1]
        x, y = tail_movement(tail, head)
        tail[0] += x
        tail[1] += y
        to_add = (tail[0], tail[1])
        if to_add not in positions:
            positions.append(to_add)

print(len(positions))