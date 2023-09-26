with open('data.txt') as f:
    lines = f.read().splitlines()

children = {}
parents = {}
files = {}
directories = []
current_dir = None

for line in lines:
    if line[0] == "$":
        if line[2:4] == "cd":
            if line[5:len(line)] == "..":
                last = len(current_dir.split("/")[-1]) + 1              
                current_dir = current_dir[:-last]
            else:
                if current_dir is None:
                    current_dir = "/"
                elif current_dir == "/":
                    current_dir += line[5:len(line)]
                else:
                    current_dir += "/" + line[5:len(line)]
                directories.append(current_dir)

    else:
        if line[0:3] == "dir":
            child = line.split(" ")[1]
            if current_dir in children:
                children[current_dir] += [current_dir + "/" + child]
            else:
                children[current_dir] = [current_dir + "/" + child]
            parents[child] = current_dir
        else:
            if current_dir in files:
                files[current_dir] += [line.split(" ")]
            else:
                files[current_dir] = [line.split(" ")]

total_size = {}
for dir in directories:
    size = 0
    if dir in files:
        for file in files[dir]:
            size += int(file[0])
    total_size[dir] = size

possible = []
for dir in directories:
    if dir in total_size:
        if total_size[dir] < 100001:
            possible.append(dir)

true = []
maybe_true = []
for i in possible:
    if i not in children:
        true.append(i)
    else:
        maybe_true.append(i)

true_total_size = {}

def sum_dirs(dirs):
    sum = 0
    for dir in dirs:
        if dir in total_size:
            sum += total_size[dir]
    return sum

def all_dirs(dir):
    dirs = [dir]
    to_check = [dir]
    checking = dir
    while True:
        if checking in children:
            to_add = children[checking]
            dirs += to_add
            to_check += to_add
        to_check.pop(0)
        if to_check:
            checking = to_check[0]
        else:
            break
    return dirs 

to_sum = []
for i in maybe_true:
    dirs = all_dirs(i)
    sum = sum_dirs(dirs)
    if sum > 100000:
        pass
    else:
        to_sum.append(sum)

for i in true:
    to_sum.append(total_size[i])

final = 0
for i in to_sum:
    final += i

print(final)