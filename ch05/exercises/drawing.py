import turtle
wn = turtle.Screen()
turtle1 = turtle.Turtle()
num_sides = int(input("how many sides?"))
side_length = int(input("how long will each side be?"))
turtle1.color("green")
wn.screensize(400,400)
wn.bgcolor("white")
turtle1.shape("turtle")

def draweqshape(turtle1, num_sides, side_length):
  for i in range(num_sides):
    turtle1.forward(side_length)
    turtle1.left(360 / num_sides)
  wn.exitonclick()

draweqshape(turtle1, num_sides, side_length)

