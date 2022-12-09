f = open("Input.txt","r")
lines = f.read().splitlines()
f.close()

DIRECTIONS = {'D': [-1,0], 'U': [1,0], 'L': [0,-1], 'R': [0,1]}
visited_spot1 = set()
visited_spot9 = set()
currentH_spot = [0, 0]
currentT_spot = [[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0]]
visited_spot1.add((0,0))
visited_spot9.add((0,0))

def follow(currentH_spot: list, currentT_spot: list):
    if abs(currentH_spot[0] - currentT_spot[0]) > 1 and abs(currentH_spot[1] - currentT_spot[1]) > 1:
        difLR = currentH_spot[1] - currentT_spot[1]
        currentT_spot[1] += int(difLR / abs(difLR))
        difUD = currentH_spot[0] - currentT_spot[0]
        currentT_spot[0] += int(difUD / abs(difUD))
    if abs(currentH_spot[0] - currentT_spot[0]) > 1:
        currentT_spot[1] = currentH_spot[1]
        dif = currentH_spot[0] - currentT_spot[0]
        currentT_spot[0] += int(dif / abs(dif))
    elif abs(currentH_spot[1] - currentT_spot[1]) > 1:
        currentT_spot[0] = currentH_spot[0]
        dif = currentH_spot[1] - currentT_spot[1]
        currentT_spot[1] += int(dif / abs(dif))
    return currentT_spot


for line in lines:
    dir, move = line.split()
    for i in range(int(move)):
        currentH_spot[0] += DIRECTIONS[dir][0]
        currentH_spot[1] += DIRECTIONS[dir][1]
        currentT_spot[0] = follow(currentH_spot,currentT_spot[0])
        for i in range(1,9):
            currentT_spot[i] = follow(currentT_spot[i-1],currentT_spot[i])
        visited_spot1.add((currentT_spot[0][0], currentT_spot[0][1]))
        visited_spot9.add((currentT_spot[8][0], currentT_spot[8][1]))

#Part 1
print('Part1', len(visited_spot1))

#Part 2
print('Part2', len(visited_spot9))



