def percentage_to_letter(score=0):
  if score >= 90:
    return("A")
  elif score >= 80:
    return("B")
  elif score >= 70:
    return("C")
  elif score >= 60:
    return("D")
  else:
    return("F")

  
def is_passing(letter=None):
  if letter == "A":
    return(True)
  elif letter == "B":
    return(True)
  elif letter == "C":
    return(True)
  else:
    return(False)

scoreinput = float(input("what score did you recieve?"))
print(scoreinput)
lettergrade = percentage_to_letter(scoreinput)
print(lettergrade)
passfail = is_passing(lettergrade)
print(passfail)
if passfail is True:
  print("You passed!")
else:
  print("You failed")


