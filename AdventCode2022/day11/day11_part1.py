f = open("Input.txt","r")
lines = f.read().splitlines()
f.close()

nb_ape = int((len(lines)+1) /7)
nb_turn = 20


class Monkey:
    def __init__(self,items, operation, test, true, false):
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false

    def operate(self, number):
        operands = self.operation.split(' ')
        if operands[1] == "+":
            new = number + int(operands[2])
        elif operands[2] == "old":
            new = number * number
        else:
            new = number * int(operands[2])
        return int(new/3)

    def inspect(self):
        inspected = []
        for item in self.items:
            new = self.operate(item)
            if new % self.test == 0:
                new_ape = self.true
            else:
                new_ape = self.false
            inspected.append(tuple((new, new_ape)))
            self.items = []
        return inspected



monkeys = []
monkeys_act = [0 for monkey in range(nb_ape)]
for i in range(nb_ape):
    label, items = lines[i*7 +1].split(':')
    items = items.split(',')
    items = [int(item) for item in items]
    label, operation = lines[i*7 +2].split('= ')
    label, test = lines[i*7 +3].split('by ')
    label, true = lines[i * 7 + 4].split('monkey ')
    label, false = lines[i * 7 + 5].split('monkey')
    monkeys.append(Monkey(items, operation, int(test), int(true), int(false)))

for turn in range(nb_turn):
    for i, monkey in enumerate(monkeys):
        to_throw = monkey.inspect()
        monkeys_act[i] += len(to_throw)
        if len(to_throw) > 0:
            for item,monk in to_throw:
                monkeys[monk].items.append(item)

#Part 1
monkeys_act.sort(reverse=True)
print('Part1',monkeys_act[0]*monkeys_act[1])



