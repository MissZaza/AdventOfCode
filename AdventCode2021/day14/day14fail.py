class Polymerization:
    def __init__(self, rules: dict, elements: dict):
        self.rules = rules
        self.elements = elements

    def grow(self, template: str) -> str:
        return self.rules[template[0] + template[1]]

    def grow_mult(self, template: str, step: int):
        if step == 0:
            self.elements[template[0]] += 1
        else:
            for x in range(1,len(template)):
                insert = self.grow(template[x-1:])
                self.grow_mult(template[x-1]+insert, step - 1)
                self.grow_mult(insert+template[x], step - 1)


with open("Input.txt") as f:
    lines = f.read().splitlines()

template = lines[0]

rules = {}

for line in lines[2:]:
    line = (line.split(" -> "))
    rules[line[0]] = line[1]

n_element = {}
for element in set(rules.values()):
    n_element[element] = 0

polymer = Polymerization(rules, n_element)

polymer.grow_mult(template,25)
polymer.elements[template[-1]] += 1


max_occurence = max(y for x,y in polymer.elements.items())
min_occurence = min(y for x,y in polymer.elements.items())



print(max_occurence , min_occurence, max_occurence - min_occurence)

