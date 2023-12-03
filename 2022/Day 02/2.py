with open('data.txt') as f:
    lines = f.read().splitlines()

input = []
for i in lines:
    input.append((i[0], i[2]))

points = 0

for game in input:
    if game[0] == "A":
        if game[1] == "X":
            points += 3
        if game[1] == "Y":
            points += 4
        if game[1] == "Z":
            points += 8

    if game[0] == "B":
        if game[1] == "X":
            points += 1
        if game[1] == "Y":
            points += 5
        if game[1] == "Z":
            points += 9
    
    if game[0] == "C":
        if game[1] == "X":
            points += 2
        if game[1] == "Y":
            points += 6
        if game[1] == "Z":
            points += 7

print(points)        