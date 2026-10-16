import random
import turtle as t

tim = t.Turtle()
screen = t.Screen()

tim.speed('fastest')
tim.pensize(8)

directions = [0,90,180,270]

colors = [
    'CornflowerBlue',
    'DarkOrchid',
    'Wheat',
    'Pink',
    'SeaGreen',
    'SlateGray',
    'DeepSkyBlue',
]

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(50)

    tim.setheading(random.choice(directions))

screen.exitonclick()