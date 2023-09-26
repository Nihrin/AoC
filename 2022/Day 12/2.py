import numpy as np
import string

with open('data.txt') as f:
    lines = f.read().splitlines()

for x in range(len(lines)):
    lines[x] = list(lines[x])
value_matrix = np.array(lines)
height = value_matrix.shape[0]
width = value_matrix.shape[1]

path_matrix = np.full((height, width), -1)
letter_dict = dict(zip(string.ascii_lowercase, range(1,27)))
letter_dict['S'] = 1
letter_dict['E'] = 27
value_mat = np.full((height, width), -1)

a_tiles = []
for i in range(height):
    for j in range(width):
        value_mat[i,j] = letter_dict[value_matrix[i,j]]
        if value_mat[i,j] == 1:
            a_tiles.append((i,j))
        if value_mat[i,j] == 27:
            end_r = i
            end_c = j

value_matrix = value_mat.copy()
movement_dict = {"U":(-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}
end_tile = (end_r, end_c)

def check_edges(tile):
    found = []
    looks = ["U", "R", "D", "L"]
    if tile[0] == 0:
        looks.remove("U")
    if tile[1] == width - 1:
        looks.remove("R")
    if tile[0] == height - 1:
        looks.remove("D")
    if tile[1] == 0:
        looks.remove("L")
    for dir in looks:
        found.append((tile[0] + movement_dict[dir][0], tile[1] + movement_dict[dir][1]))
    return found

def look_around(tile):
    found = check_edges(tile)
    found_ = found.copy()
    for t in found:
        if t in checked:
            found_.remove(t)
        elif value_matrix[t] > (value_matrix[tile] + 1):
            found_.remove(t)
    return found_

best = []
path_matrix_ = path_matrix.copy()

while a_tiles:
    path_matrix = path_matrix_.copy()
    steps = 0
    checked = []
    current_tile = a_tiles[0]
    a_tiles.pop(0)
    to_check = [current_tile]

    while to_check:
        too_check = to_check.copy()
        for t in too_check:
            if t in checked:
                to_check.pop(0)
                break
            path_matrix[t] = steps
            to_check += look_around(to_check[0])
            checked.append(to_check[0])
            to_check.pop(0)

        steps += 1

        to_check = list(dict.fromkeys(to_check))
    if path_matrix[end_tile] > -1:
        best.append(path_matrix[end_tile])
        print(path_matrix[end_tile])

print(min(best))