x_min = 265
x_max = 287
y_min = -103
y_max = -58



class Probe:
    def __init__(self, x_vel: int, y_vel: int):
        self.x = 0
        self.y = 0
        self.x_vel = x_vel
        self.y_vel = y_vel

    def next_point(self) -> None:
        self.x += self.x_vel
        self.y += self.y_vel
        if self.x_vel != 0:
            self.x_vel = abs(self.x_vel - 1) * int(self.x_vel/abs(self.x_vel))
        self.y_vel -= 1


"""
for x in range(15,25):
    print(x,sum(range(x)))  #x => 24

"""
for y_vel in range(100,110):
    probe = Probe(23, y_vel)
    highest_y = 0
    while (probe.x < x_min and probe.x_vel != 0) or probe.y > y_max:
        probe.next_point()
        #print(probe.x, probe.y)
        highest_y =  max(probe.y, highest_y)
    if x_min <= probe.x <= x_max and y_min <= probe.y <= y_max:
        print( "For y velocity", y_vel, "Highest y = ", highest_y)
    else:
        print("For y velocity", y_vel,"probe didn't reach the target area")
