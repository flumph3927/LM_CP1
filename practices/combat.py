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
            print(f'You deal {dmg} damage.')
            if monster[0]<=0:
                monster[0]=0
                print('You defeat the monster!')
        return attrib, monster
    elif choice=='2':
        if random.randint(1,20)+attrib[4]>=10:
            monster[0] = -1
            print('You successfully escape!')
        else:
            print('You fail to flee.')
        return attrib, monster
    elif choice=='3':
        if random.randint(1,20)+attrib[4]>=random.randint(6,15):
            print('You successfully hide!\nThe monster cannot find you!')
            attrib, monster = playerTurn(attrib, monster)
        else:
            print('You fail to hide.')
        return attrib, monster
    else:
        print('You do nothing.')
        return attrib, monster

def monsterTurn(attrib,monster):
    print('The monster\'s turn!')
    print('The monster is attacking you!')
    hit=random.randint(1,20)+monster[2]
    if attrib[1]>hit:
        hits='misses'
    else:
        hits='hits'
    print(f'The monster {hits} you with a {hit}.')
    dmg=0
    if hits=='hits':
        dmg+=random.randint(1,6)*2
        attrib[0]-=dmg
        print(f'The monster deals {dmg} damage')
        if attrib[0]<=0:
            attrib[0]=0
            print('You are dead.')
        else:
            print(f'You now have {attrib[0]} hit points.')
    return attrib, monster

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
player=[health,defense,attack,damage,stealth]
enemy=[random.randint(5,15),random.randint(8,18),random.randint(2,8)]

combat=True
if player[2]>enemy[2]:
    print('You go first!')
    last='m'
else:
    print('The monster goes first.')
    last='p'
while combat:
    if last=='m':
        player,enemy=playerTurn(player,enemy)
        last='p'
    else:
        player,enemy=monsterTurn(player,enemy)
        last='m'
    if enemy[0]<1:
        combat=False
        print('You win!')
    elif player[0]<1:
        combat=False
        print('You lost.')