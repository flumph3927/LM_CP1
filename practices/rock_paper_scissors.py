#LM 2nd Rock Paper Scissors
import random
score=[0,0]
while True:
    comp2=77584368927017369370292 #needed in the event of rock and scissors. defaults to arbitrarily large number
    choice2=798043659823759836175691
    print('The round has begun.')
    print('What do you choose:\n1. Rock\n2. Paper\n3. Scissors\n(any other character to quit)')
    choice=input()
    if choice=='1' or choice=='2' or choice=='3':
        choice=int(choice)
    else:
        print('Terminating program')
        break
    if choice==3:
        choice2=0
    comp=random.randint(1,3)
    if comp==3:
        comp2=0
    if comp==1:
        print('The computer chose Rock')
    elif comp==2:
        print('The computer chose Paper')
    else:
        print('The computer chose Scissors')
    if choice+1==comp or choice2+1==comp or choice+1==comp2 or choice2+1==comp2:
        print('The computer wins!')
        score[1]+=1
    elif choice-1==comp or choice2-1==comp or choice-1==comp2 or choice2-1==comp2:
        print('You win!')
        score[0]+=1
    else:
        print('It\'s a tie!')
    print(f'The score is now {score[0]} to {score[1]}')
    if score[0]>score[1]:
        print('You are winning!')
    elif score[0]<score[1]:
        print('The computer is winning!')
    else:
        print('It is a tie!')