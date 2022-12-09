f = open("Input.txt","r")
lines = f.read().splitlines()
f.close()
L = len(lines[0])
H = len(lines)


def visible(height, lines : list, posL, posH):
    if height > max(lines[posH][0:posL]) :
        return True
    elif height > max(lines[posH][posL+1:L+1]):
        return True
    elif height > max([line[posL] for line in lines[0:posH]]):
        return True
    elif height > max([line[posL] for line in lines[posH+1:L+1]]):
        return True
    else:
        return False

def scenic_score(height, lines, posL, posH):
    S, E, O, N = 0,0,0,0
    if posL ==0 or posL == L-1 or posH == 0 or posH == H-1:
        return 0
    trees_S = []
    trees_N = []
    trees_O = []
    trees_E = []
    for i in range(L):
        if i < posL:
            trees_E.append(lines[posH][i])
        if i > posL:
            trees_O.append(lines[posH][i])
    for i in range(H):
        if i < posH:
            trees_N.append(lines[i][posL])
        if i > posH:
            trees_S.append(lines[i][posL])
    trees_E.reverse()
    trees_N.reverse()
    for tree in trees_E:
        if tree < height:
            E += 1
        else:
            E += 1
            break
    for tree in trees_O:
        if tree < height:
            O += 1
        else:
            O += 1
            break
    for tree in trees_N:
        if tree < height:
            N += 1
        else:
            N += 1
            break
    for tree in trees_S:
        if tree < height:
            S += 1
        else:
            S += 1
            break
    return E*O*S*N

nbT = L*2 + (H-2)*2
posL = 1
posH = 1
scores =[]
for line in lines[1:H-1]:
    for tree in line[1:L-1]:
        scores.append(scenic_score(tree,lines,posL,posH))
        if visible(tree,lines,posL,posH):
            nbT += 1
        posL += 1
    posL = 1
    posH += 1

#Part 1


print('Part1', nbT)

#Part 2


print('Part2', max(scores))



