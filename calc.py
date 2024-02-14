def add(a, b):
  """Adds two numbers together.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The sum of a and b.
  """
  return a + b

def subtract(a, b):
  """Subtracts two numbers.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The difference of a and b.
  """
  return a - b


 def divide(a, b):
   

  Args:
     a: The first number.
     b: The second number.

   Returns:
     The quotient of a and b.
   Raises:
     ZeroDivisionError: If b is zero.   
 return a / b

def multiply(a, b):
  

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The product of a and b.

  return a * b

if __name__ == "__main__":
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  operation = input("Choose operation (+, -, *, /): ")

  if operation == "+":
    result = add(num1, num2)
  elif operation == "-":
    result = subtract(num1, num2)

 elif operation == "/":
    result = divide(num1, num2)
  elif operation == "*":
    result = multiply(num1, num2)
  else:
    print("Invalid operation.")

  print("Result:", result)
