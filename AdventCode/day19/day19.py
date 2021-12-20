class Point:
    def __init__(self, x, y , z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point(x, y, z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash(self.x) + hash(self.y) + hash(self.z)

    def __gt__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return self.z > other.z
            else:
                return self.y > other.y
        else:
            return self.x > other.x

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

    def dist(self, other)-> int:
        return pow(self.x - other.x,2) + pow(self.y - other.y,2) + pow(self.z - other.z,2)

    def man_dist(self, other)-> int:
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def round(self):
        self.x = round(self.x)
        self.y = round(self.y)
        self.z = round(self.z)
        return self


class Scanner:
    def __init__(self):
        self.scanners = [Point(0, 0, 0)]
        self.beacons = []

    def add_beacon(self, beacon: Point) -> None:
        self.beacons.append(beacon)

    def distances(self) -> dict:
        distances = {}
        for x,  b1 in enumerate(self.beacons):
            distances[b1] = []
            for b2 in self.beacons:
                distances[b1].append(b1.dist(b2))
        return distances

    def overlap(self, other) -> tuple:
        other_dist = other.distances()
        self_dist = self.distances()
        overlap1 = []
        overlap2 = []
        for self_p in self.beacons:
            for other_p in other.beacons:
                if len([distance for distance in self_dist[self_p] if distance in other_dist[other_p]]) >= 12:
                    overlap1.append(self_p)
                    overlap2.append(other_p)
        return overlap1, overlap2

    def rebase_and_add(self, other) -> bool:
        overlap1, overlap2 = self.overlap(other)
        if len(overlap1) >= 12:
            center1 = barycentre(overlap1)
            center2 = barycentre(overlap2)
            rebase_o1 = [(point - center1).round() for point in overlap1]
            rebase_o2 = [(point - center2).round() for point in overlap2]
            rotation = {}
            if set([int(p.x) for p in rebase_o1]) == set([int(p.x) for p in rebase_o2]):
                rotation["x"] = "0"
            elif set([int(p.x) for p in rebase_o1]) == set([int(-p.x) for p in rebase_o2]):
                rotation["x"] = "-0"
            elif set([int(p.x) for p in rebase_o1]) == set([int(p.y) for p in rebase_o2]):
                rotation["y"] = "0"
            elif set([int(p.x) for p in rebase_o1]) == set([int(-p.y) for p in rebase_o2]):
                rotation["y"] = "-0"
            elif set([int(p.x) for p in rebase_o1]) == set([int(p.z) for p in rebase_o2]):
                rotation["z"] = "0"
            elif set([int(p.x) for p in rebase_o1]) == set([int(-p.z) for p in rebase_o2]):
                rotation["z"] = "-0"
            if set([int(p.y) for p in rebase_o1]) == set([int(p.x) for p in rebase_o2]):
                rotation["x"] = "1"
            elif set([int(p.y) for p in rebase_o1]) == set([int(-p.x) for p in rebase_o2]):
                rotation["x"] = "-1"
            elif set([int(p.y) for p in rebase_o1]) == set([int(p.y) for p in rebase_o2]):
                rotation["y"] = "1"
            elif set([int(p.y) for p in rebase_o1]) == set([int(-p.y) for p in rebase_o2]):
                rotation["y"] = "-1"
            elif set([int(p.y) for p in rebase_o1]) == set([int(p.z) for p in rebase_o2]):
                rotation["z"] = "1"
            elif set([int(p.y) for p in rebase_o1]) == set([int(-p.z) for p in rebase_o2]):
                rotation["z"] = "-1"
            if set([int(p.z) for p in rebase_o1]) == set([int(p.x) for p in rebase_o2]):
                rotation["x"] = "2"
            elif set([int(p.z) for p in rebase_o1]) == set([int(-p.x) for p in rebase_o2]):
                rotation["x"] = "-2"
            elif set([int(p.z) for p in rebase_o1]) == set([int(p.y) for p in rebase_o2]):
                rotation["y"] = "2"
            elif set([int(p.z) for p in rebase_o1]) == set([int(-p.y) for p in rebase_o2]):
                rotation["y"] = "-2"
            elif set([int(p.z) for p in rebase_o1]) == set([int(p.z) for p in rebase_o2]):
                rotation["z"] = "2"
            elif set([int(p.z) for p in rebase_o1]) == set([int(-p.z) for p in rebase_o2]):
                rotation["z"] = "-2"
            center1 = rotate(center1, rotation)
            self.rotate(rotation)
            self.move(center2 - center1)
            self.scanners.append(Point(0, 0, 0))
            new_beacons = set(self.beacons + other.beacons)
            self.beacons = sorted(list(new_beacons))
            return True
        else:
            return False

    def rotate(self, rotation: dict):
        for p in self.beacons:
            rotate(p, rotation)
        for p in self.scanners:
            rotate(p, rotation)

    def move(self, direction: Point):
        for p in self.beacons:
            p.x = round(p.x + direction.x)
            p.y = round(p.y + direction.y)
            p.z = round(p.z + direction.z)
        for p in self.scanners:
            p.x = round(p.x + direction.x)
            p.y = round(p.y + direction.y)
            p.z = round(p.z + direction.z)
        return self


def rotate(p: Point, rotation: dict):
    temp = [p.x, p.y, p.z]
    p.x = temp[int(rotation["x"][-1])]
    if rotation["x"][0] == "-":
        p.x = - p.x
    p.y = temp[int(rotation["y"][-1])]
    if rotation["y"][0] == "-":
        p.y = - p.y
    p.z = temp[int(rotation["z"][-1])]
    if rotation["z"][0] == "-":
        p.z = - p.z
    return p


def barycentre(points: set) -> Point:
    return Point(sum(point.x for point in points)/len(points), sum(point.y for point in points)/len(points), sum(point.z for point in points)/len(points))


with open("input2.txt") as f:
    lines = f.read().splitlines()

scanners = []
nb_scanner = 0
for line in lines:
    if len(line) != 0:
        if line[0:3] == '---':
            scanner = Scanner()
            scanners.append(scanner)
            nb_scanner += 1
        else:
            point = line.split(",")
            beacon = Point(int(point[0]), int(point[1]), int(point[2]))
            scanners[nb_scanner - 1].add_beacon(beacon)

to_rebase = scanners
nb_beacons = 0
index_scan = 0
while len(to_rebase) > 1:
    not_rebased = [to_rebase[0]]
    for scanner in to_rebase[1:]:
        if not to_rebase[0].rebase_and_add(scanner):
            not_rebased.append(scanner)
        else:
            #print(scanners[0].scanners)
            continue
    if to_rebase == not_rebased:
        nb_beacons += len(to_rebase[0].beacons)
        to_rebase = to_rebase[1:]
    else:
        to_rebase = not_rebased.copy()
nb_beacons += len(to_rebase[0].beacons)
#print(nb_beacons)

manhattan_dist = []
for x, p1 in enumerate(scanners[0].scanners[:-1]):
    for p2 in scanners[0].scanners[x:]:
        manhattan_dist.append(p1.man_dist(p2))
print(max(manhattan_dist))



