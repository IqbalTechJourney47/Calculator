from addition import add
from subtraction import subtract
from multiplication import multiply
from division import div

print("Select an operation to perform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    add(num1, num2)

elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    subtract(num1, num2)

elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    multiply(num1, num2)

elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    div(num1, num2)

else:
    print("Invalid Entry")
