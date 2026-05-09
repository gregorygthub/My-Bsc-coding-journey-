num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "*", num2, "=", num1 * num2)
if num2 != 0:
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("Error: Cannot divide by zero")

