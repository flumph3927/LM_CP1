import random, string

#source=['This is a sentence.','Hey.','Oh hey, I didn’t see you there.','Did you already get a table?','Yeah, right over here.','I’m glad we had time to meet up.','Me too.','So, what’s going on?','Oh, not much.','You?','Not much.','Hey, how did your interview go?','Wasn’t that today?','Oh, yeah.','I think it went well.','I don’t know if I got the job yet, but they said they would call in a few days.','Well, I’m sure you did great.','Good luck.','Thanks.','I’m just happy that it’s over. I was really nervous about it.','I can understand that.','I get nervous before interviews, too.','Well, thanks for being supportive.', 'I appreciate it.','Sure, no problem.','A word is a basic element of language that carries meaning, can be used on its own, and is uninterruptible.', 'Despite the fact that language speakers often have an intuitive grasp of what a word is, there is no consensus among linguists on its definition and numerous attempts to find specific criteria of the concept remain controversial.', 'Different standards have been proposed, depending on the theoretical background and descriptive context; these do not converge on a single definition.','Some specific definitions of the term "word" are employed to convey its different meanings at different levels of description, for example based on phonological, grammatical or orthographic basis.', 'Others suggest that the concept is simply a convention used in everyday situations.', 'Philosophy is a systematic study of general and fundamental questions concerning topics like existence, reason, knowledge, value, beauty, mind, and language.', 'It is a rational and critical inquiry that reflects on its methods and assumptions.','Historically, many of the individual sciences, such as physics and psychology, formed part of philosophy.', 'However, they are considered separate academic disciplines in the modern sense of the term.', 'Influential traditions in the history of philosophy include Western, ArabicPersian, Indian, and Chinese philosophy.', 'Western philosophy originated in Ancient Greece and covers a wide area of philosophical subfields.', 'A central topic in ArabicPersian philosophy is the relation between reason and revelation.', 'Indian philosophy combines the spiritual problem of how to reach enlightenment with the exploration of the nature of reality and the ways of arriving at knowledge.', 'Chinese philosophy focuses principally on practical issues about right social conduct, government, and self-cultivation.',
source=['Never let your sense of morals prevent you from doing what is right.','The unexamined life is not worth living','He who thinks great thoughts, often makes great errors','Even while they teach, men learn','We are what we repeatedly do.', 'Excellence, then, is not an act, but a habit','Life must be understood backward', 'But it must be lived forward','You can discover more about a person in an hour of play than in a year of conversation','It is one thing to show a man that he is in error, and another to put him in possession of truth','The only thing I know is that I know nothing','The secret of happiness, you see is not found in seeking more, but in developing the capacity to enjoy less.','When it is obvious that goals can’t be reached, don’t adjust the goals, but adjust the action steps.','It is what you read when you don’t have to that determines what you will be when you can’t help it','No amount of anxiety makes any difference to anything that is going to happen','Prejudices are what fools use for reason','Happiness depends upon ourselves','We do not describe the world we see.','We see the world we can describe','What did you do as a child that made the hours pass like minutes','Herein lies the key to your earthly pursuits','What labels me, negates me.','It is not true that people stop pursuing dreams because they grow old, they grow old because they stop pursuing dreams','The menu is not the meal','Out of suffering have emerged the strongest souls; the most massive characters are seared with scars','Anybody can become angry - that is easy, but to be angry with the right person and to the right degree and at the right time and for the right purpose, and in the right way - that is not within everybodys power and is not easy.','You dont develop courage by being happy in your relationships everyday.', 'You develop it by surviving difficult times and challenging adversity.','There is nothing permanent except change.','By all means, get married: if you find a good wife, youll be happy; if not, youll become a philosopher.','Death does not concern us, because as long as we exist, death is not here.', 'And when it does come, we no longer exist.','Youll come to learn a great deal if you study the Insignificant in depth.']
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