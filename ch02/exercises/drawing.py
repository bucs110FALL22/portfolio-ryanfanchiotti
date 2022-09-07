import turtle
wn = turtle.Screen()
turtle1 = turtle.Turtle()

sides = int(input("How many sides?"))
length = int(input("How long is each side?"))

for i in range(0, sides):
  turtle1.forward(length)
  turtle1.left(eval("360 / sides"))

wn.exitonclick()