import random, string

source=['This is a sentence.','A word is a basic element of language that carries meaning, can be used on its own, and is uninterruptible.', 'Despite the fact that language speakers often have an intuitive grasp of what a word is, there is no consensus among linguists on its definition and numerous attempts to find specific criteria of the concept remain controversial.', 'Different standards have been proposed, depending on the theoretical background and descriptive context; these do not converge on a single definition.','Some specific definitions of the term "word" are employed to convey its different meanings at different levels of description, for example based on phonological, grammatical or orthographic basis.', 'Others suggest that the concept is simply a convention used in everyday situations.']
data={}
starters=[]
sentence=[]
index=-1
for i in source:
    translator = str.maketrans('', '', (string.punctuation+'0123456789'))
    x=i.translate(translator)
    words=x.split(' ')
    for v in words:
        if index!=-1:
            data.update({words[index]:v})
            index+=1
        else:
            starters.append(v)
            index+=1
    index=-1
    data.update({words[-1]:'.'})
print(data)
print(starters)

sentence.append(random.choice(starters))
while sentence[-1]!='.':
    pass
print(sentence)