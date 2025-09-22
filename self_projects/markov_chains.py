import random, string

base=[]
source=[]
data=[]
starters=[]
sentence=[]
poss=[]
for p in base:
    bases=p.split('.')
    for h in bases:
        source.append(h.strip())
for m in source:
    if m.strip()=='':
        source.remove(m)

index=-1
for i in source:
    translator = str.maketrans('', '', (string.punctuation+'0123456789'))
    x=i.translate(translator)
    words=x.split(' ')
    starters.append(words[0])
    for v in words:
        data.append(v)
    data.append('.')
    index=-1

for j in data:
    if j.strip=='':
        data.remove(j)

sentence.append(random.choice(starters))
while sentence[-1]!='.':
    poss=[]
    count=1
    for a in data:
        if a==sentence[-1]:
            if a!=data[-1] and a!= data[-2]:
                poss.append(data[count])
        count+=1
    if poss!=[]:
        sentence.append(random.choice(poss))
    else:
        sentence.append('.')
out=''
for i in sentence:
    if i != '.':
        out=out +' '+i
    else:
        out=out+i
print('sentence:',out)