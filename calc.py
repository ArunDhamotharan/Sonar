def calculate(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Division by zero not allowed."
        return num1 / num2
    else:
        return "Invalid operator."


 num1 = float(input("Enter first number: "))
 num2 = float(input("Enter second number: "))
 operator = input("Choose operation (+, -, *, /): ")
 result = calculate(operator, num1, num2)
 print("Result:", result)
