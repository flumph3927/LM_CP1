#LM 2nd User Sign In
users=[['test','1234'],['me','thisisasentence'],['I','word']]
user=input('What is your username?')
word=input('What is your password?')
for i in users:
    if i[0]==user:
        if i[1]==word:
            valid=True
if valid:
    print('Welcome!')
else:
    print('Invalid login credentials.')