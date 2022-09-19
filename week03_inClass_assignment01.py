#week_03_inClass_assignment01
#create python program that draws consecutive squares.
#author: Joshua McBratnie
#date: 09.12.2022

from turtle import *
#define constant params
sideLength = 25
shape("turtle")
#use function to repeat square shape with x variable to change size. 
def square_func(x):
    goto(sideLength*x,0)
    pendown()
    color('red')
    goto(sideLength*x,sideLength*x)
    goto(-sideLength*x,sideLength*x)
    goto(-sideLength*x,-sideLength*x)
    goto(sideLength*x,-sideLength*x)
    goto(sideLength*x,0)
    penup()
#use dot to call out the center point and draw the item. 
dot(5,'blue')
penup()
square_func(1)
square_func(3)
goto(-sideLength*6,-sideLength*6)
setheading(90)
color('blue')
done()


