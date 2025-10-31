#LM 2nd Maze Generator
'''
make function that generates 6 by 6 grid of 1 and 0 
make function to draw square with turtle, but end one side from start
'''
import turtle,random
def generate_map():
    mapp=[[],[],[],[],[],[]]
    for i in mapp:
        for x in range(6):
            i.append(random.randint(0,1))
    return mapp
def square(trtl):
    for i in range(4):
        trtl.forward(20)
        trtl.lt(90)
    trtl.lt(180)
    trtl.forward(20)
def display(mapp):
    t=turtle.Turtle()
    t.size=0
    t.pensize(0)
    for i in mapp:
        for x in i:
            if x==1:
                t.begin_fill()
                square(t)
                t.end_fill()
            else:
                square(t)
        t.rt(90)
        t.forward(20)
    t.done()
display(generate_map())