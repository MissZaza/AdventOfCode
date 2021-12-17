def prod(liste: iter) -> int:
    prod = 1
    for x in liste:
        prod *= x
    return prod


class AtomicInteger:
    def __init__(self):
        self.value = 0

    def get(self) -> int:
        return self.value

    def grow(self, to_add: int) -> int:
        self.value += to_add
        return self.value


class Packet:
    def __init__(self):
        self.version = int()
        self.type_id = int()
        self.value = int()
        self.sub_packet = []

    @property
    def is_operator(self) -> bool:
        return self.type_id != 4

    def parse(self, bits: str, i: AtomicInteger):
        self.version = int(bits[i.get():i.grow(3)], 2)
        self.type_id = int(bits[i.get():i.grow(3)], 2)
        if self.is_operator:
            if bits[i.get():i.grow(1)] == '0': # if info of total length
                total_l = int(bits[i.get():i.grow(15)], 2)+ i.get()
                while i.get() < total_l:
                    new_packet = Packet()
                    new_packet.parse(bits,i)
                    self.sub_packet.append(new_packet)
            else: # if info of total sub packet
                nb_sub = int(bits[i.get():i.grow(11)], 2)
                for nb in range(nb_sub):
                    new_packet = Packet()
                    new_packet.parse(bits, i)
                    self.sub_packet.append(new_packet)
        else:
            message = ""
            while bits[i.get():i.grow(1)] == "1":
                message += bits[i.get():i.grow(4)]
            self.value = int(message + bits[i.get():i.grow(4)], 2)

    def sum_version(self) -> int():
        return self.version + sum(p.sum_version() for p in self.sub_packet)

    def get_value(self) -> int:
        if self.is_operator:
            if self.type_id == 0:
                if len(self.sub_packet) > 1:
                    return sum(p.get_value() for p in self.sub_packet)
                else:
                    return self.sub_packet[0].get_value()
            elif self.type_id == 1:
                if len(self.sub_packet) > 1:
                    return prod(p.get_value() for p in self.sub_packet)
                else:
                    return self.sub_packet[0].get_value()
            elif self.type_id == 2:
                return min(p.get_value() for p in self.sub_packet)
            elif self.type_id == 3:
                return max(p.get_value() for p in self.sub_packet)
            elif self.type_id == 5:
                if self.sub_packet[0].get_value() > self.sub_packet[1].get_value():
                    return 1
                else:
                    return 0
            elif self.type_id == 6:
                if self.sub_packet[0].get_value() < self.sub_packet[1].get_value():
                    return 1
                else:
                    return 0
            else:
                if self.sub_packet[0].get_value() == self.sub_packet[1].get_value():
                    return 1
                else:
                    return 0
        else:
            return self.value


"""
with open("Input") as f:
    lines = f.read().splitlines()
for line in lines:
    transmission = bin(int(line, 16))[2:].zfill(len(line) * 4)
    packet = Packet()
    i = AtomicInteger()
    packet.parse(transmission, i)
    print(packet.get_value())
"""

with open("Input2.txt") as f:
    lines = f.read().splitlines()
transmission = bin(int(lines[0], 16))[2:].zfill(len(lines[0])*4)

packet = Packet()
i = AtomicInteger()
packet.parse(transmission, i)
print(packet.get_value())




