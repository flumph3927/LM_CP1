#LM 2nd Final Project
import random

base=[[[[[{'enemies':0,'shop':0,'boss':'','passage':[]},{'enemies':0,'shop':0,'boss':'','passage':[]}],
         [{'enemies':0,'shop':0,'boss':'','passage':[]},{'enemies':0,'shop':0,'boss':'','passage':[2,[0,0],[0,1],1,[0,0]]}]],

        [[{'enemies':0,'shop':0,'boss':'','passage':[1,[1,1],[0,0],2,[0,1]]},{'enemies':0,'shop':0,'boss':'','passage':[3,[0,0],[0,2],2,[0,1]]}],
         [{'enemies':0,'shop':0,'boss':'','passage':[4,[0,1],[1,0],2,[0,1]]},{'enemies':0,'shop':1,'boss':'','passage':[]}]],

        [[{'enemies':1,'shop':0,'boss':'','passage':[2,[0,1],[0,1],3,[0,2]]},{'enemies':2,'shop':0,'boss':'','passage':[7,[1,0],[2,0],3,[0,2]]}],
         [{'enemies':1,'shop':0,'boss':'','passage':[5,[0,1],[1,1],3,[0,2]]},{'enemies':0,'shop':0,'boss':[24,[4,8]],'passage':[6,[0,1],[1,2],3,[0,2]]}]]],

        [[[{'enemies':1,'shop':0,'boss':'','passage':[7,[0,0],[1,0],4,[1,0]]},{'enemies':0,'shop':0,'boss':'','passage':[2,[1,0],[0,1],4,[1,0]]}],
          [{'enemies':2,'shop':0,'boss':'','passage':[9,[0,0],[2,2],4,[1,0]]},{'enemies':2,'shop':0,'boss':'','passage':[8,[0,0],[2,1],4,[1,0]]}]],

         [[{'enemies':3,'shop':0,'boss':'','passage':[]},{'enemies':2,'shop':0,'boss':'','passage':[3,[1,0],[0,2],5,[1,1]]}],
          [{'enemies':2,'shop':0,'boss':'','passage':[7,[0,1],[1,0],5,[1,1]]},{'enemies':2,'shop':0,'boss':'','passage':[6,[1,0],[1,2],5,[1,1]]}]],

         [[{'enemies':1,'shop':0,'boss':'','passage':[]},{'enemies':2,'shop':0,'boss':'','passage':[3,[1,1],[0,2],6,[1,2]]}],
          [{'enemies':2,'shop':0,'boss':'','passage':[5,[1,1],[1,1],6,[1,2]]},{'enemies':3,'shop':0,'boss':'','passage':[]}]]],

         [[[{'enemies':3,'shop':0,'boss':'','passage':[4,[0,0],[1,0],7,[2,0]]},{'enemies':2,'shop':0,'boss':'','passage':[5,[1,0],[1,1],7,[2,0]]}],
           [{'enemies':2,'shop':0,'boss':'','passage':[3,[1,0],[0,2],7,[2,0]]},{'enemies':0,'shop':0,'boss':[36,[5,9]],'passage':[]}]],

          [[{'enemies':random.randint(2,4),'shop':0,'boss':'','passage':[4,[1,1],[1,0],8,[2,1]]},{'enemies':0,'shop':0,'boss':[36,[5,9]] if random.randint(0,1) else '','passage':[]}],
           [{'enemies':random.randint(1,6),'shop':0,'boss':'','passage':[]},{'enemies':random.randint(1,5),'shop':0,'boss':'','passage':[9,[1,0],[2,2],8,[2,1]]}]],

          [[{'enemies':1,'shop':0,'boss':'','passage':[4,[1,0],[1,0],9,[2,2]]},{'enemies':1,'shop':0,'boss':'','passage':[]}],
           [{'enemies':1,'shop':0,'boss':'','passage':[8,[1,1],[2,1],9,[2,2]]},{'enemies':1,'shop':0,'boss':[48,[6,10]],'passage':[]}]]]],
           {10:{'Daggers':[8,'spd']},10:{'Greatsword':[8,'str']},10:{'Spell':[8,'mag']}},[48,[6,10]]]

def creation():
    total=random.randint(3,20)
    print(f'You have {total} points to put into three scores, strength, speed, and magic.')
    while True:
      try:
        str=int(input('How many points do you want to put into strength?'))
        break
      except:
        print('Invalid input, try again.')
    while True:
      try:
        spd=int(input('How many points do you want to put into speed?'))
        break
      except:
        print('Invalid input, try again.')
    while True:
      try:
        mag=int(input('How many points do you want to put into magic?'))
        break
      except:
        print('Invalid input, try again.')
    return [random.randint(5,15)+str+spd, random.randint(5,15)+str+spd, (random.randint(5,15)+str+spd)/4, str, spd, mag, 0, {'base attack':[6,'str']}]

def display_map(area, coord):
  print(f'Map of area{area[0]}:\n')
  out=''
  for x in area[1]:
    for i in x:
      end=''
      if i==area[1][coord[0]][coord[1]]:
        end+='*'
      if i['passage']:
        end+='^'
      if i['boss']:
        end+='!'
      end+=' '*(4-len(end))
      out+=end
    out+='\n'
  print(out)
  print('key:\n*: current location\n^:passage to another area\n!: boss')
  print('Area grid:\n1 2 3\n4 5 6\n7 8 9')

def move(coord):
  print('Possible move directions:')
  poss=[]
  if coord[0]==0:
    print('Down')
    poss.append('down')
  else:
    print('Up')
    poss.append('up')
  if coord[1]==0:
    print('Right')
    poss.append('right')
  else:
    print('Left')
    poss.append('left')
  choice=input('What direction would you like to move?').lower()
  while choice not in poss:
    print('Invalid input. Try again.')
    choice=input('What direction would you like to move?').lower()
  if choice == 'down':
    coord[0]=1
  if choice == 'up':
    coord[0]=0
  if choice == 'right':
    coord[1]=1
  if choice == 'left':
    coord[1]=0
  return coord

def transport(item, select, areas):
  areas[0][item[4][0]][item[4][1]]=select
  print(f'Moving to area {item[0]}.')
  return [item[0],areas[0][item[2][0]][item[2][1]]], item[1], areas

def combat(player):
  enemy=[12,2]
  while True:
    print('Possible attacks:\n', player[-1])
    attack=input('What attack would you like to use?')
    while attack not in player[-1]:
      print('Invalid input. Try again.')
      attack=input('What attack would you like to use?')
    if player[-1][attack][0]=='str':
      dmg=(player[-1][attack][0]+player[3])*random.random()*2
    elif player[-1][attack][0]=='spd':
      dmg=(player[-1][attack][0]+player[4])*random.random()*2
    elif player[-1][attack][0]=='mag':
      dmg=(player[-1][attack][0]+player[5])*random.random()*2
    print(f'You deal {int(dmg)} damage to the enemy.')
    enemy[0]-=int(dmg)