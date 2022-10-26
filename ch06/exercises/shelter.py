import time

class Animal:
  def __init__(self, name, type):
    self.name = str(name)
    self.type = str(type)
    self.adoption_date = time.strftime("%d/%m/%Y")
    self.id = id(self)

  def setAdopted(self, dd, mm, yyyy):
    self.adoption_date = str(dd) + "/" + str(mm) + "/" + str(yyyy)

  def info(self):
    return self.name, self.type, self.adoption_date, self.id
    
def main():
  garfield = Animal("garfield", "cat")
  q1 = int(input("was this animal adopted today? type 1 if so and 2 if not"))
  if q1 == 2:
    q2 = int(input("what year was this animal adopted?"))
    q3 = int(input("what month was this animal adopted?"))
    q4 = int(input("what day of the month was this animal adopted?"))
    garfield.setAdopted(q4,q3,q2)
  print(garfield.info())
main()