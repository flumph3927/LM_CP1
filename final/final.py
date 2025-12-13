#LM 2nd Final Project
import random

base=[[[[[{'enemies':0,'shop':0,'boss':'','passage':0},{'enemies':0,'shop':0,'boss':'','passage':''}],
         [{'enemies':0,'shop':0,'boss':'','passage':[]},{'enemies':0,'shop':0,'boss':'','passage':[2,[0,0],[0,1],1,[0,0]]}]],

        [[{'enemies':0,'shop':0,'boss':'','passage':[1,[1,1],[0,0],2,[0,1]]},{'enemies':0,'shop':0,'boss':'','passage':[3,[0,0],[0,2],2,[0,1]]}],
         [{'enemies':0,'shop':0,'boss':'','passage':[4,[0,1],[1,0],2,[0,1]]},{'enemies':0,'shop':1,'boss':'','passage':[]}]],

        [[{'enemies':1,'shop':0,'boss':'','passage':[2,[0,1],[0,1],3,[0,2]]},{'enemies':2,'shop':0,'boss':'','passage':[7,[2,0],[2,0],3,[0,2]]}],
         [{'enemies':1,'shop':0,'boss':'','passage':[5,[0,1],[1,1],3,[0,2]]},{'enemies':0,'shop':0,'boss':[24,[4,8]],'passage':[6,[0,1],[1,2],3,[0,2]]}]]],

        [[[{'enemies':1,'shop':0,'boss':'','passage':[7,[0,0],[2,0],4,[1,0]]},{'enemies':0,'shop':0,'boss':'','passage':[2,[1,0],[0,1],4,[1,0]]}],
          [{'enemies':2,'shop':0,'boss':'','passage':[9,[0,0],[2,2],4,[1,0]]},{'enemies':2,'shop':0,'boss':'','passage':[8,[0,0],[2,1],4,[1,0]]}]],

         [[{'enemies':3,'shop':0,'boss':'','passage':[]},{'enemies':2,'shop':0,'boss':'','passage':[3,[1,0],[0,2],5,[1,1]]}],
          [{'enemies':2,'shop':0,'boss':'','passage':[7,[0,1],[2,0],5,[1,1]]},{'enemies':2,'shop':0,'boss':'','passage':[6,[1,0],[1,2],5,[1,1]]}]],

         [[{'enemies':1,'shop':0,'boss':'','passage':[]},{'enemies':2,'shop':0,'boss':'','passage':[3,[1,1],[0,2],6,[1,2]]}],
          [{'enemies':2,'shop':0,'boss':'','passage':[5,[1,1],[1,1],6,[1,2]]},{'enemies':3,'shop':0,'boss':'','passage':[]}]]],

         [[[{'enemies':3,'shop':0,'boss':'','passage':[4,[0,0],[1,0],7,[2,0]]},{'enemies':2,'shop':0,'boss':'','passage':[5,[1,0],[1,1],7,[2,0]]}],
           [{'enemies':2,'shop':0,'boss':'','passage':[3,[1,0],[0,2],7,[2,0]]},{'enemies':0,'shop':0,'boss':[36,[5,9]],'passage':[]}]],

          [[{'enemies':random.randint(2,4),'shop':0,'boss':'','passage':[4,[1,1],[1,0],8,[2,1]]},{'enemies':0,'shop':0,'boss':[36,[5,9]] if random.randint(0,1) else '','passage':[]}],
           [{'enemies':random.randint(1,6),'shop':0,'boss':'','passage':[]},{'enemies':random.randint(1,5),'shop':0,'boss':'','passage':[9,[1,0],[2,2],8,[2,1]]}]],

          [[{'enemies':1,'shop':0,'boss':'','passage':[4,[1,0],[1,0],9,[2,2]]},{'enemies':1,'shop':0,'boss':'','passage':[]}],
           [{'enemies':1,'shop':0,'boss':'','passage':[8,[1,1],[2,1],9,[2,2]]},{'enemies':1,'shop':0,'boss':[65,[6,10]],'passage':[]}]]]],
           {8:{'Daggers':[8,'spd']},9:{'Greatsword':[8,'str']},10:{'Spell':[10,'mag']}},[65,[6,10]]]

