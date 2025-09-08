#LM 2nd Basic Calculator
run=True
while run:
    good = True
    x=input("Enter your first number.")
    y=input("Enter your second number.")
    try:
        float(x)
        float(y)
    except:
        good=False
        print("That isn't a number. Don't be stupid.")
    if good:
        x=float(x)
        y=float(y)
        eq=input("What equation would you like to run?(+,-,*,/,//,%,**)(q to quit)")
        if eq=='+':
            print(f"{x} + {y} = {x+y}")
        elif eq=='-':
            print(f"{x} - {y} = {x-y}")
        elif eq=='*':
            print(f"{x} * {y} = {x*y}")
        elif eq=='/':
            print(f"{x} / {y} = {x/y}")
        elif eq=='//':
            print(f"{x} // {y} = {x//y}")
        elif eq=='%':
            print(f"{x} % {y} = {x%y}")
        elif eq=='**':
            print(f"{x} ** {y} = {x**y}")
        elif eq=='q':
            run=False
        else:
            print("You did not enter one of the options. You will have to re-enter your numbers. Don't be stupid.")