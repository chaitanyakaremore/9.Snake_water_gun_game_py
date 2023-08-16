import random
#snake,water,gun
def gameWin(comp,you):
    #if two values are equal ,declear tied!
    if comp==you:
        return None
    #check all posibilitis when computer choose s
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
     #check all posibilitis when computer choose w
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    #check all posibilitis when computer choose g
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
        
print("comp turn: Snake(s) Water(w) or Gun(g)?")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

you=input("Your Turn: Snake(s) Water(w) Gun(g)?")
a=gameWin(comp,you)

print(f"Computer Choose {comp}")
print(f"You Choose {you}")

if a==None:
    print("The game is tied!")
elif a:
    print("You Win")
else:
    print("You loss")
    