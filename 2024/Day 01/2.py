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

def instance_counter(intersection, list2):
    unique, counts = np.unique(list2, return_counts=True)
    counter_dict = dict(zip(unique, counts))
    counter_list = list()
    for i in intersection:
        counter_list.append(counter_dict[i])
    return counter_list

def calculate_answer(intersection, counter):
    iteration_list = zip(intersection, counter)
    answer = 0
    for i, j in iteration_list:
        answer += i*j
    return answer

def solve():
    list1, list2 = data_handler()
    intersection_list = np.intersect1d(list1, list2)
    counter_list2 = instance_counter(intersection_list, list2)
    print(calculate_answer(intersection_list, counter_list2))

solve()