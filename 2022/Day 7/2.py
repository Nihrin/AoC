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
                if current_dir == "/":
                    children[current_dir] += [current_dir +  child]
                else:
                    children[current_dir] += [current_dir + "/" + child]
            else:
                if current_dir == "/":
                    children[current_dir] = [current_dir +  child]
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

total_space = 70000000
used_space = sum_dirs(directories)
free_space = total_space - used_space
to_free = 30000000 - free_space

true_total_size = {}
options = []
for dir in directories:
    kids = all_dirs(dir)
    size = sum_dirs(kids)
    if size >= to_free:
        true_total_size[dir] = size
        options.append(dir)

best = 9999999999
for i in directories:
    if i in true_total_size:
        if true_total_size[i] < best:
            best = true_total_size[i]
print(best)