
with open("Input2.txt") as f:
    lines = f.readlines()


class Bassin:
    def __init__(self):
        self.points = []

    @property
    def lengh(self):
        return len(self.points)

    def define(self,initialPoint,map):
        self.points.append(initialPoint)
        for point in map.neighbours(initialPoint):
            if point not in self.points and map.map[point] != 9:
                self.define(point,map)


class Map:
    def __init__(self, map: dict, rows: int, columns: int):
        self.map = map
        self.rows = rows
        self.columns = columns

    def neighbours(self, point: tuple):
        neighbours = []
        if point[0] > 0:
            neighbours.append((point[0] - 1, point[1]))
        if point[0] < self.columns - 1:
            neighbours.append((point[0] + 1, point[1]))
        if point[1] > 0:
            neighbours.append((point[0], point[1] - 1))
        if point[1] < self.rows - 1:
            neighbours.append((point[0], point[1] + 1))
        return neighbours

    def islow(self, point: tuple):
        for neighbour in self.neighbours(point):
            if self.map[neighbour] <= self.map[point]:
                return False
        return True

heightlist = []
for line in lines:
    heightlist.append(line.replace("\n",""))

map = {}
rows = len(heightlist)
columns = len(heightlist[0])
for r in range(rows):
    for c in range(columns):
        map[(c, r)] = int(heightlist[r][c])

cave = Map(map, rows, columns)

""" 
Code to solve part 1
riskLevel =0

for point in cave.map.keys():
    if cave.islow(point):
        riskLevel = riskLevel + cave.map[point] + 1
"""
# Code to solve part 2
lowPoints = []
for point in cave.map.keys():
    if cave.islow(point):
        lowPoints.append(point)

bassins = []
for point in lowPoints:
    bassin = Bassin()
    bassin.define(point,cave)
    bassins.append(bassin)

bassins = sorted(bassins, key=lambda x: x.lengh, reverse=True)
print(bassins[0].lengh, bassins[1].lengh, bassins[2].lengh, bassins[0].lengh * bassins[1].lengh * bassins[2].lengh)
