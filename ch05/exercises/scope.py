def multiply(num1, num2):
  value = num1
  for i in range(num2-1):
    num1 = num1 + value
  return(num1)

number1 = multiply(4,7)
print(number1)

def exponentiate(num, exp):
  value = num
  for i in range(exp-1):
    num = num * value
  return(num)

number2 = exponentiate(6,3)
print(number2)

def square(num):
  value = multiply(num,num)
  return(value)

number3 = square(13)
print(number3)