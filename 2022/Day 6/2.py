with open('data.txt') as f:
    lines = f.read().splitlines()

data = lines[0]
var = []

for i in range(len(data)):
    var.append(data[i])
    dup = False
    if len(var) > 13:
        for j in range(len(var)):
            if (var[j] in var[j+1:]) or (var[j] in var[:j]):
                dup = True
                break
        if dup == False:
            print(i+1)
            break
        var.pop(0)            
