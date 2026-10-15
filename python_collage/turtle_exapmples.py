import turtle
turtle.pensize(5)
turtle.pencolor('orange')
turtle.speed(10)
turtle.penup()
turtle.goto(-400,400)
turtle.pendown()
for i in range(0,10):
    for j in range(0,10):
        turtle.pendown()
        turtle.fillcolor('yellow')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(100)
    turtle.goto(-400, 400 - (100 * (i + 1)))
turtle.done()