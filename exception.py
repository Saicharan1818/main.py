# Division example with exception handling
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
print("Program continues...")

# Division with a single except for multiple errors
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except (ZeroDivisionError, ValueError):
    print("Error occurred: Zero division or invalid input.")

# Try-except-else block
try:
    num = int(input("Enter a number: "))
except:
    print("Oops")
else:
    print("You entered:", num)

# File handling with exception and finally
try:
    file = open("example.txt", "r")
    read_data = file.read()
    print(read_data)
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")

# Age validation with raise
age = int(input("Enter age: "))
if age < 18:
    raise Exception("Age must be at least 18!")
else:
    print("Age is valid.")