with open('data.txt') as f:
    lines = f.read().splitlines()

counter = 0
best = []

for i in lines:
    if i:
        counter += int(i)
    else:
        if len(best) < 3:
            best.append(counter)
        else:
            if counter > min(best):
                best.remove(min(best))
                best.append(counter)
        counter = 0

print(sum(best))