#LM 2nd Idiot Proof
name=input('What is your name?').strip().title()

good=False
while not good:
    phone=input('What is your phone number?').strip()
    phone=phone.replace(' ','')
    if len(phone) == 10:
        try:
            int(phone)
        except:
            good='NO'
        if good != 'NO':
            good=True
    phone=phone[0:3]+' '+phone[3:6]+' '+phone[6:10]

good=False
while not good:
    GPA=input('What is your GPA?').strip()
    try:
        float(GPA)
    except:
        good='NO'
    if good!='NO':
        if float(GPA)<=4.0 and float(GPA)>=0.0:
            good=True
            GPA=round(float(GPA),1)
    else:
        good=False

print('\nname:',name,'\n\nphone:',phone,'\n\nGPA:',GPA)