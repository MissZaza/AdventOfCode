with open("Input2.txt") as f:
    lines = f.read().splitlines()


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

    def sum_version(self):
        return self.version + sum(p.sum_version() for p in self.sub_packet)


transmission = bin(int(lines[0], 16))[2:].zfill(len(lines[0])*4)

packet = Packet()
i = AtomicInteger()
print(transmission)
packet.parse(transmission, i)

print(packet.sum_version())