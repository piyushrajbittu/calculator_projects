# take input for operator and operand
number1 = input('enter the first number: ')
number2 = input('enter the second number: ')
operator = input('enter the operator: ')
print(type(number1), type(number2))
number1= int(number1)
number2 = int(number2)
print(type(number1), type(number2))
result = ''
if operator == '+':
  result = number1 +number2
elif operator == "-":
  result = number1 - number2
elif operator == "*":
  result = number1 * number2
elif operator == "/":
  result = number1 / number2
else:
  result = 'not defined'
result = number1 + number2
print('the result is : ' , result)
