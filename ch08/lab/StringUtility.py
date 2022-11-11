class StringUtility:
  def __init__(self, string):
    self.string = string
  
  def __str__(self):
    '''
    returns internal string
	  args: none
	  return: (str) internal string
    '''  
    return self.string
  
  def vowels(self):
    '''
    counts the amount of vowels in a word and returns that number if it is less than 5, otherwise it returns "many"
	  args: none
	  return: (str) amount of vowels in a word or "many"
    '''  
    allupper = self.string.upper()
    count = 0
    vowels = ["A", "E", "I", "O", "U"]
    for i in allupper:
      if i in vowels:
        count += 1
      if count > 4:
        count = "many"
        break
    return str(count)
    
  def bothEnds(self):
    '''
    takes two letters from the start and end of a string and puts them together
	  args: none
	  return: (str) a 4 letter string
    '''  
    if len(self.string) > 2:
      return self.string[0]+self.string[1]+self.string[-2]+self.string[-1]
    else: 
      return ""
      
  def fixStart(self):
    '''
    takes a string and returns a version of it in which all repeated iterations of the first character are replaced with "*"
	  args: none
	  return: (str) string with some letters replaced with "*"
    '''  
    if len(self.string) == 0:
       return(self.string)
    letter1 = self.string[0]
    str = self.string
    for i in self.string:
       if i == letter1:
         str = str.replace(i,"*")
    str = str.replace("*",letter1,1)
    return str
    
  def asciiSum(self):
    '''
    takes a string, calculates all ascii values of characters inside, and adds them together
	  args: none
	  return: (int) sum of all ascii values in a given string
    '''  
    asciisum = 0
    for i in self.string:
      asciisum += ord(i)
    return asciisum
    
  def cipher(self):
    '''
    takes a string and swaps each character excluding spaces by a character the length of the string farther down the alphabet
	  args: none
	  return: (type) string with swapped letters
    '''  
    length = len(self.string)
    output = ""
    spaceunicode = 32
    str = self.string
    for i in str:
      if ord(i) == spaceunicode:
        output += i
      else:
        if i.isupper():
          output += chr((ord(i)+length-65)%26+65) 
        else:
          output += chr((ord(i)+length-97)%26+97)
    return output