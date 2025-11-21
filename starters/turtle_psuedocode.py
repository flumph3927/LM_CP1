#LM 2nd Turtle Psuedocode Starter
import turtle
def drawBranch(ln):
    if ln>5:
        for i in range(3):
            turtle.forward(ln)
            drawBranch(ln/3)
            turtle.backward(ln)
            turtle.rt(60)

turtle.speed(0)
turtle.color('blue')
turtle.penup()
turtle.goto(0,0)
turtle.pendown()

for i in range(6):
    drawBranch(100)
    turtle.rt(60)

turtle.ht()
turtle.done()