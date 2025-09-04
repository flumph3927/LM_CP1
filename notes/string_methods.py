#LM 2nd String Methods Notes

name='the quick brown fox jumps over the lazy dog'
a='fox'
print(name[name.find(a):name.find(a)+len(a)])


#strip() removes leading and trailing spaces
#lower() and upper() decapitalize or capitalize all letters, respectively
#capitalize() capitalizes the first character of the string
#title() capitalizes the first letter and every letter after a space
#find() finds the first occurrence of a value and returns the index of said value
#replace(x,y) replaces a given x in the string with y
#format() allows you to replace curly brackets in the string with other strings or variables(other functions too)(technically outdated)
#Use f before the string, it does the same thing.

#len() gets the length of the string, but is not a string method
#Use [x:y] to get part of the string from indexes x through y
print((2**15)*50)