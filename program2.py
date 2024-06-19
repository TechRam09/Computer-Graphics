import turtle
import math


screen = turtle.Screen()
screen.bgcolor('white')

t= turtle.Turtle()
turtle.speed(1)
turtle.pensize(2)

def draw_rectangle(x,y,width,height,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

def draw_circle(x,y,radius,color):
    turtle.penup()
    turtle.goto(x,y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(radius)
    

def translate(x,y,dx,dy):
    turtle.penup()
    turtle.goto(x+dx,y+dy)
    turtle.pendown()

def rotate(x,y,angle):
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(angle)
    turtle.pendown()

def scaling(x,y,sx,sy):
    turtle.penup()
    turtle.goto(x*sx, y*sy)
    turtle.pendown()
    

draw_rectangle(-200,0,100,50,'blue')
translate(-200,0,200,0)
draw_rectangle(0,0,100,50,'blue')
rotate(0,0,45)
draw_rectangle(0,0,100,50,'blue')
scaling(0,0,2,2)
draw_rectangle(0,0,100,50,'blue')

draw_circle(100,100,50,'red')
translate(100,100,200,0)
draw_circle(300,100,50,'red')
rotate(300,100,45)
draw_circle(300,100,50,'red')
scaling(300,100,2,2)
draw_circle(600,200,50,'red')

turtle.done()