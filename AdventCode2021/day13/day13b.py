def fold_paper(paper: set, line: str, position: int) -> set:
    folded_paper = set()

    if line == "x":
        num_line = 0
    else:
        num_line = 1

    for point in paper:
        if point[num_line] < position:
            folded_paper.add(point)
        elif num_line == 0:
            folded_paper.add((2 * position - point[0], point[1]))
        else:
            folded_paper.add((point[0], 2 * position - point[1]))
    return folded_paper

with open("Input2.txt") as f:
    lines = f.read().splitlines()

paper = set()
folds = []
for line in lines:
    if line == "":
        continue
    if line[0].isalpha():
        line = line.replace("fold along ", "").split("=")
        folds.append([line[0], int(line[1])])
    else:
        line = line.split(",")
        paper.add((int(line[0]), int(line[1])))

for fold in folds:
    paper = fold_paper(paper, fold[0], fold[1])

for y in range(max(y for x,y in paper)+1):
    visual= ""
    for x in range(max(x for x,y in paper)+1):
        if (x,y) in paper:
            visual += "#"
        else:
            visual += "."
    print(visual)
