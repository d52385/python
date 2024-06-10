import math
import turtle 

turtle.bgcolor("black")
turtle.speed(0)
turtle.goto(0, -13)
turtle.pendown()

h = 0
phi = 137.508 * (math.pi / 180.0)

for i in range(5):
    for j in range(9):
        turtle.color('#01FFC3')
        h += 5
        turtle.circle(250 - j * 8,80)
        turtle.left(90)
        turtle.circle(250 - j * 8,80)
        turtle.left(180)
turtle.color('#9D72FF')

turtle.goto(-40, -13)
x=1
while x<200:
    turtle.forward(5+x)
    turtle.right(91)
    x+=1
turtle.mainloop()
