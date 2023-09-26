import string

with open('data.txt') as f:
    lines = f.read().splitlines()

conv = dict(zip(string.ascii_letters, range(1,53)))
dups = []

for line in lines:
    length = len(line)
    var1 = line[:int(length/2)]
    var2 = line[int(length/2):]
    
    for letter in var1:
        if letter in var2:
            dups.append(letter)
            break

counter = []
for i in range(len(dups)):
    counter.append(conv[dups[i]])

print(sum(counter))