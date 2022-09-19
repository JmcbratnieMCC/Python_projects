#week_03_inClass_assignment02
#create python program that draws a traffic light
#author: Joshua McBratnie
#date: 09.12.2022

from turtle import *
#define function to draw lights taking in color and location
def lightCircle(x,lightColor):
    goto(0,x)
    pendown()
    pensize(2)
    fillcolor(lightColor)
    begin_fill()
    circle(20)
    end_fill()
    penup()
#draw sides 
def drawSides():
    goto(30,20)
    pendown()
    goto(30,120)
    goto(-30,120)
    goto(-30,-80)
    goto(30,-80)
    goto(30,20)
    penup()
#function outputs
lightCircle(0,'yellow')
lightCircle(60,'red')
lightCircle(-60,'green')
drawSides()
hideturtle()


done()