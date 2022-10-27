import turtle
import math

windowsize = 400
wheelsizefactor = 10
wheelxvaluefactor = 4
wheelyvaluefactor = 8
middleyvalue = 0
taxibasecolor = "yellow"
taxioutlinecolor = "black"
checkercolor1 = "black"
checkercolor2 = "white"
taxiheightfactor = 3
trianglesizefactor = 4
eqtriangleheight = math.sqrt(3)/8
topsquaresizefactor = 16
topsquarequantity = 4
quarterrotation = 90
halfrotation = 180
fullrotation = 360
squaresides = 4
trianglesides = 3
speed = 10
doublingfactor = 2
checkerquantity = 20
eachcolorcheckerquantity = int(checkerquantity/2)

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
  turtle1.goto(length/-doublingfactor, middleyvalue)
  for i in range(taxiheightfactor):
    eqshape(length/taxiheightfactor, taxibasecolor, squaresides)
    turtle1.forward(length/taxiheightfactor)
  turtle1.end_fill()
  turtle1.goto(length/wheelxvaluefactor, length/-wheelyvaluefactor)
  wheel(length/wheelsizefactor)
  turtle1.goto(length/-wheelxvaluefactor, length/-wheelyvaluefactor)
  wheel(length/wheelsizefactor)
  turtle1.goto(length/-trianglesizefactor, length/taxiheightfactor)
  eqshape(length/trianglesizefactor, taxioutlinecolor, trianglesides)
  turtle1.forward(length/trianglesizefactor)
  eqshape(length/trianglesizefactor, taxioutlinecolor, trianglesides)
  turtle1.left(quarterrotation)
  turtle1.forward(length * eqtriangleheight)
  turtle1.left(quarterrotation)
  turtle1.forward(length/(trianglesizefactor*doublingfactor))
  turtle1.right(halfrotation)
  for i in range(topsquarequantity):
    eqshape(length/topsquaresizefactor, taxioutlinecolor, squaresides)
    turtle1.forward(length/topsquaresizefactor)
  turtle1.goto(length/-doublingfactor, length/(taxiheightfactor*doublingfactor))
  for i in range(eachcolorcheckerquantity):
    turtle1.begin_fill()
    eqshape(length/checkerquantity, checkercolor1, squaresides)
    turtle1.end_fill()
    turtle1.forward(length/checkerquantity)
    turtle1.left(quarterrotation)
    turtle1.forward(length/checkerquantity)
    turtle1.right(quarterrotation)
    turtle1.begin_fill()
    eqshape(length/checkerquantity, checkercolor2, squaresides)
    turtle1.end_fill()
    turtle1.forward(length/checkerquantity)
    turtle1.right(quarterrotation)
    turtle1.forward(length/checkerquantity)
    turtle1.left(quarterrotation)
  turtle1.goto(length/-doublingfactor, middleyvalue)
  for i in range(taxiheightfactor):
    eqshape(length/taxiheightfactor, taxioutlinecolor, squaresides)
    turtle1.forward(length/taxiheightfactor)

def main():
  length2 = lengthquestion()
  taxi(length2)
      
main()

window.exitonclick()