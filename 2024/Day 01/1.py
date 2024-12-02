import numpy as np

with open('data.txt') as f:
    lines = f.read().splitlines()

def data_handler():
    list1 = list()
    list2 = list()
    for line in lines:
        a = line.split()
        list1.append(int(a[0]))
        list2.append(int(a[1]))
    return np.array(list1), np.array(list2)

def solve():
    list1, list2 = data_handler()
    sorted_list1 = np.sort(list1)
    sorted_list2 = np.sort(list2)
    distance_list = np.subtract(sorted_list1, sorted_list2)
    absolute_distance_list = np.absolute(distance_list)
    answer = np.sum(absolute_distance_list)
    print(answer)

solve()