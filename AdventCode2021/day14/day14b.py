class Polymerization:
    def __init__(self, rules: dict, init: str):
        self.rules = rules
        self.init = init

    @property
    def elements(self) -> set:
        return set(self.rules.values())

    @property
    def init_pairs(self) -> str:
        pairs = {}
        for x in range(1, len(self.init)):
            if self.init[x-1] + self.init[x] in pairs:
                pairs[self.init[x-1] + self.init[x]] += 1
            else:
                pairs[self.init[x - 1] + self.init[x]] = 1
        return pairs

    def grow(self, pairs: dict)-> dict:
        grown_pairs = {}
        for pair, nb in pairs.items():
            if pair[0] + self.rules[pair] in grown_pairs:
                grown_pairs[pair[0] + self.rules[pair]] += nb
            else:
                grown_pairs[pair[0] + self.rules[pair]] = nb
            if self.rules[pair] + pair[1] in grown_pairs:
                grown_pairs[self.rules[pair] + pair[1]] += nb
            else:
                grown_pairs[self.rules[pair] + pair[1]] = nb
        return grown_pairs

    def grow_til(self,nb_step):
        grown_pairs = self.init_pairs
        for x in range(nb_step):
            grown_pairs = self.grow(grown_pairs)
        return grown_pairs

    def pair_to_element(self,nb_pairs):
        nb = {}
        for element in self.elements:
            nb[element] = 0
        for pair, nb_p in nb_pairs.items():
            nb[pair[0]] += nb_p/2
            nb[pair[1]] += nb_p/2
        nb[self.init[0]] += 0.5
        nb[self.init[-1]] += 0.5
        return nb


with open("Input2.txt") as f:
    lines = f.read().splitlines()

template = lines[0]

rules = {}

for line in lines[2:]:
    line = (line.split(" -> "))
    rules[line[0]] = line[1]

polymer = Polymerization(rules, template)

nb_pairs = polymer.grow_til(40)
nb_elements = polymer.pair_to_element(nb_pairs)


max_occurence = max(y for x,y in nb_elements.items())
min_occurence = min(y for x,y in nb_elements.items())


print(nb_elements)
print(max_occurence , min_occurence, max_occurence - min_occurence)

