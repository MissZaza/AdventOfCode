f = open("Input.txt","r")
lines = f.readlines()
f.close()


def full_overlap(assign: list):
    ass1 = assign[0].split('-')
    ass2 = assign[1].split('-')
    if int(ass1[0]) in range(int(ass2[0]), int(ass2[1])+1) and int(ass1[1]) in range(int(ass2[0]), int(ass2[1])+1):
        return True
    elif int(ass2[0]) in range(int(ass1[0]), int(ass1[1])+1) and int(ass2[1]) in range(int(ass1[0]), int(ass1[1])+1):
        return True
    else:
        return False

def partial_overlap(assign: list):
    ass1 = assign[0].split('-')
    ass2 = assign[1].split('-')
    if int(ass1[0]) in range(int(ass2[0]), int(ass2[1])+1) or int(ass1[1]) in range(int(ass2[0]), int(ass2[1])+1):
        return True
    elif int(ass2[0]) in range(int(ass1[0]), int(ass1[1])+1) or int(ass2[1]) in range(int(ass1[0]), int(ass1[1])+1):
        return True
    else:
        return False


full_over = 0
part_over = 0
for line in lines:
    assignt = line.split(',')
    if full_overlap(assignt):
        full_over += 1
    if partial_overlap(assignt):
        part_over +=1

# Part 1
print(full_over)



#Part 2


print(part_over)
