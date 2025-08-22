#LM 2nd Who are you?
names,age,color=[[],[],[]]
name=''
while name!="quit": #do not use this code if your name is quit
    name=input("What is your name?")
    if name in names:
        print("You are",names[names.index(name)]+", your favorite color is",color[names.index(name)]+", and you are",age[names.index(name)],"years old.")
    else:
        names.append(name)
        age.append(input("How old are you?"))
        color.append(input("What is your favorite color?"))
        print("You are",names[-1],"your favorite color is",color[-1],"and you are",age[-1],"years old.")