#LM 2nd turtle race
'''
make function setup
    create turtles
    setup screen
    draw line on right side
    color turtles
    teleport turtles to a line on left side
    make turtles turtles
make function move
    loop through turtles
        find random amount
        move turtles amount
call setup
set WIN to False
loop if WIN is not true
    call move
    check if a turtle has won, set WIN to True
print the winner
'''
import turtle, random
def setup():
    blue=turtle.Turtle()
    green=turtle.Turtle()
    red=turtle.Turtle()
    yellow=turtle.Turtle()
    purple=turtle.Turtle()
    screen=turtle.Screen()
    screen.setup(600,400)
    screen.title('TURTLE RACE')
    blue.teleport(250,-200)
    blue.lt(90)
    blue.forward(400)
    blue.rt(90)
    blue.color('blue')
    red.color('red')
    green.color('green')
    yellow.color('yellow')
    purple.color('purple')
    blue.teleport(-250,130)
    red.teleport(-250,65)
    green.teleport(-250,0)
    yellow.teleport(-250,-65)
    purple.teleport(-250,-130)
    blue.shape('turtle')
    red.shape('turtle')
    green.shape('turtle')
    yellow.shape('turtle')
    purple.shape('turtle')
    return [blue,red,green,yellow,purple]
def move(tlist):
    for i in tlist:
        i.forward(random.randint(0,4))
    return tlist
def checkWin(tlist):
    for i in tlist:
        if i.pos()[0]>=256:
            return i.pencolor()
    return False
trtls=setup()
win=False
while win==False:
    trtls=move(trtls)
    win=checkWin(trtls)
print(f'The {win} turtle won!')
turtle.done()