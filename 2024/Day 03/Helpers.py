with open('data.txt') as f:
    lines = f.read().splitlines()

def data_handler():
    data = list()
    for line in lines:
        data += line.split("mul(")
    return data