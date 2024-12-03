import numpy as np

with open('data.txt') as f:
    lines = f.read().splitlines()

def data_handler():
    total_list = list()
    for line in lines:
        string_line = line.split()
        int_line = [int(num) for num in string_line]
        total_list.append(int_line)
    return total_list

def is_descending(line):
    for i in range(len(line)-1):
        if (line[i] <= line[i+1]):
            return False
    return True

def is_ascending(line):
    for i in range(len(line)-1):
        if (line[i] >= line[i+1]):
            return False
    return True

def descending_or_ascending(line):
    if not (is_descending(line) or is_ascending(line)):
        return False
    return True

def second_rule(line):
    for i in range(len(line)-1):
        difference = abs(line[i] - line[i+1])
        if (difference > 3):
            return False
    return True            

def line_is_valid(line):
    if not (second_rule(line) and descending_or_ascending(line)):
        return False
    return True

def check_rules(data):
    counter = 0
    for line in data:
        if line_is_valid(line):
            counter += 1
    return counter

def solve():
    data = data_handler()
    answer = check_rules(data)
    print(answer)

solve()