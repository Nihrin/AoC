import string

with open('data.txt') as f:
    lines = f.read().splitlines()

conv = dict(zip(string.ascii_letters, range(1,53)))
dups = []

for i in range(int(len(lines)/3)):
    j = i * 3
    var1 = lines[j]
    var2 = lines[j+1]
    var3 = lines[j+2]

    for letter in var1:
        if letter in var2 and letter in var3:
            dups.append(letter)
            break

counter = []
for i in range(len(dups)):
    counter.append(conv[dups[i]])
print(len(counter))

print(sum(counter))