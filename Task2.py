
while True:
    print("\nWelcome to the Calculator!")
    
    try:
        
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        ope = input("Choose an operator (+, -, /, *): ")
        
        
        if ope == '+':
            print("You have chosen Addition.")
            print("The sum of the given numbers is:", num1 + num2)
        elif ope == '-':
            print("You have chosen Subtraction.")
            print("The difference of the given numbers is:", num1 - num2)
        elif ope == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print("You have chosen Division.")
                print("The quotient of the given numbers is:", num1 / num2)
        elif ope == '*':
            print("You have chosen Multiplication.")
            print("The product of the given numbers is:", num1 * num2)
        else:
            print("Invalid operator! Please choose one of +, -, /, *.")
        
      
        cont = input("\nDo you want to perform another calculation? (y/n): ").lower()
        if cont == 'n':
            print("Thanks for using the calculator! Goodbye!")
            break

    except ValueError:
        print("Invalid input! Please enter numeric values for numbers.")

