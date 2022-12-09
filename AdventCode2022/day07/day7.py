f = open("Input.txt","r")
lines = f.read().splitlines()
f.close()


class Dir:
    def __init__(self, name):
        self.name = name
        self.taille = 0
        self.sous_dir = []
        self.path = []

    def taille_tot(self, dossier : list):
        if len(self.sous_dir) == 0:
            return self.taille
        else:
            taille = self.taille
            for dir in self.sous_dir:
                path = self.path.copy()
                path.append(self.name)
                d = [doss for doss in dossier if doss.name == dir and doss.path == path]
                taille += d[0].taille_tot(dossier)
            return taille


dossier = []
parent = []
for line in lines:
    command = line.split(" ")
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] not in ['..']:
                dossier.append(Dir(command[2]))
                if command[2] == '/':
                    parent = ['/']
                else:
                    dossier[-1].path = parent.copy()
                    parent.append(command[2])
            else:
                parent.pop(-1)
    elif command[0] == "dir":
        dossier[-1].sous_dir.append(command[1])
    else:
        dossier[-1].taille += int(command[0])

#Part 1
cumul_taille = 0
dirs=[]
for dir in dossier:
    t = dir.taille_tot(dossier)
    dirs.append( t)
    if t <= 100000:
        cumul_taille += t

print('Part1', cumul_taille)

#Part 2
possible_dir = [ taille for taille in dirs if taille >= 8381165 ]

print('Part2', min(possible_dir))





#Part 2
