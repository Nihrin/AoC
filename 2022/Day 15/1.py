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

def check_sensors(row):
    possible_sensors = []
    for sensor in sensors:
        if (sensor[0] < row and sensor[0] + man_dist[sensor] >= row) or (sensor[0] > row and sensor[0] - man_dist[sensor] <= row):
            possible_sensors.append(sensor)
    return possible_sensors

def check_row(row, sens):
    covered = []
    for s in sens:
        d = man_dist[s]
        if s[0] > row:
            delta = s[0] - row - 1
        elif s[0] < row:
            delta = row - s[0] - 1
        else:
            delta = 0
        d -= delta

        tile = (row, s[1])
        if tile not in covered and tile not in beacons:
            covered.append(tile[1])
        if d > 0:
            for i in range(d):
                tile_ = (row, s[1]+i)
                _tile = (row, s[1]-i)
                if tile_ not in beacons:
                    covered.append(tile_[1])
                if _tile not in beacons:
                    covered.append(_tile[1])
    return covered

row = 2000000

covering_sensors = check_sensors(row)
covered = check_row(row, covering_sensors)
covered = list(dict.fromkeys(covered))
print(len(covered))