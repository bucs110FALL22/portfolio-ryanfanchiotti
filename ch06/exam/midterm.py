import turtle
import math

window = turtle.Screen()
turtle1 = turtle.Turtle()
turtle.screensize(400, 400)
turtle.hideturtle()
turtle1.hideturtle()
turtle1.penup()
turtle1.goto(0,0)
turtle.speed(10)



def lengthquestion():
  length1 = int(input("how large would you like your drawing to be?"))
  return length1

def eqshape(side_length, color, sides):
  turtle1.color(color)
  turtle1.pendown()
  for i in range(sides):
    turtle1.forward(side_length)
    turtle1.left(360/sides)
  turtle1.penup()

def wheel(radius, color):
  turtle1.color(color)
  turtle1.pendown()
  turtle1.begin_fill()
  turtle1.circle(radius)
  turtle1.end_fill()
  turtle1.penup()

def taxi(length):
  turtle1.begin_fill()
  turtle1.goto(length/-2, 0)
  for i in range(3):
    eqshape(length/3, "yellow", 4)
    turtle1.forward(length/3)
  turtle1.end_fill()
  turtle1.goto(length/4, length/-8)
  wheel(length/10, "black")
  turtle1.goto(length/-4, length/-8)
  wheel(length/10, "black")
  turtle1.goto(length/-4, length/3)
  eqshape(length/4, "black", 3)
  turtle1.forward(length/4)
  eqshape(length/4, "black", 3)
  turtle1.left(90)
  turtle1.forward(length * math.sqrt(3)/8)
  turtle1.left(90)
  turtle1.forward(length/8)
  turtle1.right(180)
  for i in range(4):
    eqshape(length/16, "black", 4)
    turtle1.forward(length/16)
  turtle1.goto(length/-2, length/6)
  for i in range(10):
    turtle1.begin_fill()
    eqshape(length/20, "black", 4)
    turtle1.end_fill()
    turtle1.forward(length/20)
    turtle1.left(90)
    turtle1.forward(length/20)
    turtle1.right(90)
    turtle1.begin_fill()
    eqshape(length/20, "white", 4)
    turtle1.end_fill()
    turtle1.forward(length/20)
    turtle1.right(90)
    turtle1.forward(length/20)
    turtle1.left(90)
  turtle1.goto(length/-2, 0)
  for i in range(3):
    eqshape(length/3, "black", 4)
    turtle1.forward(length/3)

def main():
  length2 = lengthquestion()
  taxi(length2)
      
main()

window.exitonclick()