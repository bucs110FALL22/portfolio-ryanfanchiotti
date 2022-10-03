import turtle
import random
import time
wn = turtle.Screen()
width = 100
height = 100
wn.screensize(width,height)
turtle1 = turtle.Turtle()

turtle1.goto(0,0)
time.sleep(1)
xx = turtle1.xcor()
yy = turtle1.xcor()

while -width < xx < width and -height < yy < height:
  if random.randrange(2) == 0:
    turtle1.left(90)
    turtle1.forward(50)
  else:
    turtle1.right(90)
    turtle1.forward(50)
  time.sleep(1)
  xx = turtle1.xcor()
  yy = turtle1.xcor()