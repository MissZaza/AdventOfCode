f = open("Input.txt","r")
lines = f.readlines()
f.close()

elves = [0]
cpt = 0
for line in lines:
    if line == '\n':
        elves.append(0)
        cpt += 1
    else:
        elves[cpt] += int(line)

#Part 1
print(max(elves))

#Part 2

elves.sort(reverse=True)
print(elves[0]+elves[1]+elves[2])