def tutorial():
  print('You will have points to put into three scores: \nStrength affects strength-based attacks and health\nSpeed affects speed-based attacks and health\nMagic affects magic-based attack, which are stronger\n\nYou can buy attacks and score upgrade at the shop in area 2.\nThe areas are arranged in a grid of\n1 2 3\n4 5 6\n7 8 9\n\nEach area has four rooms. These are shown in a four by  four grid with no border, and a key to what the characters mean is below it.\n\nYour goal is to kill the final boss, which is in area 9.\n\nKilling enemies gives you 1 coin each\nKilling bosses gives you 10 coins.\n')

def creation():
    total=random.randint(13,30)
    print(f'You have {total} points to put into three scores, strength, speed, and magic.')
    while True:
      try:
        str=int(input('How many points do you want to put into strength?'))
        if total-str >=0:
          total-=str
        else:
          print('You do not have that many points.')
          continue
        break
      except:
        print('Invalid input, try again.')
    while True:
      try:
        spd=int(input('How many points do you want to put into speed?'))
        if total-spd >=0:
          total-=spd
        else:
          print('You do not have that many points.')
          continue
        break
      except:
        print('Invalid input, try again.')
    while True:
      try:
        mag=int(input('How many points do you want to put into magic?'))
        if total-mag >=0:
          total-=mag
        else:
          print('You do not have that many points.')
          continue
        break
      except:
        print('Invalid input, try again.')
    return [random.randint(5,15)+str+spd, random.randint(5,15)+str+spd, int((random.randint(5,15)+str+spd)/4), str, spd, mag, 0, {'base':[6,'str']}]

def displayMap(area, coord):
  print(f'\nMap of area{area[0]}:\n')
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
      if i['shop']:
        end+='$'
      end+=' '*(5-len(end))
      out+=end
    out+='\n'
  print(out,'\n')
  print('key:\n*: current location\n^:passage to another area\n!: boss\n$: shop')
  print('Area grid:\n1 2 3\n4 5 6\n7 8 9\n')

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
  choice=input('\nWhat direction would you like to move?').lower()
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
  areas[item[4][0]][item[4][1]]=select[1]
  print(f'Moving to area {item[0]}.')
  return [item[0],areas[item[2][0]][item[2][1]]], item[1], areas

def combat(player):
  enemy=[12,2]
  while True:
    print('Possible attacks:')
    for i in player[-1].keys():
      print(f'{i}: {player[-1][i][0]} damage. Uses {player[-1][i][1]} score.')
    attack=input('What attack would you like to use?')
    while attack not in player[-1]:
      print('Invalid input. Try again.')
      attack=input('What attack would you like to use?')
    if player[-1][attack][1]=='str':
      dmg=(player[-1][attack][0]+player[3])*random.random()*2
    elif player[-1][attack][1]=='spd':
      dmg=(player[-1][attack][0]+player[4])*random.random()*2
    elif player[-1][attack][1]=='mag':
      dmg=(player[-1][attack][0]+player[5])*random.random()*2
    print(f'You deal {int(dmg)} damage to the enemy.\n')
    enemy[0]-=int(dmg)
    if player[2]<1 or player[1]<1:
      print('You are defeated.')
      player[2]=int(player[0]/4)
      return player
    elif enemy[0]<1:
      print('You defeat the enemy. You get a coin.')
      player[2]=int(player[0]/4)
      player[6]+=1
      return player
    player[1]-=int(enemy[1]*random.random()*2)
    player[2]-=int(enemy[1]*random.random()*2)
    print(f'The enemy attacked. You are now at {player[1]} health and {player[2]} health remaining in this battle.\n')
    if player[2]<1 or player[1]<1:
      print('You are defeated.')
      player[2]=int(player[0]/4)
      return player
    elif enemy[0]<1:
      print('You defeat the enemy. You get a coin.')
      player[2]=int(player[0]/4)
      player[6]+=1
      return player

