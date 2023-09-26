import math

with open('data.txt') as f:
    lines = f.read().splitlines()

class Monkey():
    def __init__(self, number):
        self.number = number
        start_index = 7 * number
        
        self.items = lines[start_index + 1].split(" ")[4:]
        for i in range(len(self.items)):
            if self.items[i][-1] == ",":
                self.items[i] = int(self.items[i][:-1])
            else:
                self.items[i] = int(self.items[i])
        
        self.operation = lines[start_index + 2].split(" ")[-2:]

        self.test = int(lines[start_index + 3].split(" ")[-1])
        self.true = int(lines[start_index + 4].split(" ")[-1])
        self.false = int(lines[start_index + 5].split(" ")[-1])

        self.inspect = 0

    def get_items(self):
        return self.items

    def get_result(self):
        return self.inspect
    
    def catch_item(self, item):        
        self.items.append(item)

    def inspect_item(self, item):
        self.inspect += 1
        old = item
        try:
            val = int(self.operation[1])
        except:
            val = vars()[self.operation[1]]
        if self.operation[0] == "*":
            new = old * val
        elif self.operation[0] == "+":
            new = old + val
        else:
            print("Inspect item error")
            exit()

        return new
    
    def throw_item(self, monkey, new_item):
        self.items.pop(0)
        monkeys[monkey].catch_item(new_item)

    def go(self):
        items = self.items.copy()
        for item in items:
            worry = self.inspect_item(item)
            worry = math.floor(worry / 3)
            if worry % self.test == 0:
                self.throw_item(self.true, worry)
            else:
                self.throw_item(self.false, worry)
    
   
total_monkeys = int((len(lines) + 1) / 7)

monkeys = []

for number in range(total_monkeys):
    monkey = Monkey(number)
    monkeys.append(monkey)

rounds = 20

for round in range(rounds):
    for m in monkeys:
        m.go()

best = []
for n in monkeys:
    best.append(n.get_result())

print(best)

print(sorted(best)[-1] * sorted(best)[-2])