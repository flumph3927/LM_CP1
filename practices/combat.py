#LM 2nd Combat Game
import random

def playerTurn(attrib,monster):
    print('Your turn!')
    choice=input('1. Attack\n2. Flee\n3. Hide\nAnything else to Pass\n')
    if choice=='1':
        print('Rolling to hit.')
        hit=random.randint(1,20)+attrib[2]
        if monster[1]>hit:
            hits='miss'
        else:
            hits='hit'
        print(f'You {hits} with a {hit}.')
        dmg=0
        if hits=='hit':
            for i in range(int(attrib[3][0][0])):
                dmg+=random.randint(1,int(attrib[3][0][2]))
            monster[0]-=dmg
            print('You deal {dmg} damage.')
            if monster[0]<=0:
                monster=0
                print('You defeat the monster!')
            return attrib, monster
    elif choice==2:
        if random.randint(1,20)+attrib[4]<=10:
            monster[0] = -1
            print('You successfully escape!')
        else:
            print('You fail to flee.')
    elif choice==3:


name=input('What is your character\'s name? ')
clas=input('What class are you?\n1. Fighter\n2. Rogue\n3. Mage\n')
if clas == '1':
    health=14
    defense=16
    attack=6
    damage=['2d6',4]
    stealth=1
elif clas == '2':
    health=10
    defense=12
    attack=6
    damage=['2d4',4]
    stealth=8
elif clas == '3':
    health=6
    defense=10
    attack=6
    damage=['8d4',4]
    stealth=0
else:
    print('Incorrect input. Error imminent.')
print(f'Your stats are:\nHealth: {health}\nDefense: {defense}\nAttack: {attack}\nDamage: {damage[0]}+{damage[1]}\nStealth: {stealth}')