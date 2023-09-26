import numpy as np

with open('data.txt') as f:
    lines = f.read().splitlines()

for i in range(len(lines)):
    lines[i] = lines[i].split(" ")

cycle = 0
pos = [0,1,2]
row = ""

for line in lines:
    if cycle in pos:
        row += "#"
    else:
        row += "."
    cycle += 1
    if line[0] == "noop":
        pass
    else:
        if cycle % 40 == 0:
            print(row)
            row = ""
            cycle = 0
        if cycle in pos:
            row += "#"
        else:
            row += "."
        pos = [i+int(line[1]) for i in pos]
        cycle += 1
    
    if cycle % 40 == 0:
        print(row)
        row = ""
        cycle = 0

print(row)
