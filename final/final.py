#LM 2nd Final Project
import random

base=[[[[[{'enemies':0,'shop':0,'boss':'','passage':[]},{'enemies':0,'shop':0,'boss':'','passage':[]}],
         [{'enemies':0,'shop':0,'boss':'','passage':[]},{'enemies':0,'shop':0,'boss':'','passage':[2,[0,0],1]}]],

        [[{'enemies':0,'shop':0,'boss':'','passage':[1,[1,1],2]},{'enemies':0,'shop':0,'boss':'','passage':[3,[0,0],2]}],
         [{'enemies':0,'shop':0,'boss':'','passage':[4,[0,1],2]},{'enemies':0,'shop':1,'boss':'','passage':[]}]],

        [[{'enemies':1,'shop':0,'boss':'','passage':[2,[0,1],3]},{'enemies':2,'shop':0,'boss':'','passage':[7,[1,0],3]}],
         [{'enemies':1,'shop':0,'boss':'','passage':[5,[0,1],3]},{'enemies':0,'shop':0,'boss':[24,[4,8]],'passage':[6,[0,1],3]}]]],

        [[[{'enemies':1,'shop':0,'boss':'','passage':[7,[0,0],4]},{'enemies':0,'shop':0,'boss':'','passage':[2,[1,0],4]}],
          [{'enemies':2,'shop':0,'boss':'','passage':[9,[0,0],4]},{'enemies':2,'shop':0,'boss':'','passage':[8,[0,0],4]}]],

         [[{'enemies':3,'shop':0,'boss':'','passage':[]},{'enemies':2,'shop':0,'boss':'','passage':[3,[1,0],5]}],
          [{'enemies':2,'shop':0,'boss':'','passage':[7,[0,1],5]},{'enemies':2,'shop':0,'boss':'','passage':[6,[1,0],5]}]],

         [[{'enemies':1,'shop':0,'boss':'','passage':[]},{'enemies':2,'shop':0,'boss':'','passage':[3,[1,1],6]}],
          [{'enemies':2,'shop':0,'boss':'','passage':[5,[1,1],6]},{'enemies':3,'shop':0,'boss':'','passage':[]}]]],

         [[[{'enemies':3,'shop':0,'boss':'','passage':[4,[0,0],7]},{'enemies':2,'shop':0,'boss':'','passage':[5,[1,0],7]}],
           [{'enemies':2,'shop':0,'boss':'','passage':[3,[1,0],7]},{'enemies':0,'shop':0,'boss':[36,[5,9]],'passage':[]}]],

          [[{'enemies':random.randint(2,4),'shop':0,'boss':'','passage':[4,[1,1],8]},{'enemies':0,'shop':0,'boss':[36,[5,9]] if random.randint(0,1) else '','passage':[]}],
           [{'enemies':random.randint(1,6),'shop':0,'boss':'','passage':[]},{'enemies':random.randint(1,5),'shop':0,'boss':'','passage':[9,[1,0],8]}]],

          [[{'enemies':1,'shop':0,'boss':'','passage':[4,[1,0],9]},{'enemies':1,'shop':0,'boss':'','passage':[]}],
           [{'enemies':1,'shop':0,'boss':'','passage':[8,[1,1],9]},{'enemies':1,'shop':0,'boss':[48,[6,10]],'passage':[]}]]]],
           {10:{'Daggers':[8,'spd']},10:{'Greatsword':[8,'str']},10:{'spell':[8,'mag']}},[48,[6,10]]]

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
    return [random.randint(5,15)+str+spd, random.randint(5,15)+str+spd, (random.randint(5,15)+str+spd)/4, str, spd, mag, 0, {'base attack':[6,str]}]

def display_map(area, coord):
  out=''
  for x in area:
    for i in x:
      end=''
      if i==area[coord[0],coord[1]]:
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
  print('Area grid:\n1 2 3')