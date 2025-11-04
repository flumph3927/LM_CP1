#LM 2nd Maze Generator
'''
make function that generates 20 by 20 grid of 1 and 0, edges all 1
make function to draw square with turtle, but end one side from start
make function to set up turtle, draw rows out of squares with fill depending on generated map, draw rows in correct alignment
make function to check map:
    set DONE to empty lists
    set POSS to list with start square
    loop while POSS not empty:
        set SELECT to square in POSS
        if select is end square, return true
        check all areas surrounding SELECT for empty squares
        add coordinates of all empty squares to POSS
        add SELECT to DONE
        remove all in DONE from POSS
    if POSS empty, return false
set MP to function generate grid
loop while mp is unsolvable, using function check map
    set MP to function generate grid
display map using function
'''
import turtle,random
#make function that generates 20 by 20 grid of 1 and 0, edges all 1
def generateMap():
    mapp=[[2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2]]#make base grid
    for i in mapp:
        if mapp.index(i)!=0 and mapp.index(i)!=19:# loop through grid and add random objects, also edges
            i.append(2)
            for x in range(18):
                i.append(random.randint(0,2))
            i.append(2)
    return mapp
#make function to draw square with turtle, but end one side from start
def square(trtl):
    for i in range(4):
        trtl.lt(90)
        trtl.forward(20)
    trtl.forward(20)
#make function to set up turtle, draw rows out of squares with fill depending on generated map, draw rows in correct alignment
def display(mapp):
    t=turtle.Turtle()# setup turtle
    t.speed(0)
    t.pensize(0)
    t.penup()
    for i in mapp:# loop through map
        for x in i:
            if x==2:
                t.begin_fill()#draw solid square
                square(t)
                t.end_fill()
            else:
                square(t)#draw empty square
        t.rt(180)
        t.forward(420) # move to new line
        for i in range(2):
            t.lt(90)
            t.forward(20)
    turtle.done()
#make function to check map:
def check(mapp):
    ps=[[19,18]] #    set DONE to empty lists  set POSS to list with start square
    dne=[]
    while ps:#loop while POSS not empty:
        slct=random.choice(ps)#set SELECT to square in POSS
        if slct==[0,1]:#if select is end square, return true
            return True
        for i in [[slct[0]+1,slct[1]],[slct[0]-1,slct[1]],[slct[0],slct[1]-1],[slct[0],slct[1]+1]]:#check all areas surrounding SELECT for empty squares
            if i[0]>-1 and i[0]<20 and i[1]>-1 and i[1]<20 and mapp[i[0]][i[1]]!=2:
                ps.append(i)#add coordinates of all empty squares to POSS
        dne.append(slct)#add SELECT to DONE
        for i in dne:
            if i in ps:#remove all in DONE from POSS
                ps.remove(i)
mp=generateMap()#set MP to function generate grid
while not check(mp):#loop while mp is unsolvable, using function check map
    mp=generateMap()#set MP to function generate grid
display(mp)#display map using function