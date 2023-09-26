import numpy as np

with open('data.txt') as f:
    lines = f.read().splitlines()

for i in range(len(lines)):
    lines[i] = lines[i].split(" ")

cycle = 1
val = 1
total = []

for line in lines:
    if line[0] == "noop":
        cycle += 1
    else:
        cycle += 1
        if cycle % 40 == 20:
            total.append(cycle * val)
        cycle += 1
        val += int(line[1])
    
    if cycle % 40 == 20:
        total.append(cycle * val)

print(sum(total))
