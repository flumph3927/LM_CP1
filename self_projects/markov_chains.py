import random, string

source=['This is a sentence.','A word is a basic element of language that carries meaning, can be used on its own, and is uninterruptible.', 'Despite the fact that language speakers often have an intuitive grasp of what a word is, there is no consensus among linguists on its definition and numerous attempts to find specific criteria of the concept remain controversial.', 'Different standards have been proposed, depending on the theoretical background and descriptive context; these do not converge on a single definition.','Some specific definitions of the term "word" are employed to convey its different meanings at different levels of description, for example based on phonological, grammatical or orthographic basis.', 'Others suggest that the concept is simply a convention used in everyday situations.','the word this means this thing.','The Saturn V[f] is a retired American super heavy-lift launch vehicle developed by NASA under the Apollo program for human exploration of the Moon.', 'The rocket was human-rated, had three stages, and was powered by liquid fuel.', 'Flown from 1967 to 1973, it was used for nine crewed flights to the Moon and to launch Skylab, the first American space station.'As of 2025, the Saturn V remains the only launch vehicle to have carried humans beyond low Earth orbit (LEO). The Saturn V holds the record for the largest payload capacity to low Earth orbit, 140,000 kg (310,000 lb), which included unburned propellant needed to send the Apollo command and service module and Lunar Module to the Moon.

The largest production model of the Saturn family of rockets, the Saturn V was designed under the direction of Wernher von Braun at the Marshall Space Flight Center in Huntsville, Alabama; the lead contractors for construction of the rocket were Boeing, North American Aviation, Douglas Aircraft Company, and IBM. Fifteen flight-capable vehicles were built, not counting three used for ground testing. A total of thirteen missions were launched from Kennedy Space Center, nine of which carried 24 astronauts to the Moon from Apollo 8 to Apollo 17.']
data=[]
starters=[]
sentence=[]
poss=[]
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
print(data)
print(starters)

sentence.append(random.choice(starters))
while sentence[-1]!='.':
    poss=[]
    count=1
    for a in data:
        if a==sentence[-1]:
            if a!=data[-1] and a!= data[-2]:
                poss.append(data[count])
                print(count)
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