f = open("Input.txt","r")
lines = f.readlines()
f.close()

crats = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
cpt = 0

for line in lines:
    cpt +=1
    if cpt <= 8:
        cpt2 = 0
        for i in range(1, 37, 4):
            if line[i] != ' ':
                if crats[cpt2] == [0]:
                    crats[cpt2] = [line[i]]
                else:
                    crats[cpt2].append(line[i])
            cpt2 += 1
    if cpt ==8 :
        for crat in crats:
            crat.reverse()
        print(crats)
    if cpt >= 11:
        move = []
        instruct = line.split(' ')
        for i in range(int(instruct[1])):
            '''crats[int(instruct[5])-1].append(crats[int(instruct[3])-1].pop(-1))'''
            move.append(crats[int(instruct[3]) - 1].pop(-1))
        for i in range(len(move)):
            crats[int(instruct[5]) - 1].append(move.pop(-1))


# Part 1
answer = ""
for nb in range(9):
   answer += crats[nb][-1]

print(answer)






#Part 2



