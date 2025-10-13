#LM 2nd Password Strength Checker
'''Psuedocode:
set PASSWORD to user input
set SCORE to 0
if length of password is 8 or larger, add 1 to SCORE
loop through characters in PASSWORD
    if character in password is in QWERTYUIOPASDFGHJKLZXCVBNM
        add one to score
        end loop
loop through characters in PASSWORD
    if character in password is in qwertyuiopasdfghjklzxcvbnm
        add one to score
        end loop
loop through characters in PASSWORD
    if character in password is in 1234567890
        add one to score
        end loop
loop through characters in PASSWORD
    if character in password is in !@#$%^&*()_+-=[]{}|;:,.<>?/\
        add one to score
        end loop
if SCORE is 5, display Very Strong Password
else if SCORE is 4, display Strong Password
else if SCORE is 3, display Weak Password
else display Very Weak Password
'''
word=input('Enter password: ')
score=0
if len(word)>7:
    score+=1
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        score+=1
        break
for i in word:
    if i in 'qwertyuiopasdfghjklzxcvbnm':
        score+=1
        break
for i in word:
    if i in '1234567890':
        score+=1
        break
for i in word:
    if i in '`~!@#$%^&*()_+-=[]{}|\\;:\'",.<>?/':
        score+=1
        break
if score==5:
    print('Very Strong Password')
elif score==4:
    print('Strong Password')
elif score==3:
    print('Weak Password')
else:
    print('Very Weak Password')