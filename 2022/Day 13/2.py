import ast

with open('data.txt') as f:
    lines = f.read().splitlines()


class Pair():
    def __init__(self, list1, list2):
        self.list1 = ast.literal_eval(list1)
        self.list2 = ast.literal_eval(list2)
    
    def get_lists(self):
        return self.list1, self.list2
    
    def evaluation(self):
        left = self.list1
        right = self.list2
        return self.compare(left, right)

    def compare(self, l, r):
        check, empty = self.check_empty(l, r)
        if check:
            return empty
        for i in range(len(l) + 1):
            if i == len(r) and i == len(l):
                return
            if i == len(r):
                return False
            if i == len(l):
                return True
            varl = l[i]
            varr = r[i]
            if type(varl) != type(varr) and type(varl) == int:
                varl = [varl]
            elif type(varl) != type(varr) and type(varr) == int:
                varr = [varr]
            
            if type(varl) == type(varr) == int:
                if varl < varr:
                    return True
                elif varl > varr:
                    return False
            elif type(varl) == type(varr) == list:
                x = self.compare(varl, varr)
                if x == True:
                    return True
                elif x == False:
                    return False
    
    def check_empty(self, l ,r):
        if l and not r:
            return True, False
        if r and not l:
            return True, True
        return False, ""


lines = list(filter(None, lines))
lines += ['[[2]]', '[[6]]']
scores = dict(zip(range(1, len(lines)+1), [0]*(len(lines))))
for i in range(len(lines) - 1):
    for j in range(i+1, len(lines)):
        pair = Pair(lines[i], lines[j])
        if pair.evaluation():
            scores[j+1] += 1
        else:
            scores[i+1] += 1

print((scores[len(lines)-1] + 1) * (scores[len(lines)] + 1))