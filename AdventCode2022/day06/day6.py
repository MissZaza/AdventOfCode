f = open("Input.txt","r")
lines = f.read().splitlines()
f.close()

#Part 1
cpt = 4
buffer =lines[0][0:4]

if len(set(buffer)) == 4:
    print(buffer)
    print(set(buffer))
    print(4)

for char in lines[0][4:]:
    cpt += 1
    if cpt>=4:
        buffer = buffer[1:4] + char
        if len(set(buffer)) == 4:
            print('stop')
            break

print(cpt)






#Part 2

cpt2 = 14
buffer =lines[0][0:14]

if len(set(buffer)) == 14:
    print(buffer)
    print(set(buffer))
    print(14)

for char in lines[0][14:]:
    cpt2 += 1

    buffer = buffer[1:14] + char
    if len(set(buffer)) == 14:
        print('stop')
        break

print(cpt2)