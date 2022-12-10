f = open("Input.txt","r")
lines = f.read().splitlines()
f.close()


def draw(screen, cycle, x):
    row, pos = int((cycle-1)/40), ((cycle-1) % 40)
    if pos in [ x-1, x, x +1]:
        screen[row]+= "#"
    else:
        screen[row] += "."
    return None


cycle = 0
X = 1
st_signal =0
screen = ["" for rows in range(6)]
for line in lines:
    if line == 'noop':
        cycle += 1
        draw(screen,cycle,X)
        if cycle in [20,60,100,140,180,220]:
            st_signal += cycle * X
    else:
        add, move = line.split()
        cycle += 1
        draw(screen, cycle, X)
        if cycle in [20,60,100,140,180,220]:
            st_signal += cycle * X
        cycle +=1
        draw(screen, cycle, X)
        if cycle in [20,60,100,140,180,220]:
            st_signal += cycle * X
        X += int(move)

#Part 1
print('Part1', st_signal)

#Part 2
print('Part2')
for row in screen:
    print(row)



