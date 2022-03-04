# program to perform arthmetic operations

x, y = map(float, input("Enter two numbers: ").split())
op = input("Enter the operator (+, -, *, /): ")

if op == "+":
    print(f"{x} + {y} = {x+y}")
elif op == "-":
    print(f"{x} - {y} = {x-y}")
elif op == "*":
    print(f"{x} * {y} = {x*y}")
elif op == "/":
    print(f"{x} / {y} = {x/y}")
else:
    print("Not a correct operator")
