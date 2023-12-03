with open('data.txt') as f:
    lines = f.read().splitlines()

numbers = list()

for line in lines:
    number = str()
    for i in line:
        if i.isdigit():
            number += i
            break
    for j in reversed(line):
        if j.isdigit():
            number += j
            break
    number = int(number)
    numbers.append(number)

print(sum(numbers))