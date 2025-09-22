import random, string

base=['Write a program that asks a user for their username and their. If the username and the password match the ones given in the program it welcomes the user to the program. Otherwise it tells the user that their login credentials were invalid.','Have a selection of several different users with different passwords. Check to see if the username is one of the options, then check to see if the password matches for that given user. (I recommend using a list of users with the username and password set up as their own list)']
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