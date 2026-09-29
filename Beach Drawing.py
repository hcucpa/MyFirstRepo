import turtle
import random
from random import randint
s = turtle.Screen()
s.bgcolor('gray10')
t = turtle.Turtle()
t.shape('arrow')
t.speed(300)
t.penup()
t.setpos(-0,-175)

mylistblue = [('CadetBlue'),('aquamarine'),('teal'),('cyan'),('cyan1'),('cyan2'),('cyan3'),('cyan4'),('darkcyan'),\
        ('aquamarine1'),('aquamarine2'),('aquamarine3'),('aquamarine4')]
tcounter = 0
# Stars
for i in range (30):
    t.color('azure2')
    t.penup()
    t.setpos(0 + randint(-325,325),0 + randint(-325,325))
    t.pendown()
    t.begin_fill()
    t.circle(-3,95)
    t.circle(3,-95)
    t.rt(180)
    t.circle(3,-95)
    t.circle(-3,95)
    t.end_fill()
# Sand Island
t.color('LightGoldenrod3')
t.speed(100)
t.penup()
t.setpos(-200,-200)
t.pendown
t.begin_fill()
t.rt(75)
t.circle(-250,90)
t.rt(135)
t.fd(300)
t.end_fill()

# Palm Tree Trunk
t.pendown()
t.color('chocolate3')
t.penup()
t.setpos(-10,-150)
t.pendown()
t.rt(180)
t.begin_fill()
t.lt(90)
t.circle(-600,30)
t.lt(120)
t.fd(20)
t.lt(57)
t.circle(600,30)
t.lt(90)
t.fd(36)
t.end_fill()

#Bottom Right LEaf
t.penup()
t.color('DarkGreen')
t.setpos(60,120)
t.rt(10)
t.pendown()
t.begin_fill()
t.circle(-100,50)
t.lt(160)
t.circle(100,70)
t.lt(120)
t.fd(30)
t.end_fill()

# Top right Leaf
t.penup()
t.color('chartreuse4')
t.setpos(70,130)
t.lt(90)
t.pendown()
t.begin_fill()
t.circle(-100,50)
t.lt(160)
t.circle(100,70)
t.lt(120)
t.fd(30)
t.end_fill()

# Left Leaf
t.speed(300)
t.penup()
t.color('DarkGreen')
t.setpos(30,150)
t.lt(240)
t.pendown()
t.begin_fill()
t.circle(100,50)
t.lt(160)
t.circle(-100,70)
t.lt(120)
t.fd(30)
t.end_fill()

#Top left leaf
t.speed(300)
t.penup()
t.setpos(35,164)
t.color('chartreuse4')
t.lt(60)
t.pendown()
t.begin_fill()
t.circle(100,50)
t.lt(160)
t.circle(-100,70)
t.lt(120)
t.circle(-100,40)
t.end_fill()

# Waves
t.speed(300)
t.penup()
t.setpos(-325,-195)
t.pendown()
t.color('blue4')
for i in range(13):
    t.begin_fill()
    t.lt(25)
    t.circle(-100,35)
    t.rt(120)
    t.circle(50,30)
    t.lt(100)
    t.end_fill()
t.begin_fill()
t.rt(105)
t.fd(100)
t.rt(90)
t.fd(700)
t.rt(90)
t.fd(140)
t.end_fill()

#Waves flat option
# t.penup()
# t.setpos(-325,-170)
# t.pendown()
# t.rt(17)
# t.color('blue4')
# t.begin_fill()
# t.fd(1000)
# t.rt(90)
# t.fd(200)
# t.rt(90)
# t.fd(1000)
# t.rt(90)
# t.fd(200)
# t.end_fill()



# Moon
t.color('azure2')
t.penup()
t.setpos(-375,315)
t.pendown()
t.begin_fill()
t.rt(30)
t.circle(-75)
t.end_fill()

#tree shade
t.color('chocolate4')
t.penup()
t.setpos(-10,-150)
t.pendown()
t.begin_fill()
t.lt(27)
t.circle(-600,26)
t.lt(160)
t.circle(600,1)
t.lt(18)
t.circle(600,25)
t.lt(90)
t.fd(10)
t.end_fill()

#Sand Shade
t.color('LightGoldenrod4')
t.begin_fill()
t.circle(-250,29)
t.lt(61)
t.circle(-100,8)
t.lt(125)
t.circle(250,32)
t.end_fill()

#Coconuts

#Right Coconut
t.penup()
t.color('gray20')
t.setpos(71,109)
t.pendown()
t.dot(30)
t.penup()
t.setpos(70,110)
t.pendown()
t.color('DarkGoldenrod4')
t.dot(30)

#Left Coconut
t.penup()
t.setpos(20,120)
t.pendown()
t.color('DarkGoldenrod4')
t.dot(30)

# Moon Circles
t.penup()
t.setpos(-300,245)
t.pendown
t.color('azure3')
t.dot(15)
t.penup()
t.setpos(-260,275)
t.pendown
t.dot(25)
t.penup()
t.setpos(-300,275)
t.pendown()
t.dot(10)

# Turtle pen last shape
t.color("DarkSlateGray")
t.penup()
t.setpos(-100,-225)
t.pendown()
t.shape("turtle")
t.shapesize(3)


# t.hideturtle()
turtle.done()