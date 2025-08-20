#LM 2nd Hello World

letters=['a','b','c','d','e']
name=input("What is your name? ")
if name=="Levi" or name=="Ms. LaRose":
    print("Hello, Admin",name)
elif name in letters:
    print("Welcome back, letter",name+'!')
else:
    print("Hello",name)