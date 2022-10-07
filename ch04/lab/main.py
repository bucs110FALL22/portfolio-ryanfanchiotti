import pygame
import time
import math
import random

width = 250
height = 250 
center = (125, 125)
centerx = 125
centery = 125
dartboardcolor = (9,99,9)
line1start = (125, 0)
line1end = (125, 250)
line2start = (0, 125)
line2end = (250, 125)
radius = 125.0
pygame.init()
window = pygame.display.set_mode((width, height))

pygame.draw.circle(window, dartboardcolor, center, radius, width = 0)
pygame.draw.circle(window, "white", center, radius, width = 2)
pygame.draw.line(window, "white", line1start, line1end, width = 2)
pygame.draw.line(window, "white", line2start, line2end, width = 2)

pygame.display.flip()
time.sleep(1)

for i in range(10):
  xcor = random.randrange(0,width)
  ycor = random.randrange(0,height)
  hit_color = (255,255,0)
  miss_color = (255,165,0)

  distance_from_center = math.hypot(xcor - centerx, ycor - centery)
  is_in_circle = distance_from_center <= width/2

  if is_in_circle is True:
    color1 = hit_color
  else:
    color1 = miss_color

  pygame.draw.circle(window, color1, (xcor, ycor), 5, width = 0)
  pygame.display.flip()
  time.sleep(0.5)

print("click the color that you think will win!")
redbox = pygame.Rect(0,0,125,250)
bluebox = pygame.Rect(125,0,125,250)
blackbox = pygame.Rect(0,0,250,250)
choice = 0
pygame.draw.rect(window, "red", redbox)
pygame.draw.rect(window, "blue", bluebox)
pygame.display.flip()

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      x,y = pygame.mouse.get_pos()
      if pygame.Rect.collidepoint(redbox, x,y):
        print("red has been selected")
        choice = 1
        running = False
      if pygame.Rect.collidepoint(bluebox, x,y):
        print("blue has been selected")
        choice = 2
        running = False
    if event.type == pygame.QUIT:
      running = False

pygame.draw.rect(window, "black", blackbox)

pygame.draw.circle(window, dartboardcolor, center, radius, width = 0)
pygame.draw.circle(window, "white", center, radius, width = 2)
pygame.draw.line(window, "white", line1start, line1end, width = 2)
pygame.draw.line(window, "white", line2start, line2end, width = 2)
pygame.display.flip()

redhits = 0
bluehits = 0
for i in range(10):
  redxcor = random.randrange(0,width)
  redycor = random.randrange(0,height)
  bluexcor = random.randrange(0,width)
  blueycor = random.randrange(0,height)
 

  red_distance_from_center = math.hypot(redxcor - centerx, redycor - centery)
  red_is_in_circle = red_distance_from_center <= width/2
  blue_distance_from_center = math.hypot(bluexcor - centerx,       blueycor - centery)
  blue_is_in_circle = blue_distance_from_center <= width/2

  if red_is_in_circle is True:
    redhits = redhits + 1
    reddotcolor = "red"
  else:
    reddotcolor = "white"
  if blue_is_in_circle is True:
    bluehits = bluehits + 1
    bluedotcolor = "blue"
  else:
    bluedotcolor = "white"

  pygame.draw.circle(window, reddotcolor, (redxcor, redycor), 5, width=0)
  pygame.display.flip()
  pygame.draw.circle(window, bluedotcolor, (bluexcor, blueycor), 5, width=0)
  pygame.display.flip()
  time.sleep(0.5)

print("blue hit this many times:")
print(bluehits)
print("red hit this many times:")
print(redhits)

if choice == 1:
  if redhits > bluehits:
    print("your choice was correct")
  elif redhits < bluehits:
    print("your choice was incorrect")
  elif redhits == bluehits:
    print("it was a tie")
if choice == 2:
  if bluehits > redhits:
    print("your choice was correct")
  elif bluehits < redhits:
    print("your choice was incorrect")
  elif redhits == bluehits:
    print("it was a tie")