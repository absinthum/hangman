import random
import string

reci = ['python', 'java', 'kotlin', 'javascript']
rec = random.choice(reci)
rec_l = list(rec)

st_in = len(rec_l) * '-'
lives = 8
pog = set()
prob = set()

print('H A N G M A N')
print()
print(st_in)
st_in = list(st_in)
pisi = len(rec_l) * '-'

while lives != 0:
    nn = len(pog)
    print('Input a letter: > ')
    n = input()

    if len(n) != 1:
        print('You should print a single letter')
        print()
        print(pisi)
        continue
    if not (n.isascii() and n.islower()):
        print('It is not an ASCII lowercase letter')
        print()
        print(pisi)
        continue


    if n in prob:
        print('You already typed this letter')

    for a in range(len(rec_l)):
        if n == rec_l[a]:
            pog.add(n)
        if rec_l[a] in pog:
            st_in[a] = rec_l[a]
    pisi = ''
    for b in range(len(rec_l)):
        pisi += st_in[b]
    if n not in pog and n not in prob:
        print('No such letter in the word')
        lives -= 1
        if lives == 0:
            break
    prob.add(n)
    if pisi == rec:
        print('You guessed the word!')
        print('You survived!')
        break
    print()
    print(pisi)

if lives == 0:
    print('You are hanged!')
