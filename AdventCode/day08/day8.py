f = open("Input2.txt","r")
lines = f.readlines()
f.close()


class Digit:
    def __init__(self, input):
        self.bit = input
        self.nbit = len(input)

    def has(self, bitlist):
        result = True
        for bit in bitlist:
            if bit not in self.bit:
                result = False
        return result

    def isd(self, bitlist):
        if self.nbit == len(bitlist) and self.has(bitlist):
            return True
        else:
            return False


class Connexion:
    def __init__(self, input):
        output = input[1].replace("\n", "")
        self.pattern = [Digit(digit) for digit in input[0].split(" ")]
        self.output = [Digit(digit) for digit in output.split(" ")]
        self.decode = {}
        for digit in self.pattern:
            if digit.nbit == 2:
                self.decode[1] = digit.bit
            elif digit.nbit == 3:
                self.decode[7] = digit.bit
            elif digit.nbit == 4:
                self.decode[4] = digit.bit
            elif digit.nbit == 7:
                self.decode[8] = digit.bit

    def nb_easy(self):
        nb_easy = len([digit for digit in self.output if len(digit) in [2, 3, 4, 7]])
        #print(self.output, nb_easy)
        return nb_easy

    def solve(self):
        result = ""
        for digit in [digit for digit in self.pattern if digit.nbit == 6]:
                if digit.has(self.decode[1]):
                    if digit.has(self.decode[4]):
                        self.decode[9] = digit.bit
                    else:
                        self.decode[0] = digit.bit
                else:
                    self.decode[6] = digit.bit
        ebar = self.decode[8]
        for bit in self.decode[9]:
            ebar = ebar.replace(bit, "")
        for digit in [digit for digit in self.pattern if digit.nbit == 5]:
            if digit.has(self.decode[7]):
                self.decode[3] = digit.bit
            elif digit.has(ebar):
                self.decode[2] = digit.bit
            else:
                self.decode[5] = digit.bit
        for digit in self.output:
            for k in self.decode.keys():
                if Digit(self.decode[k]).isd(digit.bit):
                    result = result + str(k)
        #print(result, ebar, self.decode[5])
        return int(result)

    
connexions = []
for line in lines:
    connexions.append(Connexion(line.split(" | ")))

result = 0
for x in connexions:
   result = result + x.solve()

print(result)
