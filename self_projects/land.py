
import random
mp = [
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','','']
    ]
dne=False
while not dne:
    tle=[random.randint(0,8),random.randint(0,8)]
    if mp[tle[0]][tle[1]]=='':
        ps=['~','-']
        for j in [tle[0]-1,tle[0],tle[0]+1]:
            for k in [tle[1]-1,tle[1],tle[1]+1]:
                if j<9 and j>-1 and k>-1 and k<9:
                    if mp[j][k] != '':
                        ps.append(mp[j][k])
        mp[tle[0]][tle[1]]=random.choice(ps)
    dne=True
    for i in mp:
        for x in i:
            if x == '':
                dne=False
for i in mp:
    for x in i:
        print(x,end='')
    print()