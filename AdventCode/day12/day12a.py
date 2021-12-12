class Path:
    def __init__(self, caves: list):
        self.caves = caves

    @property
    def last_position(self)-> str:
        return self.caves[-1]

    def can_be_visited(self,cave):
        if cave.isupper() or cave not in self.caves:
            return True
        else:
            return False

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
        test = path.next_positions(links)
        for cave in path.next_positions(links):
            if cave == "end":
                ended_paths.append(Path(path.caves+[cave]))
            else:
                paths.append(Path(path.caves+[cave]))
    init = paths.copy()
    paths = []

print(len(ended_paths))


