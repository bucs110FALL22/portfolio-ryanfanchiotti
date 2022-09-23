import turtle #1. import modules
import random
import time

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
michelangelo.forward(random.randrange(0,100))
leonardo.forward(random.randrange(0,100))
time.sleep(2)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range (0, 10):
  michelangelo.forward(random.randrange(0,10))
  leonardo.forward(random.randrange(0,10))

time.sleep(2)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
window.exitonclick()

# PART B - complete part B here

import pygame
import math

pygame.init()
window = pygame.display.set_mode()

coords = []
num_sides = 5
side_length = 100
offset = 100
color = (255, 0, 0)

for i in range(0,num_sides):
  theta = (2.0 * math.pi * i/num_sides) 
  x = side_length * math.cos(theta) +    offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))
print(coords)
pygame.draw.polygon(window, color, coords, 5)

