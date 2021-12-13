def fold(paper: set, line: str, position: int) -> set:
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
        print(line)
        folds.append([line[0], int(line[1])])
    else:
        line = line.split(",")
        paper.add((int(line[0]), int(line[1])))

folded_paper = fold(paper, folds[0][0], folds[0][1])
print(len(folded_paper))