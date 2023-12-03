import string

with open('data.txt') as f:
    lines = f.read().splitlines()

data = []
for i in range(len(lines)):
    x = lines[i].split(",")
    a = x[0].split("-")
    b = x[1].split("-")
    data.append([a, b])

counter = 0

for i in range(len(data)):
    if (int(data[i][0][0]) >= int(data[i][1][0]) and int(data[i][0][1]) <= int(data[i][1][1])) or (int(data[i][0][0]) <= int(data[i][1][0]) and int(data[i][0][1]) >= int(data[i][1][1])):
        counter += 1
    elif (int(data[i][0][0]) <= int(data[i][1][1]) and int(data[i][0][1]) >= int(data[i][1][1])) or (int(data[i][0][0]) >= int(data[i][1][1]) and int(data[i][0][1]) <= int(data[i][1][1])):
        counter += 1
    elif (int(data[i][0][0]) <= int(data[i][1][0]) and int(data[i][0][1]) >= int(data[i][1][0])) or (int(data[i][0][0]) >= int(data[i][1][0]) and int(data[i][0][1]) <= int(data[i][1][0])):
        counter += 1
print(counter)