BORDER = 2
class Image:
    def __init__(self, pixels: list, infinite : str):
        self.pixels = pixels
        self.infinite = infinite

    @property
    def x_len(self) -> int:
        return len(self.pixels[0])

    @property
    def y_len(self) -> int:
        return len(self.pixels)

    @property
    def nb_lit(self):
        nb_lit =0
        for line in self.pixels[BORDER:-BORDER]:
            for pixel in line[BORDER:-BORDER]:
                if pixel == "#":
                    nb_lit += 1
        return nb_lit

    def in_image(self,x,y):
        return 0 <= x < self.x_len and 0 <= y < self.y_len

    def decode(self, x: int, y: int) -> int:
        nine_pix = [self.infinite]*9
        index = 0
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                #print("x,y =", x,y, "index=", index, "r,c =", r,c)
                if self.in_image(x + c - BORDER, y + r - BORDER):
                    #print("x,y =", x,y, "index=", index, "r,c =", r,c,self.pixels[y+r-1][x+c-1] )
                    nine_pix[index] = decode(self.pixels[y+r-BORDER][x+c-BORDER])
                index += 1
        return int("".join(nine_pix), 2)

    def enhance(self, algorithm: str):
        new_image = [""] * (self.y_len + BORDER *2)
        for y in range(self.y_len + BORDER *2):
            for x in range(self.x_len + BORDER*2):
                new_image[y] += algorithm[self.decode(x, y)]
        if self.infinite == "0":
            infinite = "1"
        else:
            infinite = "0"
        return Image(new_image, infinite)


def decode(code: str)->str:
    if code == "#":
        return "1"
    else:
        return "0"


with open("input2.txt") as f:
    lines = f.read().splitlines()

algorithm = lines[0]
image = Image(lines[2:], "0")


for step in range(50):
    image = image.enhance(algorithm)


print(image.nb_lit)