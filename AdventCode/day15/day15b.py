DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def neighbours(point: tuple) -> list:
    neighbour =[]
    for direction in DIRECTIONS:
        if (0 <= point[0] + direction[0] < ncolumns * 5) and (0 <= point[1] + direction[1] < nrows * 5):
            neighbour.append((point[0] + direction[0], point[1] + direction[1]))
    return neighbour


def new_risk(duplicate: int, risk: int) -> int:
    if risk + duplicate > 9:
        return (risk + duplicate) % 9
    else:
        return risk + duplicate


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

for r in range(0, nrows * 5):
    for c in range(0, ncolumns * 5):
        if (c,r) in grid.keys():
            continue
        else:
            duplicate = int(c/ncolumns) + int(r/nrows)
            original_point = (c % ncolumns, r % nrows)
            grid[c, r] = new_risk(duplicate, grid[original_point])
            risk_level_p[c, r] = 100000


end = (nrows * 5 - 1, ncolumns * 5 - 1)
last_points = [(0, 0)]

while len(last_points) > 0:
    new_path = set()
    for point in last_points:
        for neighbour in neighbours(point):
            if risk_level_p[neighbour] > risk_level_p[point] + grid[neighbour]:
                new_path.add(neighbour)
                risk_level_p[neighbour] = risk_level_p[point] + grid[neighbour]
    last_points = list(new_path)


print(risk_level_p[end])
