class SNumber:
    def __init__(self, snum: str,level):
        self.brut = snum
        self.level = level
        self.left = str()
        self.right = str()

    @property
    def is_regular(self):
        return type(self.left) == int and type(self.right) == int

    def parse(self):
        sub_pair = 0
        for i, x in enumerate(self.brut[1:-1]):
            if x == "[":
                sub_pair += 1
            elif x == "]":
                sub_pair -= 1
            elif x == "," and sub_pair == 0:
                if self.brut[1:i+1].isnumeric():
                    self.left = int(self.brut[1:i + 1])
                else:
                    self.left = SNumber(self.brut[1:i+1], self.level+1)
                    self.left.parse()
                if self.brut[i + 2 : -1].isnumeric():
                    self.right = int(self.brut[i + 2: -1])
                else:
                    self.right = SNumber(self.brut[i + 2: -1], self.level+1)
                    self.right.parse()

    def magnitude(self):
        if type(self.left) == int:
            mag = 3 * self.left
        else:
            mag = 3 * self.left.magnitude()
        if type(self.right) == int:
            mag += 2 * self.right
        else:
            mag += 2 * self.right.magnitude()
        return mag

    def __add__(self, other):
        result = SNumber("[" + self.print() + "," + other.print() + "]", self.level)
        result.parse()
        return result

    def can_explode(self) -> bool:
        if type(self.left) == int  and self.level >= 4: #and type(self.right) == int
            return True
        else:
            if type(self.left) != int:
                if self.left.can_explode():
                    return True
            if type(self.right) != int:
                if self.right.can_explode():
                    return True
            else:
                return False

    def explode(self):
        explode_chain = []
        n_chain =[self]
        while not n_chain[-1].is_regular:
            if type(n_chain[-1].left) != int and n_chain[-1].left.can_explode():
                explode_chain.append("left")
                n_chain.append(n_chain[-1].left)
            elif type(n_chain[-1].right) != int and n_chain[-1].right.can_explode():
                explode_chain.append("right")
                n_chain.append(n_chain[-1].right)
        #print(n_chain[-1].print(), explode_chain, n_chain[-2].print())

        add = [n_chain[-1].left, n_chain[-1].right]
        #print("je dois split", add, "dans", explode_chain[-1], n_chain[-2].print())
        if explode_chain[-1] == "left":
            n_chain[-2].left = 0
            if type(n_chain[-2].right) == int:
                n_chain[-2].right += add[1]
                #print("simple left")
            else:
                #print("hard left", n_chain[-2].right.print(), "pour placer", add[1])
                to_change = n_chain[-2].right
                while type(to_change.left) != int:
                    to_change = to_change.left
                to_change.left += add[1]
        else:
            n_chain[-2].right = 0
            if type(n_chain[-2].left) == int:
                n_chain[-2].left += add[0]
                #print("simple right")
            else:
                #print("hard right", n_chain[-2].left, "pour placer", add[0])
                to_change = n_chain[-2].left
                while type(to_change.right) != int:
                    to_change = to_change.right
                to_change.right += add[0]

        for x in range(1,len(explode_chain)):
            if explode_chain[-x] != explode_chain[-(x +1)]:
                if explode_chain[-(x+1)] == "left":
                    if type(n_chain[-(x + 2)].right) == int:
                        n_chain[-(x+2)].right += add[1]
                    else:
                        to_change = n_chain[-(x + 2)].right
                        while type(to_change.left) != int:
                            to_change = to_change.left
                        to_change.left += add[1]
                if explode_chain[-(x+1)] == "right":
                    if type(n_chain[-(x+2)].left) == int:
                        n_chain[-(x+2)].left += add[0]
                    else:
                        to_change = n_chain[-(x + 2)].left
                        while type(to_change.right) != int:
                            to_change = to_change.right
                        to_change.right += add[0]
                break

    def split(self)-> bool:
        if type(self.left) == int and self.left >= 10:
            half = self.left / 2
            if half.is_integer():
                self.left = SNumber("[" + str(int(half)) + "," + str(int(half)) + "]", self.level + 1)
            else:
                self.left = SNumber("[" + str(int(half)) + "," + str(int(half) + 1) + "]", self.level + 1)
            self.left.parse()
            return True
        if type(self.left) != int:
            if self.left.split():
                return True
        if type(self.right) == int and self.right >= 10:
            half = self.right / 2
            if half.is_integer():
                self.right = SNumber("[" + str(int(half)) + "," + str(int(half)) + "]", self.level+1)
            else:
                self.right = SNumber("[" + str(int(half)) + "," + str(int(half) + 1) + "]", self.level + 1)
            self.right.parse()
            return True
        if type(self.right) != int:
            if self.right.split():
                return True

        return False

    def reduce(self):
        if self.can_explode():
            self.explode()
            return True
        elif self.split():
            return True
        else:
            return False

    def max_reduce(self):
        step = 0
        while self.reduce():
            step += 1
            #print("step :", step, self.print())
        return step

    def print(self):
        to_print = ""
        if type(self.left) == int:
            to_print += "[" + str(self.left)
        else:
            to_print += "[" + self.left.print()
        to_print += ","
        if type(self.right) == int:
            to_print += str(self.right) + "]"
        else:
            to_print += self.right.print() + "]"
        return to_print


with open("Input2.txt") as f:
    lines = f.read().splitlines()

for x, num in enumerate(lines):
    number = SNumber(num,0)
    number.parse()
    number.max_reduce()

    if x == 0:
        result = number
    else:
        result = result + number
        #print("le resultat brut",result.print())
        result.max_reduce()
        #print("le resultat réduit",result.print())
print(result.magnitude())