def bossCombat(player,boss,final):
  if boss==final:
    end=True
    print('This is the final boss.')
  else: end=False
  while True:
    print('Possible attacks:')
    for i in player[-1].keys():
      print(f'{i}: {player[-1][i][0]} damage. Uses {player[-1][i][1]} score.')
    attack=input('What attack would you like to use?')
    while attack not in player[-1]:
      print('Invalid input. Try again.')
      attack=input('What attack would you like to use?')
    if player[-1][attack][1]=='str':
      dmg=(player[-1][attack][0]+player[3])*random.random()*2
    elif player[-1][attack][1]=='spd':
      dmg=(player[-1][attack][0]+player[4])*random.random()*2
    elif player[-1][attack][1]=='mag':
      dmg=(player[-1][attack][0]+player[5])*random.random()*2
    print(f'You deal {int(dmg)} damage to the boss.\n')
    boss[0]-=int(dmg)
    if player[2]<1:
      print('You are defeated.')
      return player, boss
    elif boss[0]<1:
      print('You defeat the boss.')
      if end: final[0]=0
      boss=0
      player[6]+=10
      scr=input('What score would you like to upgrade?(str, spd, mag)').lower()
      while scr not in ['str','spd','mag']:
        scr=input('What score would you like to upgrade?(str, spd, mag)').lower()
      if scr=='str':
        player[3]+=1
      if scr=='spd':
        player[4]+=1
      if scr=='mag':
        player[5]+=1
      return player,boss
    player[1]-=int(random.choice(boss[1])*random.random()*2)
    print(f'The boss attacked. You are now at {player[1]} health.\n')
    if player[1]<1:
      print('You are defeated.')
      return player, boss
    elif boss[0]<1:
      print('You defeat the boss.')
      if end: final[0]=0
      boss=0
      player[6]+=10
      scr=input('What score would you like to upgrade?(str, spd, mag)').lower()
      while scr not in ['str','spd','mag']:
        scr=input('What score would you like to upgrade?(str, spd, mag)').lower()
      if scr=='str':
        player[3]+=1
      if scr=='spd':
        player[4]+=1
      if scr=='mag':
        player[5]+=1
      return player,boss

def shop(player, items):
  while True:
    print(f'You have {player[6]} coins.')
    print('Avaliable shop items:(price: item)')
    check=['str','spd','mag']
    for i in items.keys():
      print(f'{i}: {list(items[i].keys())[0]} ({items[i][list(items[i].keys())[0]][0]} damage, uses {items[i][list(items[i].keys())[0]][1]} score.)')
      check.append(list(items[i].keys())[0])
    print('11:str up\n11:spd up\n11: mag up')
    buy=input('What item would you like to buy? L to leave shop.')
    while buy not in check:
      buy=input('What item would you like to buy? L to leave shop.')
    if buy.lower()=='l': break
    if buy in ['str','spd','mag']:
      player[6]-=11
      if buy=='str':
        player[3]+=1
      if buy=='spd':
        player[4]+=1
      if buy=='mag':
        player[5]+=1
    else:
      for i in items.keys():
        if list(items[i].keys())[0]==buy:
          player[-1][buy]==items[i][list(items[i].keys())[0]]
          player[6]-=i
  return player,items

def loss(player):
  if player[1]<1:
    print('You ran out of health.\n~~~~~~~~~~Game Over~~~~~~~~~~')
    return True
  else: return False

def win(final):
  if final[0]<1:
    print('You have defeated the final boss.\n~~~~~~~~~~You Win!~~~~~~~~~~')
    return True
  else: return False

def update(player,shopp,areas,select,coords,finalboss):
  print('You enter the room.')
  for i in range(select[1][coords[0]][coords[1]]['enemies']):
    print('There is an enemy!')
    player=combat(player)
    select[1][coords[0]][coords[1]]['enemies']-=1
  if loss(player):
    return player,shopp,areas,select,coords,finalboss,False
  if select[1][coords[0]][coords[1]]['boss']:
    print('There is an boss!')
    player,select[1][coords[0]][coords[1]]['boss']=bossCombat(player,select[1][coords[0]][coords[1]]['boss'],finalboss)
  if loss(player):
    return player,shopp,areas,select,coords,finalboss,False
  if win(finalboss):
    return player,shopp,areas,select,coords,finalboss,False
  if select[1][coords[0]][coords[1]]['shop']:
    player,shopp=shop(player,shopp)
  if select[1][coords[0]][coords[1]]['passage'] and input(f'Would you like to travel to area {select[1][coords[0]][coords[1]]["passage"][0]}?(y to travel, anything else to not)').lower()=='y':
    select,coords,areas=transport(select[1][coords[0]][coords[1]]['passage'],select,areas) 
    return player,shopp,areas,select,coords,finalboss,1
  displayMap(select,coords)
  coords=move(coords)
  return player,shopp,areas,select,coords,finalboss,1

tutorial()
while True:
  areas=base[0]
  items=base[1]
  player=creation()
  loc=[1,base[0][0][0]]
  coords=[0,0]
  while True:
    lst=update(player,items,areas,loc,coords,base[-1])
    if lst[-1]!= 1:
      break
    player=lst[0]
    items=lst[1]
    areas=lst[2]
    loc=lst[3]
    coords=lst[4]
  play=input('Would you like to play again?(y for yes, anything else to exit.)')
  if play!='y':
    break