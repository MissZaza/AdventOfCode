f = open("Input.txt","r")
lines = f.readlines()
f.close()

dico = {'A': 'Rock','B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
dico2 = {'A': 'Rock','B': 'Paper', 'C': 'Scissors', 'X': 'lost', 'Y': 'draw', 'Z': 'win'}
Points = {'Rock': 1, 'Paper': 2, 'Scissors': 3, 'lost':0, 'draw': 3, 'win': 6}
win = [('Rock', 'Paper'),('Paper', 'Scissors'),('Scissors', 'Rock')]
def scoring(line: str):
    other = dico[line[0]]
    me = dico[line[2]]
    score = Points[me]
    if me == other:
        score += Points['draw']
    elif (other,me) in win:
        score += Points['win']
    else:
        score += Points['lost']
    return score

def playing(line: str):
    other = dico2[line[0]]
    issue = dico2[line[2]]
    score = Points[issue]
    if issue == 'draw':
        score += Points[other]
    elif issue == 'win':
        play = [line[1] for line in win if line[0]== other]
        score += Points[play[0]]
    else:
        play = [line[0] for line in win if line[1] == other]
        score += Points[play[0]]
    return score

score = 0
score2 = 0
for line in lines:
    score += scoring(line)
    score2 += playing(line)


#Part 1
print(score)

#Part 2
print(score2)