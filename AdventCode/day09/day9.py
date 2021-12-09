f = open("Input2.txt","r")
lines = f.readlines()
f.close()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Map:
    def __init__(self, heightlist):
        self.rows = len(heightlist)
        self.columns = len(heightlist[0])
        self.map = {}
        for r in range(self.rows):
            for c in range(self.columns):
                self.map[(c, r)] = int(heightlist[r][c])

    def neighbours(self, point):
        neighbours = []
        if point[0] > 0:
            neighbours.append((point[0] - 1, point[1]))
        if point[0] < self.columns - 1:
            neighbours.append((point[0] + 1, point[1]))
        if point[1] > 0:
            neighbours.append((point[0], point[1] - 1))
        if point[1] < self.rows - 1:
            neighbours.append((point[0], point[1] + 1))

        print(point, neighbours)
        return neighbours

    def islow(self, point):
        result = True
        for neighbour in self.neighbours(point):
            if self.map[neighbour] <= self.map[point]:
                result = False

        return result

clines = []
for line in lines:
    clines.append(line.replace("\n",""))

cave = Map(clines)

riskLevel =0
for point in cave.map.keys():
    if cave.islow(point):
        riskLevel = riskLevel + cave.map[point] + 1

print(riskLevel)