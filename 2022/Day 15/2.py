import numpy as np
import re

with open('data.txt') as f:
    lines = f.read().splitlines()

sensors = []
beacons = []
closest_beacon = {}
for line in lines:
    x = [int(d) for d in re.findall(r'-?\d+', line)]
    sensors += [(x[1], x[0])]
    beacons += [(x[3], x[2])]
    closest_beacon[(x[1], x[0])] = (x[3], x[2])

man_dist = {}
for sensor in sensors:
    distance = (abs(sensor[0] - closest_beacon[(sensor)][0]) + abs(sensor[1] - closest_beacon[(sensor)][1]))
    man_dist[(sensor[0], sensor[1])] = distance

sensors = sorted(list(man_dist.items()), key=lambda x: x[1], reverse=True)
sensors = [x[0] for x in sensors]

rows = 4000000
cols = 4000000

for row in range(rows):
    col = 0
    if row % 100000 == 0:
        print(row)
    while col < cols:
        checked = []
        for s in sensors:
            if abs(col - s[1]) + abs(row - s[0]) <= man_dist[s]:
                if col > s[1]:
                    col += (man_dist[s] - abs(row - s[0]) - abs(col - s[1]) + 1)
                    break
                elif col < s[1]:
                    col += (man_dist[s] - abs(row - s[0]) + abs(col - s[1]) + 1)
                    break
                elif col == s[1]:
                    col += (man_dist[s] - abs(row - s[0]) + 1)
                    break

            checked.append(s)
        if len(checked) == len(sensors):
            print(col*cols+row)
            exit()