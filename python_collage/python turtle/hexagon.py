import turtle
turtle.pensize(5)
turtle.pencolor('aqua')
for j in range(1,9):
    turtle.forward(100)
    turtle.right(45)

for i in range(1,9):
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.circle(80)
    turtle.pencolor("blue")
    turtle.circle(60)
    turtle.penup()
    turtle.right(45)


turtle.done()
