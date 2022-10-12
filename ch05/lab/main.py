import pygame
display = pygame.display.set_mode()
pygame.init()

upperlimit = 20
iters = {}
max = 0
  
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
  iters[xx] = count  
  if count > max:
    max = count
    maxvalue = xx
print(iters)
print("the max is", max)
coords = iters.items()
print(coords)

#pygame.draw.lines(display, (255, 0, 0), False, iters.items())
#new_display = pygame.transform.flip(display, False, True)
#display.blit(new_display,(0, 0))

 