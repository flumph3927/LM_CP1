import random, string

source=['This is a sentence.','A word is a basic element of language that carries meaning, can be used on its own, and is uninterruptible.', 'Despite the fact that language speakers often have an intuitive grasp of what a word is, there is no consensus among linguists on its definition and numerous attempts to find specific criteria of the concept remain controversial.', 'Different standards have been proposed, depending on the theoretical background and descriptive context; these do not converge on a single definition.','Some specific definitions of the term "word" are employed to convey its different meanings at different levels of description, for example based on phonological, grammatical or orthographic basis.', 'Others suggest that the concept is simply a convention used in everyday situations.', 'Philosophy is a systematic study of general and fundamental questions concerning topics like existence, reason, knowledge, value, beauty, mind, and language.', 'It is a rational and critical inquiry that reflects on its methods and assumptions.','Historically, many of the individual sciences, such as physics and psychology, formed part of philosophy.', 'However, they are considered separate academic disciplines in the modern sense of the term.', 'Influential traditions in the history of philosophy include Western, ArabicPersian, Indian, and Chinese philosophy.', 'Western philosophy originated in Ancient Greece and covers a wide area of philosophical subfields.', 'A central topic in ArabicPersian philosophy is the relation between reason and revelation.', 'Indian philosophy combines the spiritual problem of how to reach enlightenment with the exploration of the nature of reality and the ways of arriving at knowledge.', 'Chinese philosophy focuses principally on practical issues about right social conduct, government, and self-cultivation.','Never let your sense of morals prevent you from doing what is right.','The unexamined life is not worth living','He who thinks great thoughts, often makes great errors','Even while they teach, men learn','We are what we repeatedly do. Excellence, then, is not an act, but a habit','Life must be understood backward', 'But it must be lived forward','You can discover more about a person in an hour of play than in a year of conversation','It is one thing to show a man that he is in error, and another to put him in possession of truth','The only thing I know is that I know nothing','The secret of happiness, you see is not found in seeking more, but in developing the capacity to enjoy less.','When it is obvious that goals can’t be reached, don’t adjust the goals, but adjust the action steps.','It is what you read when you don’t have to that determines what you will be when you can’t help it','No amount of anxiety makes any difference to anything that is going to happen','Prejudices are what fools use for reason','Happiness depends upon ourselves','We do not describe the world we see.','We see the world we can describe','What did you do as a child that made the hours pass like minutes','Herein lies the key to your earthly pursuits','What labels me, negates me.','It is not true that people stop pursuing dreams because they grow old, they grow old because they stop pursuing dreams','The menu is not the meal','Out of suffering have emerged the strongest souls; the most massive characters are seared with scars',]
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