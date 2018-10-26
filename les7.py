import turtle
import random
import math

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()



def baraban(x, y):
    gotoxy(x, y)
    turtle.circle(80)
    gotoxy(0, 160)
    draw_circle(5, 'red')
    phi = 360 / 7
    r = 50
    for i in range(0, 7):
        phi_rad = phi * i * math.pi / 180.0
        gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 58)
        draw_circle(22, 'white')

def vrash(x,y):
    gotoxy(math.sin(phi_rad) * r+x, math.cos(phi_rad) * r + 58+y)
    draw_circle(22, 'brown')
    draw_circle(22, 'white')


turtle.speed(0)

baraban (0, 0)


answer = ''
start = 0

while answer != 'N':
    answer = turtle.textinput('Играем?', 'Y/N')
    if answer == 'Y':
        phi = 360 / 7
        r = 50
        for i in range(start, random.randrange(10, 22)):
            phi_rad = phi * i * math.pi / 180.0
            vrash(0,0)

        gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 58)
        draw_circle(22, 'brown')

        start = i % 7
        if start == 0:
            gotoxy(-150, 250)
            turtle.write('Вы проиграли!', font=('Arial', 18, 'normal'))




        #turtle.penup()
        #turtle.goto(random.randrange(-300,300), random.randrange(-300,300))
        # turtle.begin_fill()                                                  # начать закрашивать
        # turtle.circle(random.randrange(1,100))                        отрисовка случайних кругов
        #  turtle.end_fill()
    else:
        pass