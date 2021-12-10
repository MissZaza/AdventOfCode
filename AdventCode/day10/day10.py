import statistics

VALIDCHUNCK = {'<': '>', '{': '}', '(': ')', '[': ']'}
SCORE = {')': 3, ']': 57, '}': 1197, '>': 25137}
SCORE2 = {')': 1, ']': 2, '}': 3, '>': 4}

class Pile:
    def __init__(self):
        self.pile = []

    @property
    def lengh(self) -> int:
        return len(self.pile)

    @property
    def sommet(self) -> str:
        return self.pile[self.lengh - 1]

    @property
    def vide(self):
        return self.lengh == 0

    def empiler(self, c: str) -> None:
        self.pile.append(c)

    def depiler(self) -> None:
        del self.pile[self.lengh - 1]


with open("Input2.txt") as f:
    lines = f.read().splitlines()

score = 0
"""  Part 1 solution
for line in lines:
    pile = Pile()
    for c in line:
        if c in VALIDCHUNCK.keys():
            pile.empiler(VALIDCHUNCK[c])
        elif c == pile.sommet:
            pile.depiler()
        elif pile.vide:
            pass
        else:
            print(c, SCORE[c], line)
            score = score + SCORE[c]
            break
"""
# Part 2 solution
scores = []
for line in lines:
    pile = Pile()
    score = 0
    for c in line:
        if c in VALIDCHUNCK.keys():
            pile.empiler(VALIDCHUNCK[c])
        elif c == pile.sommet:
            pile.depiler()
        elif pile.vide:
            pass
        else:
            score = SCORE[c]
            break
    if score != 0:
        pass
    else:
        score = 0
        for i in range(pile.lengh):
            score = score * 5 + SCORE2[pile.sommet]
            print(score, pile.pile)
            pile.depiler()
        if score != 0:
            scores.append(score)
print(statistics.median(scores))
