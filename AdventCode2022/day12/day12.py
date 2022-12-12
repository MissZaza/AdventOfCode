f = open("Input.txt","r")
lines = f.read().splitlines()
f.close()

rows = len(lines)
cols = len(lines[0])
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Path:
    def __init__(self,coord):
        self.row = coord[0]
        self.col = coord[1]

    @property
    def height(self):
        hgt = lines[self.row][self.col]
        if hgt == 'E':
            return ord('z')
        elif hgt == 'S':
            return ord('a')
        else:
            return ord(hgt)

    @property
    def finished(self):
        return lines[self.row][self.col] == 'E'

    def next_step(self,dir: tuple):
        new_end = [self.row + dir[0], self.col +dir[1]]
        if 0 <= new_end[0] < rows and 0 <= new_end[1] < cols:
            new_p = Path(new_end)
            if self.height - new_p.height >= -1:
                return new_p
        return self


def shortest(start):
    paths = [Path(start)]
    visited_spot = set(start)
    ans=[]
    cpt = 0

    while len(ans) == 0:
        cpt +=1
        new_paths = []
        for path in paths:
            for dir in DIRECTIONS:
                new_path = path.next_step(dir)
                if (new_path.row, new_path.col) not in visited_spot:
                    new_paths.append(new_path)
                    visited_spot.add((new_path.row, new_path.col))
        paths = new_paths
        ans = [path for path in paths if path.finished]
    return cpt


def near_b(r,c):
    for dir in DIRECTIONS:
        neigh = [r + dir[0], c + dir[1]]
        if 0 <= neigh[0] < rows and 0 <= neigh[1] < cols:
            if lines[neigh[0]][neigh[1]] == 'b':
                return True
    return False


#Part 1
start = []
for r, line in enumerate(lines):
    for c, spot in enumerate(line):
        if spot == "S" :
            start = (r,c)
            break
    if len(start)>0:
        break

print('Part1', shortest(start))

#Part 2

shorter = 449

for r, line in enumerate(lines):
    for c, spot in enumerate(line):
        if spot == "a" and near_b(r,c):
            start = (r,c)
            shorter = min(shortest(start), shorter)

print('Part2', shorter)


