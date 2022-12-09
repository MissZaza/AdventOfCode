"""
x_min = 20
x_max = 30
y_min = -10
y_max = -5

""" 
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
            self.x_vel -= 1
        self.y_vel -= 1

    def is_in_target(self):
        return x_min <= probe.x <= x_max and y_min <= probe.y <= y_max


nb_ok_launch = 0
for x_vel in range(0,288):
    for y_vel in range(-103,110):
        probe = Probe(x_vel, y_vel)
        while not (probe.x > x_max or probe.y < y_min):
            probe.next_point()
            if probe.is_in_target():
                nb_ok_launch += 1
                break

print(nb_ok_launch)