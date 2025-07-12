def calculator():
    print("Welcome to My Personal Calculator!\n")
    
    try:
      
        num1 = float(input("Enter first number: "))
        num2 = float(input(" Enter second number: "))
        print("\nChoose an operation:")
        print(" + for Addition")
        print(" - for Subtraction")
        print(" * for Multiplication")
        print(" / for Division")
        print(" % for Modulus")
        
      
        operation = input(" Your choice: ")

      
        print("\n Calculating result")

        if operation == '+':
            result = num1 + num2
           print(f"Result: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f" Result: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f" Result: {num1} * {num2} = {result}")
        elif operation == '/':
           
      if num2 != 0:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            
      else:
                print(" Cannot divide by zero!")
        elif operation == '%':
            if num2 != 0:
                result = num1 % num2
                print(f" Result: {num1} % {num2} = {result}")
            else:
                print(" Cannot take modulus with zero!")
        else:
            print("Invalid operation selected.")

    except ValueError:
        print(" Please enter valid numbers only.")
calculator()
