from turtle import *
import turtle
import random
from random import randrange
from freegames import square, vector

coloursb = ["navy", "purple", "blue", "darkgreen", "chocolate"]
coloursf = ["gold", "orange", "skyblue", "yellow", "lightgreen"]
rb=random.choice(coloursb)
rf=random.choice(coloursf)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
turtle.Screen().bgcolor("rosy brown")
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def insideF():
    "Return True if head inside boundaries."
    return -200 < food.x < 190 and -200 < food.y < 190

def moveFood():
    ranX = randrange(-10, 11, 10)
    ranY = randrange(-10, 11, 10)
    if ranX == -10:
        if food.x > -190:
            food.x += ranX
    if ranX == 10:
        if food.x < 190:
            food.x += ranX
    if ranY == -10:
        if food.y > -190:
            food.y += ranY
    if ranY == 10:
        if food.y < 190:
            food.y += ranY
    
    ontimer(moveFood, 450)

    if not insideF():
        square(food.x, food.y, 9, 'red')
        update()

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()


    for body in snake:
        square(body.x, body.y, 9, rb)

    square(food.x, food.y, 9, rf)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
moveFood()
done()
