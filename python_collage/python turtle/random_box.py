
import turtle as t
import random

tim = t.Turtle() 
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]

for _ in range (300): # set it 300 times to draw
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))#randomly to choose a random directions.

tim.pensize(100)
tim.speed("fastest")