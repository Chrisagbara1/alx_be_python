def perform_operation():
      print("____Arithmetic Operations_____")
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower() 
      
      match operation:
           case "add":
               result = num1 + num2
               return f"Result: {result}"
           case "subtract":
               result = num1 - num2
               return f"Result: {result}"
           case "multiply":
               result = num1 * num2
               return f"Result: {result}"
           case "divide":
               if num2 != 0:
                  result = num1 / num2
                  return f"Result: {result}"
               else:
                  return "Cannot divide by zero."
           case _:
               return "Invalid operator."
print(perform_operation())
    