import turtle
import random

win = turtle.Screen()
win.title("Car Race")
win.bgcolor("white")

t1 = turtle.Turtle()
t2 = turtle.Turtle()

for t in (t1, t2):
    t.shape("turtle")
    t.penup()

t1.goto(-100, 0)
t2.goto(-100, -30)

for i in range(100):
    t1.forward(random.randint(1, 5))
    t2.forward(random.randint(1, 5))

win.mainloop()
