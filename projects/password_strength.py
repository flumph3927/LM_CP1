#LM 2nd Password strength checker
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
    if character in password is in !@#$%^&*()_+-=[]{}|;:,.<>?
        add one to score
        end loop
if SCORE is 5, display Very Strong Password
else if SCORE is 4, display Strong Password
else if SCORE is 3, display Weak Password
else if SCORE is 0, display This actually might be good???
else display Very Weak Password
'''
word=input('Enter password')
score=0
if len(word)>7:
    score+=1
