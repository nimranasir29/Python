num1 = float(input("Enter 1st Number: "))
op = input("Enter Operator: ")
num2 = float(input("Enter 2nd Number: "))


if op == "+":
     print(num1 + num2)
elif op == "-":
     print(num1 - num2)
elif op == "/":
     print(num1 / num2)
elif op == "*":
     print(num1 * num2)
else:
     print("Invalid Operator")
