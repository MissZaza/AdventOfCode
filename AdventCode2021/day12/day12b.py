class Path:
    def __init__(self, caves: list):
        self.caves = caves

    @property
    def last_position(self)-> str:
        return self.caves[-1]

    def can_be_visited(self,cave):
        if cave.isupper() or cave not in self.caves:
            return True
        elif cave == "start":
            return False
        else:
            small_caves = [cave for cave in self.caves if not cave.isupper()]
            if max( len([cave for cave in small_caves if cave ==x]) for x in set(small_caves)) > 1:
                return False
            else:
                return True

    def next_positions(self,links: list) -> list:
        next_positions = []
        for link in links:
            if self.last_position in link:
                candidate = (link - {self.last_position}).pop()
                if self.can_be_visited(candidate):
                    next_positions.append(candidate)
        return next_positions


with open("Input2.txt") as f:
    lines = f.read().splitlines()

links = []
for line in lines:
    links.append(set(line.split("-")))

init = [Path(["start"])]
paths = []
ended_paths = []

while len(init) > 0:
    for path in init:
        for cave in path.next_positions(links):
            if cave == "end":
                ended_paths.append(Path(path.caves+[cave]))
            else:
                paths.append(Path(path.caves+[cave]))
    init = paths.copy()
    paths = []

print(len(ended_paths))


