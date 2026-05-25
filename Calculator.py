# =============================
# Advanced Beginner Calculator
# =============================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b


# To store calculation history
history = []


def show_menu():
    print("\n========= PYTHON CALCULATOR =========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. View History")
    print("8. Exit")
    print("=====================================")


while True:
    show_menu()

    choice = input("Enter your choice (1-8): ")

    # View History
    if choice == '7':
        print("\n------ Calculation History ------")
        if len(history) == 0:
            print("No calculations yet.")
        else:
            for item in history:
                print(item)
        continue

    # Exit Program
    elif choice == '8':
        print("Thank you for using the calculator!")
        break

    # Operations
    elif choice in ['1', '2', '3', '4', '5', '6']:

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                operation = f"{num1} + {num2} = {result}"

            elif choice == '2':
                result = subtract(num1, num2)
                operation = f"{num1} - {num2} = {result}"

            elif choice == '3':
                result = multiply(num1, num2)
                operation = f"{num1} × {num2} = {result}"

            elif choice == '4':
                result = divide(num1, num2)
                operation = f"{num1} ÷ {num2} = {result}"

            elif choice == '5':
                result = power(num1, num2)
                operation = f"{num1} ^ {num2} = {result}"

            elif choice == '6':
                result = modulus(num1, num2)
                operation = f"{num1} % {num2} = {result}"

            print("\nResult:", result)

            # Save history
            history.append(operation)

        except ValueError:
            print("Invalid input! Please enter numeric values.")

    else:
        print("Invalid choice! Please select between 1 to 8.")