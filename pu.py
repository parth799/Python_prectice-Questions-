import random
def game(comp,you):
    if comp == you:
        return None
    elif comp=='s':
        if you=="p":
            return False
        elif you=='g':
            return True
    elif comp=='p':
        if you=="c":
            return False
        elif you=='s':
            return True
    elif comp=='c':
        if you=="s":
            return False
        elif you=='p':
            return True
print("comp 1 turn : stone(s) paper(p) or scissors(c)?")
randno = random.randint(1,3)
if randno == 1:
    comp ='s'
elif randno == 2:
    comp = 'p'
elif randno == 3:
    comp = 'c'

you=input("your 2 turn : stone(s) paper(p) or scissors(c)?\n")
a=game(comp,you)
if a==None:
    print("the game is a tie!")
elif a:
    print("you win!")
else:
    print("you lose!")