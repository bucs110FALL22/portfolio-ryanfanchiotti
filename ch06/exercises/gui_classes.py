class Shirts:
  def __init__(self, amount):
    self.shirt_quantity = amount
    self.shirt_color = (0,0,0)
    self.long_sleeve = False

class Person:
  def __init__(self, eyecolor, size):
    self.person_age = 0
    self.person_eyecolor = eyecolor
    self.person_size = size

class Laptop:
  def __init__(self, color):
    self.laptop_color = (0,0,0)
    self.is_laptop_on = False
    self.laptop_battery = 100