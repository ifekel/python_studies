
from turtle import*
import colorsys

bgcolor("black")
hue = 0.0
hideturtle()
pensize(100)
speed(100)

for i in range(300):
    col = colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(col)
    hue += 0.50
    fd(i)
    rt(60+10+10)
    lt(56)
    circle(10)
done()


