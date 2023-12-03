with open('data.txt') as f:
    lines = f.read().splitlines()

input = []
for i in lines:
    input.append((i[0], i[2]))

points = 0

for game in input:
    if game[1] == "X":
        points += 1
        if game[0] == "A":
            points += 3
        if game[0] == "C":
            points += 6
    
    if game[1] == "Y":
        points += 2
        if game[0] == "A":
            points += 6
        if game[0] == "B":
            points += 3
    
    if game[1] == "Z":
        points += 3
        if game[0] == "B":
            points += 6
        if game[0] == "C":
            points += 3

print(points)

        