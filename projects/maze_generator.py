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


#make function that generates 20 by 20 grid of 1 and 0, edges all 1 except entrance and exit
def generateMap():
    #make base grid
    mapp=[[2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2]]
    # loop through grid and add random objects, also edges
    for i in mapp:
        if mapp.index(i)!=0 and mapp.index(i)!=19:
            i.append(2)
            for x in range(18):
                i.append(random.randint(0,2))
            i.append(2)
    return mapp


#make function to check map:
def check(mapp):
    #    set DONE to empty lists  set POSS to list with start square
    ps=[[19,18]] 
    dne=[]
    #loop while POSS not empty:
    while ps:
        #set SELECT to square in POSS
        slct=random.choice(ps)
        #if select is end square, return true
        if slct==[0,1]:
            return True
        #check all areas surrounding SELECT for empty squares
        for i in [[slct[0]+1,slct[1]],[slct[0]-1,slct[1]],[slct[0],slct[1]-1],[slct[0],slct[1]+1]]:
            #add coordinates of all empty squares to POSS
            if i[0]>-1 and i[0]<20 and i[1]>-1 and i[1]<20 and mapp[i[0]][i[1]]!=2:
                ps.append(i)
        #add SELECT to DONE
        dne.append(slct)
        #remove all in DONE from POSS
        for i in dne:
            if i in ps:
                ps.remove(i)


#make function to draw square with turtle, but end one side from start
def square(trtl):
    for i in range(4):
        trtl.lt(90)
        trtl.forward(20)
    trtl.forward(20)

#make function to set up turtle, draw rows out of squares with fill depending on generated map, draw rows in correct alignment
def display(mapp):
    # setup turtle, 
    t=turtle.Turtle()
    turtle.tracer(0)
    t.penup()
    t.goto(-200,200)
    # loop through map
    for i in mapp:
        for x in i:
            if x==2:
                #draw solid square
                t.begin_fill()
                square(t)
                t.end_fill()
            else:
                #draw empty square
                square(t)
         # move to new line
        t.rt(180)
        t.forward(420)
        for i in range(2):
            t.lt(90)
            t.forward(20)
    turtle.update()
    turtle.done()


#set MP to function generate grid
mp=generateMap()
#loop while mp is unsolvable, using function check map
while not check(mp):
    #set MP to function generate grid
    mp=generateMap()
#display map using function
display(mp)