#LM 2nd Maze Generator
'''
make function that generates 8 by 8 grid of 1 and 0, edges all 1
make function to draw square with turtle, but end one side from start
make function to set up turtle, draw rows out of squares with fill depending on generated map, draw rows in correct alignment
make function to check map:
    set POSS and DONE to empty lists
    add start square to POSS
    loop while POSS not empty:
        set SELECT to square in POSS
        if select is end square, return true
        check all areas surrounding SELECT for empty squares
        add coordinates of all empty squares to POSS
        add SELECT to DONE
        remove SELECT from POSS
    if POSS empty, return false
'''
import turtle,random
def generate_map():
    mapp=[[2,0,2,2,2,2,2,2,2,2],[],[],[],[],[],[],[],[],[2,2,2,2,2,2,2,2,0,2]]
    for i in mapp:
        if mapp.index(i)!=0 and mapp.index(i)!=9:
            i.append(2)
            for x in range(8):
                i.append(random.randint(0,2))
            i.append(2)
    return mapp
def square(trtl):
    for i in range(4):
        trtl.lt(90)
        trtl.forward(20)
    trtl.forward(20)
def display(mapp):
    t=turtle.Turtle()
    t.speed(0.01)
    t.pensize(0)
    t.penup()
    for i in mapp:
        for x in i:
            if x==2:
                t.begin_fill()
                square(t)
                t.end_fill()
            else:
                square(t)
        t.rt(180)
        t.forward(220)
        for i in range(2):
            t.lt(90)
            t.forward(20)
    turtle.done()
def check(mapp):
    ps=[]
    dne=[]
    ps+=[7,6]
    while ps:
        slct=random.choice(ps)
        if slct==[0,1]:
            return True
        
display(generate_map())