#LM 2nd Caesar Cipher
'''
create function encode, get MESSAGE and SHIFT
    set CODE to empty string
    loop through characters in MESSAGE
        if it is an uppercase letter
            shift character through list of uppercase letters and add new character to CODE
        if it is an lowercase letter
            shift character through list of lowercase letters and add new character to CODE
        else
            add character to end of CODE
    return CODE
create function decode, get CODE and SHIFT
    set MESSAGE to empty string
    loop through characters in CODE
        if it is an uppercase letter
            shift character through list of uppercase letters and add new character to MESSAGE
        if it is an lowercase letter
            shift character through list of lowercase letters and add new character to MESSAGE
        else
            add character to end of MESSAGE
    return MESSAGE
set INPUT to user input in response to message to encode or decode?
if user wants to encode
    set SHIFT to user input
    call encode on INPUT and SHIFT
else if user wants to decode
    set SHIFT to user input
    call decode on INPUT and SHIFT
'''
import string
def encode(shift, message):
    code=''
    for i in message:
        if i in string.ascii_uppercase:
            place=string.ascii_uppercase.index(i)
            if place+shift>=26:
                code += string.ascii_uppercase[place+shift-26]
            else:
                code += string.ascii_uppercase[place+shift]
        elif i in string.ascii_lowercase:
            place=string.ascii_lowercase.index(i)
            if place+shift>=26:
                code += string.ascii_lowercase[place+shift-26]
            else:
                code += string.ascii_lowercase[place+shift]
        else:
            code += i
    return code
def decode(shift,code):
    message=''
    for i in code:
        if i in string.ascii_uppercase:
            place=string.ascii_uppercase.index(i)
            if place-shift<0:
                message += string.ascii_uppercase[place-shift+26]
            else:
                message += string.ascii_uppercase[place-shift]
        elif i in string.ascii_lowercase:
            place=string.ascii_lowercase.index(i)
            if place-shift<0:
                message += string.ascii_lowercase[place-shift+26]
            else:
                message += string.ascii_lowercase[place-shift]
        else:
            message += i
    return message
user=input('What message would you like to encode/decode? ')
if input('Enter e to encode, any other key to decode ')=='e':
    shift=int(input('How far to shift your message? '))
    print(f'Your encoded message is {encode(shift,user)}')
else:
    shift=int(input('What is your code\'s shift? '))
    print(f'Your decoded message is {decode(shift,user)}')