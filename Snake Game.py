import turtle
import time
import random

delay = 0.1
score = 0

# Set up screen
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Movement
def go_up(): head.direction = "up"
def go_down(): head.direction = "down"
def go_left(): head.direction = "left"
def go_right(): head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor() + 20
        head.sety(y)
    if head.direction == "down":
        y = head.ycor() - 20
        head.sety(y)
    if head.direction == "left":
        x = head.xcor() - 20
        head.setx(x)
    if head.direction == "right":
        x = head.xcor() + 20
        head.setx(x)

win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

# Game loop
while True:
    win.update()
    move()

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add new segment
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("grey")
        new_seg.penup()
        segments.append(new_seg)

    # Move body
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    # Check wall collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        break

    # Check self-collision
    for segment in segments:
        if segment.distance(head) < 20:
            break

    time.sleep(delay)

win.bye()
