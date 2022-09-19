from turtle import *
speed(0)
bgcolor('black')
color('red')
hideturtle()

n = 3
p = True

while True:
    circle(n)
    if p:
        n = n - 3
    else:
        n = n + 3
    if n == 0 or n == 150:
        p = not p
    left(1)

done()
