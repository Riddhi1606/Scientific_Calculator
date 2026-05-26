# =========================================
# Advanced Scientific Calculator in Python
# =========================================

import math

# List to store calculation history
history = []


# ---------- Functions ----------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b


def square_root(x):
    if x < 0:
        return "Invalid Input"
    return math.sqrt(x)


def logarithm(x):
    if x <= 0:
        return "Invalid Input"
    return math.log10(x)


def sine(x):
    return math.sin(math.radians(x))


def cosine(x):
    return math.cos(math.radians(x))


def tangent(x):
    return math.tan(math.radians(x))


def degree_to_radian(x):
    return math.radians(x)


def radian_to_degree(x):
    return math.degrees(x)


# ---------- Main Program ----------

while True:

    print("\n========== SCIENTIFIC CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Square Root")
    print("8. Logarithm")
    print("9. Value of Pi")
    print("10. Sin(x)")
    print("11. Cos(x)")
    print("12. Tan(x)")
    print("13. Degree to Radian")
    print("14. Radian to Degree")
    print("15. View History")
    print("16. Clear History")
    print("17. Exit")
    print("===========================================")

    choice = input("Enter your choice (1-17): ")

    try:

        # Addition
        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = add(a, b)

            print("Result:", result)

            history.append(f"{a} + {b} = {result}")

        # Subtraction
        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = subtract(a, b)

            print("Result:", result)

            history.append(f"{a} - {b} = {result}")

        # Multiplication
        elif choice == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = multiply(a, b)

            print("Result:", result)

            history.append(f"{a} × {b} = {result}")

        # Division
        elif choice == '4':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = divide(a, b)

            print("Result:", result)

            history.append(f"{a} ÷ {b} = {result}")

        # Power
        elif choice == '5':
            a = float(input("Enter base number: "))
            b = float(input("Enter power: "))

            result = power(a, b)

            print("Result:", result)

            history.append(f"{a} ^ {b} = {result}")

        # Modulus
        elif choice == '6':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = modulus(a, b)

            print("Result:", result)

            history.append(f"{a} % {b} = {result}")

        # Square Root
        elif choice == '7':
            number = float(input("Enter number: "))

            result = square_root(number)

            print("Square Root:", result)

            history.append(f"√{number} = {result}")

        # Logarithm
        elif choice == '8':
            number = float(input("Enter number: "))

            result = logarithm(number)

            print("Log Value:", result)

            history.append(f"log({number}) = {result}")

        # Pi
        elif choice == '9':
            result = math.pi

            print("Value of Pi:", result)

            history.append(f"Pi = {result}")

        # Sin(x)
        elif choice == '10':
            angle = float(input("Enter angle in degrees: "))

            result = sine(angle)

            print("Sin(", angle, ") =", result)

            history.append(f"sin({angle}) = {result}")

        # Cos(x)
        elif choice == '11':
            angle = float(input("Enter angle in degrees: "))

            result = cosine(angle)

            print("Cos(", angle, ") =", result)

            history.append(f"cos({angle}) = {result}")

        # Tan(x)
        elif choice == '12':
            angle = float(input("Enter angle in degrees: "))

            result = tangent(angle)

            print("Tan(", angle, ") =", result)

            history.append(f"tan({angle}) = {result}")

        # Degree to Radian
        elif choice == '13':
            degree = float(input("Enter degree value: "))

            result = degree_to_radian(degree)

            print("Radians:", result)

            history.append(f"{degree}° = {result} radians")

        # Radian to Degree
        elif choice == '14':
            radian = float(input("Enter radian value: "))

            result = radian_to_degree(radian)

            print("Degrees:", result)

            history.append(f"{radian} radians = {result}°")

        # View History
        elif choice == '15':

            print("\n========== CALCULATION HISTORY ==========")

            if len(history) == 0:
                print("No calculations performed yet.")

            else:
                for item in history:
                    print(item)

        # Clear History
        elif choice == '16':

            history.clear()

            print("History Cleared Successfully.")

        # Exit
        elif choice == '17':

            print("Scientific Calculator Closed")

            break

        else:
            print("Invalid Choice! Please select valid option.")

    except ValueError:
        print("Please enter valid numeric input.")
