import turtle
import math

windowsize = 400
wheelsizefactor = 10
#wheelxvalue = 
#wheelyvalue = 
middleyvalue = 0
taxibasecolor = "yellow"
taxioutlinecolor = "black"
checkercolor1 = "black"
checkercolor2 = "white"
taxiheightfactor = 3
#trianglesizefactor = 
#eqtriangleheight = 
#topsquaresizefactor = 
#topsquarequantity = 
quarterrotation = 90
halfrotation = 180
fullrotation = 360
squaresides = 4
trianglesides = 3
speed = 10

window = turtle.Screen()
turtle1 = turtle.Turtle()
turtle.screensize(windowsize, windowsize)
turtle.hideturtle()
turtle1.hideturtle()
turtle1.penup()
turtle.speed(speed)


def lengthquestion():
  
  '''
  asks users how wide their drawing should be
  args: none
  return: length1 (int) input of question
  '''
  
  length1 = int(input("how wide would you like your drawing to be? this affects proportions"))
  return length1

def eqshape(side_length=50, color=(0,0,0), sides=4):
  
  '''
  uses turtle functions to trace an equilateral shape
  args: side_length (int) length of each side, color (str or tuple) color of the shape, sides (int) amount of sides shape will have
  return: shape drawing
  '''
  
  turtle1.color(color)
  turtle1.pendown()
  for i in range(sides):
    turtle1.forward(side_length)
    turtle1.left(fullrotation/sides)
  turtle1.penup()

def wheel(radius=10):
  
  '''
  uses turtle functions to draw a black wheel
  args: radius (int) radius of the wheel
  return: filled in wheel drawing
  '''
  turtle1.color("black")
  turtle1.pendown()
  turtle1.begin_fill()
  turtle1.circle(radius)
  turtle1.end_fill()
  turtle1.penup()

def taxi(length=100):

  '''
  uses turtle functions to trace a taxi and fill parts of it in
  args: length (int) length of the taxi that is drawn
  return: drawing of taxi
  '''
  
  turtle1.begin_fill()
  turtle1.goto(length/-2, middleyvalue)
  for i in range(3):
    eqshape(length/3, "yellow", squaresides)
    turtle1.forward(length/3)
  turtle1.end_fill()
  turtle1.goto(length/4, length/-8)
  wheel(length/wheelsizefactor)
  turtle1.goto(length/-4, length/-8)
  wheel(length/wheelsizefactor)
  turtle1.goto(length/-4, length/3)
  eqshape(length/4, "black", trianglesides)
  turtle1.forward(length/4)
  eqshape(length/4, "black", trianglesides)
  turtle1.left(90)
  turtle1.forward(length * math.sqrt(3)/8)
  turtle1.left(90)
  turtle1.forward(length/8)
  turtle1.right(180)
  for i in range(4):
    eqshape(length/16, "black", squaresides)
    turtle1.forward(length/16)
  turtle1.goto(length/-2, length/6)
  for i in range(10):
    turtle1.begin_fill()
    eqshape(length/20, checkercolor1, squaresides)
    turtle1.end_fill()
    turtle1.forward(length/20)
    turtle1.left(90)
    turtle1.forward(length/20)
    turtle1.right(90)
    turtle1.begin_fill()
    eqshape(length/20, checkercolor2, squaresides)
    turtle1.end_fill()
    turtle1.forward(length/20)
    turtle1.right(90)
    turtle1.forward(length/20)
    turtle1.left(90)
  turtle1.goto(length/-2, middleyvalue)
  for i in range(3):
    eqshape(length/3, "black", squaresides)
    turtle1.forward(length/3)

def main():
  length2 = lengthquestion()
  taxi(length2)
      
main()

window.exitonclick()