#LM 2nd What is my Grade

grades=[]
run=True
while run: #gets inputs
    grad=input('What is your percentage grade(q to stop entering grades)(do not include %)')
    try: #checks if valid input
        if grad=='q':
            bad=False
        else:
            float(grad)
            if float(grad) < 0 or float(grad) > 100:
                bad=True
            else:
                bad=False
    except:
        bad=True
    if bad:
        print('That is not a valid input.')
    else:
        print('That is a valid input')
    if not bad: #adds to list of grades or stops loop
        if grad != 'q':
            grades.append(grad)
        else:
            if len(grades) != 0:
                print('Your grades have been recorded')
                run=False
            else:
                print('You need to enter at least one grade.')

total=0
for i in grades:
    total += float(i)
avg=round(total/len(grades),2)

if avg >= 93:
    print(f'Your average grade is {avg}, which is an A.')
elif avg >= 90:
    print(f'Your average grade is {avg}, which is an A-.')
elif avg >= 87:
    print(f'Your average grade is {avg}, which is an B+.')
elif avg >= 84:
    print(f'Your average grade is {avg}, which is an B.')
elif avg >= 80:
    print(f'Your average grade is {avg}, which is an B-.')
elif avg >= 77:
    print(f'Your average grade is {avg}, which is an C+.')
elif avg >= 74:
    print(f'Your average grade is {avg}, which is an C.')
elif avg >= 70:
    print(f'Your average grade is {avg}, which is an C-.')
elif avg >= 65:
    print(f'Your average grade is {avg}, which is an D.')
elif avg >= 60:
    print(f'Your average grade is {avg}, which is an D-.')
else:
    print(f'Your average grade is {avg}, which is an F.')