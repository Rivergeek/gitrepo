import turtle
import random
import math

import mrrobot


turtle.speed(0)

phi = 360 / 7
r = 50

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()



def baraban(xc, yc):
    gotoxy(xc, yc)
    turtle.circle(80)
    gotoxy(0 + xc, 160 + yc)
    draw_circle(5, 'red')
    phi = 360 / 7
    r = 50
    for i in range(0, 7):
        phi_rad = phi * i * math.pi / 180.0
        gotoxy(math.sin(phi_rad) * r + xc, math.cos(phi_rad) * r + 58 + yc)
        draw_circle(22, 'white')


def vrash(xc,yc, start):
    for i in range(start, random.randrange(10, 22)):
        phi_rad = phi * i * math.pi / 180.0
        gotoxy(math.sin(phi_rad) * r+xc, math.cos(phi_rad) * r + 58+yc)
        draw_circle(22, 'brown')
        draw_circle(22, 'white')

    gotoxy(math.sin(phi_rad) * r + xc, math.cos(phi_rad) * r + 58 + yc)
    draw_circle(22, 'brown')

    return i % 7




baraban(100, 100)


answer = ''
start = 0

while answer != 'N':
    answer = turtle.textinput('Играем?', 'Y/N')
    if answer == 'Y':
        vrash(100, 100, start)

        start = 0
        if start == vrash(100, 100, start):
            gotoxy(-150, 250)
            turtle.write('Вы проиграли!', font=('Arial', 18, 'normal'))
            xrandom = random.randrange(0, 2)
            if xrandom == 0:
                mrrobot.del_file('test')
            else:
                mrrobot.dupl_files()




        #turtle.penup()
        #turtle.goto(random.randrange(-300,300), random.randrange(-300,300))
        # turtle.begin_fill()                                                  # начать закрашивать
        # turtle.circle(random.randrange(1,100))                        отрисовка случайних кругов
        #  turtle.end_fill()
    else:
        pass