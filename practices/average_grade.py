#LM 2nd Average Grade
grades=[]
total=0
classes=int(input("How many classes do you have?\n"))
for i in range(classes):
    grades.append(float(input("What is your grade in your period "+str(i+1)+" class.\n")))
for x in grades:
    total+=x
avg_grade=(total/len(grades))
print("Your average grade is",str(round(avg_grade,2))+"%!")