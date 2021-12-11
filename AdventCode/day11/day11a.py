DIRECTIONS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

def is_in_grid(point: tuple) -> bool :
    return 0 <= point[0] < 10 and 0 <= point[1] < 10

class Octopus:
    def __init__(self,energy: int,):
        self.energy = energy
        self.flashed = False

    def reset(self)-> None:
        self.energy = 0
        self.flashed = False

    def gain(self) -> None:
        self.energy += 1

    def flash(self,grid: list, position: tuple)-> None:
        self.flashed = True
        for c,r in DIRECTIONS:
            neighbour = (position[0] + c, position[1] + r)
            if is_in_grid(neighbour):
                grid[neighbour[1]][neighbour[0]].gain()

def step1(grid: list) -> list:
    for c in range(10):
        for r in range(10):
            grid[r][c].gain()
    return grid

def step2(grid: list) -> list:
    nbflash = 0
    for c in range(10):
        for r in range(10):
            if grid[r][c].energy >9 and not grid[r][c].flashed:
                grid[r][c].flash(grid, (c, r))
                nbflash += 1
    if nbflash >0:
        grid = step2(grid)
    return grid

def step3(grid: list) -> tuple:
    nbflash = 0
    for c in range(10):
        for r in range(10):
            if grid[r][c].flashed:
                grid[r][c].reset()
                nbflash += 1
    return grid , nbflash

with open("Input2.txt") as f:
    lines = f.read().splitlines()

grid = []
for line in lines:
    grid.append([Octopus(int(e)) for e in line])

nbflash = 0
for step in range(100):
    grid = step1(grid)
    grid = step2(grid)
    grid, newflash = step3(grid)
    nbflash += newflash

print("step",step+1,"a flashé", nbflash)
for c in grid:
    print([octopus.energy for octopus in c])

