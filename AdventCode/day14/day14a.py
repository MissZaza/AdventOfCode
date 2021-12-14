def next_step(template: str, rules: dict) -> str:
    new_polymer= template[0]
    for x in range(1,len(template)):
        new_polymer += rules[template[x-1]+template[x]] + template[x]
    return new_polymer

with open("Input2.txt") as f:
    lines = f.read().splitlines()

template = lines[0]

rules = {}
for line in lines[2:]:
    line = (line.split(" -> "))
    rules[line[0]] = line[1]

for step in range(10):
    grown_template = next_step(template,rules)
    template = grown_template
    print(template)

n_element = {}
for element in set(template):
    n_element[element] = len([x for x in template if x == element])

max_occurence = max(y for x,y in n_element.items())
min_occurence = min(y for x,y in n_element.items())

print(max_occurence , min_occurence, max_occurence - min_occurence)