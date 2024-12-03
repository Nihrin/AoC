import numpy as np
import copy

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

def first_check(data):
    invalid_lines = list()
    counter = 0
    for line in data:
        if line_is_valid(line):
            counter += 1
        else:    
            invalid_lines.append(line)
    return counter, invalid_lines

def second_check(data):
    counter = 0
    for line in data:
        for i in range(len(line)):
            new_line = copy.deepcopy(line)
            new_line.pop(i)
            if line_is_valid(new_line):
                counter += 1
                break
    return counter    

def check_rules(data):
    counter, invalid_lines = first_check(data)
    counter += second_check(invalid_lines)
    return counter

def solve():
    data = data_handler()
    answer = check_rules(data)
    print(answer)

solve()