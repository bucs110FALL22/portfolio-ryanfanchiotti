import turtle
import math
window = turtle.Screen()
turtle1 = turtle.Turtle()
turtle.screensize(400, 400)
#turtle1.hideturtle()
turtle1.penup()
turtle1.goto(0,0)
turtle.speed(3)

def lengthquestion():
  length1 = int(input("how wide would you like your drawing to be?"))
  return length1

def eqshape(side_length, color, sides):
  turtle1.color(color)
  turtle1.pendown()
  for i in range(0, sides):
    turtle1.forward(side_length)
    turtle1.left(eval("360 / sides"))
  turtle1.penup()

def wheel(radius):
  turtle1.color("black")
  turtle1.pendown()
  turtle1.circle(radius)
  turtle1.color("grey")
  turtle1.circle(radius * 5/7)
  turtle1.penup()

def taxi(length):
  turtle1.begin_fill()
  turtle1.goto(length / -2, 0)
  for i in range(3):
    eqshape(length / 3, "yellow", 4)
    turtle1.forward(length/3)
  turtle1.end_fill()
  turtle1.goto(length*(5/6), 0)
  wheel(length/10)
  turtle1.goto(length*(-5/6), 0)
  wheel(length/10)
  

def main():
  length2 = lengthquestion()
  taxi(length2)
      
main()

window.exitonclick()