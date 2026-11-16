import turtle
import math

screen = turtle.Screen()
screen.setup(900, 520)
screen.bgcolor("#dde8f2")
screen.title("BMW M4 - Turtle")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

BODY = "#1c4fa8"      # Interlagos-style blue
GROUND_Y = -122
WHEEL_Y = -80
WHEELS_X = (-170, 175)


def poly(pts, fill, outline="black", w=2):
    t.penup()
    t.goto(pts[0])
    t.pendown()
    t.color(outline, fill)
    t.pensize(w)
    t.begin_fill()
    for p in pts[1:]:
        t.goto(p)
    t.goto(pts[0])
    t.end_fill()
    t.penup()


def circ(x, y, r, fill, outline="black", w=2):
    t.penup()
    t.goto(x, y - r)
    t.setheading(0)
    t.color(outline, fill)
    t.pensize(w)
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()


def line(a, b, color="black", w=2):
    t.penup()
    t.goto(a)
    t.color(color)
    t.pensize(w)
    t.pendown()
    t.goto(b)
    t.penup()


# ---------- body ----------
poly([(-295, -65), (-295, -25), (-282, 2), (-210, 18), (-150, 28),
      (-110, 68), (-40, 88), (40, 84), (105, 48), (112, 30),
      (200, 20), (270, 8), (298, -12), (300, -60), (285, -68)], BODY)

# lower black skirt / diffuser
poly([(-290, -65), (285, -65), (285, -68), (-290, -68)], "#111", "#111", 1)
line((-130, -58), (120, -58), "#111", 4)

# windows
poly([(-135, 32), (-105, 64), (-40, 80), (32, 77), (88, 43), (80, 32)],
     "#9fc3d9")
line((-5, 80), (0, 32), BODY, 8)           # B-pillar
line((-5, 80), (0, 32), "black", 1)

# door cut lines + handle
line((-5, 32), (-8, -56), "black", 2)
line((-135, 32), (-140, -50), "black", 2)
line((-60, 14), (-35, 14), "#0d2a5c", 4)
line((30, 14), (55, 14), "#0d2a5c", 4)

# character line
line((-250, 0), (270, 3), "#12388a", 2)

# side mirror
poly([(70, 52), (95, 55), (98, 45), (75, 42)], BODY)

# headlight
poly([(250, 14), (292, 2), (297, -8), (258, -3)], "#fff6c8")
line((262, 6), (288, -1), "#f4b400", 2)

# front air intake
poly([(272, -30), (298, -28), (298, -52), (278, -52)], "#111", "#111", 1)

# tail light
poly([(-295, -12), (-284, 2), (-262, 6), (-268, -8)], "#d40000")

# M stripes on fender
line((168, 10), (178, -15), "#6fc3f2", 4)
line((178, 10), (188, -15), "#1b2a8a", 4)
line((188, 10), (198, -15), "#d40000", 4)

# exhaust tips
poly([(-300, -48), (-280, -48), (-280, -58), (-300, -58)], "#888")

# ---------- wheel arches ----------
for x in WHEELS_X:
    circ(x, WHEEL_Y, 47, "#111", "#111", 1)

# ---------- ground ----------
poly([(-450, GROUND_Y), (450, GROUND_Y), (450, -260), (-450, -260)],
     "#555", "#555", 1)
line((-450, GROUND_Y), (450, GROUND_Y), "#333", 3)
for x in range(-420, 450, 120):
    line((x, -190), (x + 60, -190), "#ddd", 4)   # road dashes

# shadow
poly([(-285, GROUND_Y - 4), (290, GROUND_Y - 4), (270, GROUND_Y - 12),
      (-265, GROUND_Y - 12)], "#333", "#333", 1)

# ---------- wheels ----------
for x in WHEELS_X:
    circ(x, WHEEL_Y, 42, "#1a1a1a", "black", 2)          # tire
    circ(x, WHEEL_Y, 28, "#c9ced4", "#777", 2)           # rim
    for i in range(10):                                   # spokes
        a = math.radians(i * 36)
        line((x + 7 * math.cos(a), WHEEL_Y + 7 * math.sin(a)),
             (x + 26 * math.cos(a), WHEEL_Y + 26 * math.sin(a)),
             "#8a9099", 3)
    poly([(x + 14, WHEEL_Y + 18), (x + 26, WHEEL_Y + 8),
          (x + 28, WHEEL_Y + 2), (x + 16, WHEEL_Y + 10)],
         "#d40000", "#d40000", 1)                         # caliper
    circ(x, WHEEL_Y, 7, "#333", "black", 1)               # hub

# ---------- text ----------
t.goto(0, 150)
t.color("#12388a")
t.write("BMW M4", align="center", font=("Arial", 28, "bold"))

screen.update()
turtle.done()