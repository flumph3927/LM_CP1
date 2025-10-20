import random

bord=[1,2,3,4,5,6,7,8,9]
while True:
    if input('Do you want to quit(y to quit)(anything else to continue)\n')=='y':
        break
    print(bord[0],bord[1],bord[2])
    print(bord[3],bord[4],bord[5])
    print(bord[6],bord[7],bord[8])
    player=input('Enter a square from 1-9\n')
    comp=random.randint(0,8)
    bord[int(player)-1] = 'o'
    bord[comp] = 'x'

    if bord[0] == "x" and bord[1] == "x" and bord[2] == "x":
        print("player win")
        break
    elif bord[3] == "x" and bord[4] == "x" and bord[5] == "x":
        print("player win")
        break
    elif bord[6] == "x" and bord[7] == "x" and bord[8] == "x":
        print("player win")
        break

    if bord[0] == "x" and bord[3] == "x" and bord[6] == "x":
        print("player win")
        break
    elif bord[1] == "x" and bord[4] == "x" and bord[7] == "x":
        print("player win")
        break
    elif bord[2] == "x" and bord[5] == "x" and bord[8] == "x":
        print("player win")
        break

    if bord[0] == "x" and bord[4] == "x" and bord[8] == "x":
        print("player win")
        break
    elif bord[2] == "x" and bord[4] == "x" and bord[6] == "x":
        print("player win")
        break
    if bord[0] == "x" and bord[1] == "x" and bord[2] == "x":
        print("computer won")
        break
    elif bord[3] == "x" and bord[4] == "x" and bord[5] == "x":
        print("computer won")
        break
    elif bord[6] == "x" and bord[7] == "x" and bord[8] == "x":
        print("computer won")
        break
    if bord[0] == "x" and bord[4] == "x" and bord[8] == "x":
        print("computer won")
        break
    elif bord[6] == "x" and bord[4] == "x" and bord[2] == "x":
        print("computer won")
        break
    if bord[0] == "x" and bord[3] == "x" and bord[6] == "x":
        print("computer won")
        break
    elif bord[1] == "x" and bord[4] == "x" and bord[7] == "x":
        print("computer won")
        break
    elif bord[0] == "x" and bord[5] == "x" and bord[8] == "x":
        print("computer won")
        break