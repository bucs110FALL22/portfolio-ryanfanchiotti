import pygame
import time
import math
import random

width = 250
height = 250 

pygame.init()
window = pygame.display.set_mode((width,height))

pygame.draw.circle(window, (9,99,9), (125, 125), 125.0, width = 0)
pygame.draw.circle(window, "white", (125, 125), 125.0, width = 2)
pygame.draw.line(window, "white", (125, 0) , (125, 250), width = 2)
pygame.draw.line(window, "white", (0, 125) , (250, 125), width = 2)

pygame.display.flip()
time.sleep(1)

xcor = random.randrange(0,width)
ycor = random.randrange(0,height)
hit_color = (255,0,0)
miss_color = (0,0,255)
if
pygame.draw.circle(window, "red", (xcor, ycor), 5, width = 0)
pygame.display.flip()
time.sleep(3)
