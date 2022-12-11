f = open("Input.txt","r")
lines = f.read().splitlines()
f.close()

nb_ape = int((len(lines)+1) /7)
nb_turn = 10000


class Monkey:
    def __init__(self,items, operation, test, true, false,id):
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.id = id

    def operate(self, item):
        operands = self.operation.split(' ')
        new_item = Item(0,monkeys)
        for i, number in enumerate(item.worry):
            if operands[1] == "+":
                number += int(operands[2])
                new_item.worry[i] = number % item.test[i]
            elif operands[2] == "old":
                number = number * number
                new_item.worry[i] = number % item.test[i]
            else:
                number = number * int(operands[2])
                new_item.worry[i] = number % item.test[i]
        return new_item

    def inspect(self):
        inspected = []
        for item in self.items:
            item = self.operate(item)
            if item.worry[self.id] == 0:
                new_ape = self.true
            else:
                new_ape = self.false
            inspected.append(tuple((item, new_ape)))
        self.items = []
        return inspected

class Item:
    def __init__(self,worry, monkeys):
        self.worry = [worry for m in monkeys]
        self.test = [m.test for m in monkeys]


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
    monkeys.append(Monkey(items, operation, int(test), int(true), int(false),i))

for monkey in monkeys:
    monkey.items = [Item(item,monkeys) for item in monkey.items]

for turn in range(nb_turn):
    for i, monkey in enumerate(monkeys):
        to_throw = monkey.inspect()
        monkeys_act[i] += len(to_throw)
        if len(to_throw) > 0:
            for item,monk in to_throw:
                monkeys[monk].items.append(item)

#Part 2
monkeys_act.sort(reverse=True)
print('Part2',monkeys_act[0]*monkeys_act[1])



