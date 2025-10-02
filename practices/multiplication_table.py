#LM 2nd Multiplication Table

for i in range(1,13):
    for x in range(1,13):
        dgts=len(str(i*x))
        print(i*x,' '*(3-dgts),end='')
    print()