def calculator():
    while True:
        print("Select the operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter your choice (1/2/3/4): ")
        """if choice != 1 or choice !=2 or choice !=3 or choice !=4:
            print("Enter the valid choice : ")
            calculator()
"""
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        match choice:
            case "1":
                print(num1, "+", num2, "=", num1 + num2)
            case "2":
                print(num1, "-", num2, "=", num1 - num2)
            case "3":
                print(num1, "*", num2, "=", num1 * num2)
            case "4":
                if num2 != 0:
                    print(num1, "/", num2, "=", num1 / num2)
                else:
                    print("Error! Division by zero is not allowed.")
            case _:
                print("Invalid choice. Please try again.")

        repeat = input("Do you want to perform another operation? (yes/no): ")
        if repeat.lower() != "yes":
            break

calculator()