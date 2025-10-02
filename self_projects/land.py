import random
sze=60
mp=[]
for i in range(sze):
    mp.append([])
    for x in range(sze):
        mp[i].append('')
dne=False
while not dne:
    tle=[random.randint(0,(sze-1)),random.randint(0,(sze-1))]
    if mp[tle[0]][tle[1]]=='':
        ps=['~','-','~','~','~','-','^','+','+']
        for j in [[tle[0],tle[1]+1],[tle[0]-1,tle[1]],[tle[0]+1,tle[1]],[tle[0],tle[1]-1]]:
            if j[0]<(sze-1) and j[0]>-1 and j[1]>-1 and j[1]<(sze-1):
                if mp[j[0]][j[1]] != '':
                    for a in range(100):
                        ps.append(mp[j[0]][j[1]])
        mp[tle[0]][tle[1]]=random.choice(ps)
    dne=True
    for i in mp:
        for x in i:
            if x == '':
                dne=False
cds={'~':'\033[104m','-':'\033[43m','^':'\033[1m\033[47m','+':'\033[102m'}
for i in mp:
    for x in i:
        print(cds[x]+'',x,'\033[00m',end='')
    print()