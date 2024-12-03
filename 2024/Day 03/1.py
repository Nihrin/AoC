from Helpers import data_handler

def are_integers(input_list):
    if input_list[0].isdigit() and input_list[1].isdigit():
        return True
    return False

def splittable(input):
    if ')' in input:
        input_list = input.split(')')
        if ',' in input_list[0]:
            return True
    return False

def get_multiple(input):
    if splittable(input):
        clean_input = input.split(')')[0].split(',')
        if are_integers(clean_input):
            return int(clean_input[0]) * int(clean_input[1])
    return 0

def get_list_of_multiplications(data):
    multiples = list()
    for var in data:
        multiples.append(get_multiple(var))
    return multiples

def add_all_muls(data):
    multiples = get_list_of_multiplications(data)
    total = 0
    for m in multiples:
        total += m
    return total

def solve():
    data = data_handler()
    answer = add_all_muls(data)
    print(answer)

solve()