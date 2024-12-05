def data_handler(input):
    data = list()
    for line in input:
        data += [list(line)]
    return data

def puzzle_data_handler():
    with open('puzzle_data.txt') as f:
        lines = f.read().splitlines()
    return data_handler(lines)

def test_data_handler():
    with open('test_data.txt') as f:
        lines = f.read().splitlines()
    return data_handler(lines)