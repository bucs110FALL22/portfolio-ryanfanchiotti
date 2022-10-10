def star_pyramid():
  starnum = int(input("how many rows?"))
  count = 0
  while count <= starnum:
    print(count * "*")
    count = count + 1

star_pyramid()

def rstar_pyramid():
  xx = int(input("how many rows?"))
  while xx > 0:
    print (xx * ("*"))
    xx = xx - 1

rstar_pyramid()