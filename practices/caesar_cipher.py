#LM 2nd Caesar Cipher
import string
def encode(shift, message):
    code=''
    for i in message:
        if i in string.ascii_uppercase:
            place=string.ascii_uppercase.index(i)
            if place+shift>=26:
                code += string.ascii_uppercase[place+shift-26]
            
        if i in string.ascii_lowercase:
            place=string.ascii_lowercase.index(i)
            if place+shift>=26:
                code += string.ascii_lowercase[place+shift-26]
        else:
            code += i
    return code