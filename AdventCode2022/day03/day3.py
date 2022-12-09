f = open("Input.txt","r")
lines = f.readlines()
f.close()

prio = {'a' : '1',
        'b' : '2',
        'c' : '3',
        'd' : '4',
        'e' : '5',
        'f' : '6',
        'g' : '7',
        'h' : '8',
        'i' : '9',
        'j' : '10',
        'k' : '11',
        'l' : '12',
        'm' : '13',
        'n' : '14',
        'o' : '15',
        'p' : '16',
        'q' : '17',
        'r' : '18',
        's' : '19',
        't' : '20',
        'u' : '21',
        'v' : '22',
        'w' : '23',
        'x' : '24',
        'y' : '25',
        'z' : '26',
        'A' : '27',
        'B' : '28',
        'C' : '29',
        'D' : '30',
        'E' : '31',
        'F' : '32',
        'G' : '33',
        'H' : '34',
        'I' : '35',
        'J' : '36',
        'K' : '37',
        'L' : '38',
        'M' : '39',
        'N' : '40',
        'O' : '41',
        'P' : '42',
        'Q' : '43',
        'R' : '44',
        'S' : '45',
        'T' : '46',
        'U' : '47',
        'V' : '48',
        'W' : '49',
        'X' : '50',
        'Y' : '51',
        'Z' : '52',}


#Part 1
priorities1 = 0
for line in lines:
    rucksack1 = line[0: int(len(line)/2)]
    rucksack2 = line[int(len(line) / 2): len(line)]
    for letter in rucksack1:
        if letter in rucksack2:
            priorities1 += int(prio[letter])
            break
print(priorities1)

#Part 2
priorities2 = 0
cpt = 0
groups = []
for line in lines:
    if cpt % 3 == 0:
        groups.append([line[0:len(line)-1]])
    else:
        groups[-1].append(line[0:len(line)-1])
    cpt += 1

for group in groups:
    identity = set()
    for letter in group[0]:
        if letter in group[1]:
            identity.add(letter)
    for letter in identity:
        if letter in group[2]:
            priorities2 += int(prio[letter])
            break
print(priorities2)

print()