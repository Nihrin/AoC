with open('data.txt') as f:
    lines = f.read().splitlines()

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
words_to_numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

new_lines = list()

for line in lines:
    new_line = line
    for word in words:
        new_line = new_line.replace(word, word + str(words_to_numbers[word]) + word)
    new_lines.append(new_line)


numbers = list()

for line in new_lines:
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