DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

with open("Input2.txt") as f:
    lines = f.read().splitlines()

grid = {}
risk_level_p= {}
for r, line in enumerate(lines):
    for c,risk in enumerate(str(line)):
        grid[c,r] = int(risk)
        risk_level_p[c,r] = 100000

risk_level_p[(0, 0)] = 0

nrows = len(lines)
ncolumns = len(lines[0])


def neighbours(point: tuple) -> list:
    neighbour =[]
    for direction in DIRECTIONS:
        if (0 <= point[0] + direction[0] < ncolumns) and (0 <= point[1] + direction[1] < nrows):
            neighbour.append((point[0] + direction[0], point[1] + direction[1]))
    return neighbour


end = (nrows-1, ncolumns-1)
last_points = [(0, 0)]

while len(last_points) > 0:
    new_path = set()
    for point in last_points:
        for neighbour in neighbours(point):
            if risk_level_p[neighbour] > risk_level_p[point] + grid[neighbour]:
                print(neighbour, risk_level_p[neighbour], risk_level_p[point] + grid[neighbour])
                new_path.add(neighbour)
                risk_level_p[neighbour] = risk_level_p[point] + grid[neighbour]
    last_points = list(new_path)


print(risk_level_p[end])
