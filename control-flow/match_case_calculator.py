num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")
match operator:
    case "+":
        addition = num1 + num2
        print("The result is", addition)
    case "-":
        subtraction = num1 - num2
        print("The result is", subtraction)
    case "*":
        multiplication = num1 * num2
        print("The result is", multiplication)
    case "/":
        if num2 != 0:
          division = num1 / num2
          print("The result is", division)
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operator")