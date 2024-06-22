from turtle import *
from random import *
colors = ['blue', 'red', 'green', 'black', 'yellow', "orange", 'cyan', 'darkmagenta', 'navy', 'orchid', 'maroon', 'purple', 'gold', 'deepskyblue', 'darkred']
speed('fastest')
pensize(3)
hideturtle()
drawing = False

list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

def draw_figure(size, count):
    for i in range(count):
        forward(size)
        left(360/count)

def draw_field(x, y):
    penup()
    goto(x, y)
    pendown()
    for i in range(10):
        penup()
        goto(x, y-50*i)
        pendown()
        for j in range(10):
            draw_figure(50, 4)
            penup()
            forward(50)
            pendown()

second = Turtle()
second.hideturtle()

def y_axis(y):
    if y == 0:
        y = 200
        return y
    elif y == 1:
        y = 150
        return y
    elif y == 2:
        y = 100
        return y
    elif y == 3:
        y = 50
        return y
    elif y == 4:
        y = 0
        return y
    elif y == 5:
        y = -50
        return y
    elif y == 6:
        y = -100
        return y
    elif y == 7:
        y = -150
        return y
    elif y == 8:
        y = -200
        return y
    elif y == 9:
        y = -250
        return y
    
def click(x, y):
    global drawing, y_axis
    if drawing == False:
        if x >= -250 and x <= -200:
            x = 0
        elif x > -200 and x <= -150:
            x = 1
        elif x > -150 and x <= -100:
            x = 2
        elif x > -100 and x <= -50:
            x = 3
        elif x > -50 and x <= 0:
            x = 4
        elif x > 0 and x <= 50:
            x = 5
        elif x > 50 and x <= 100:
            x = 6
        elif x > 100 and x <= 150:
            x = 7
        elif x > 150 and x <= 200:
            x = 8
        elif x > 200 and x <= 250:
            x = 9
        else:
            x = None

        if y <= 250 and y >= 200:
            y = 0
        elif y < 200 and y >= 150:
            y = 1
        elif y < 150 and y >= 100:
            y = 2
        elif y < 100 and y >= 50:
            y = 3
        elif y < 50 and y >= 0:
            y = 4
        elif y < 0 and y >= -50:
            y = 5
        elif y < -50 and y >= -100:
            y = 6
        elif y < -100 and y >= -150:
            y = 7
        elif y < -150 and y >= -200:
            y = 8
        elif y < -200 and y >= -250:
            y = 9
        else: y = None
        
        if x != None and y != None:
            index = x + y * 10
            if list[index] == 0:
                drawing = True
                list[index] = 1
                second.color(choice(colors))
                second.speed('fastest')
                second.pensize(3)
                second.penup()
                second.goto(x * 50 - 250, y_axis(y))
                second.begin_fill()
                for i in range(4):
                    second.forward(50)
                    second.left(90)
                second.end_fill()
                drawing = False
        print(x, y)

draw_field(-250, 200)
onscreenclick(click)
mainloop()