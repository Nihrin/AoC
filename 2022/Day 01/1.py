with open('data.txt') as f:
    lines = f.read().splitlines()

counter = 0
best = 0

for i in lines:
    if i:
        counter += int(i)
        if counter > best:
            best = counter
    else:
        counter = 0

print(best)