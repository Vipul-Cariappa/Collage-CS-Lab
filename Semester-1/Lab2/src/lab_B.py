# program to find quotient and reminder of two numbers

x, y = input("Enter two Numbers to find quotient and reminder: ").split()
x, y = int(x), int(y)

quotient = x // y
reminder = x % y

print(f"{quotient = }   {reminder = }")
