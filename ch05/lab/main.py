import pygame
display = pygame.display.set_mode((300,300))
pygame.init()

upperlimit = int(input("what is the highest number you'd like to graph?"))
iters = {}
max = 0
maxvalue = 0
scale = 10
displaytime = 5000
color = (255,0,0)
fontsize = 20
corner = (0, 0)
textpos = (10,10)

if upperlimit > 2:
  for i in range(2, upperlimit + 1):
    count = 0
    xx = i
    while i != 1:
      if i % 2 == 0:
        i = i/2
        count = count + 1
      else:
        i = 3*i + 1
        count = count + 1
    iters[xx * scale] = count * scale  
    if count > max:
      max = count
      maxvalue = xx
  coords = iters.items()
else:
  print("your number has to be higher than 2")
  quit()
coords2 = []
for x in coords:
  coords2.append(x)

text = ["the largest amount of iterations is", str(max), "at", str(maxvalue)]
text2 = " ".join(text)
pygame.draw.lines(display, color, False, coords2)
new_display = pygame.transform.flip(display, False, True)
display.blit(new_display,corner)
font = pygame.font.Font(None, fontsize)
msg = font.render(text2, False, color)
display.blit(msg, textpos)
pygame.display.flip()
pygame.time.wait(displaytime) 