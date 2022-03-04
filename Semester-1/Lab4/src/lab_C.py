# program to find roots of quadratic equation

a, b, c = map(int, input("Enter coefficients of the quadratic equation: ").split())

sup_script = "\u00b2"
equation = f"{a}x{sup_script} + {b}x + {c}"

d = b*b - 4*a*c

if d < 0:
    root1 = (-b + d**0.5)/(2*a)
    root2 = (-b - d**0.5)/(2*a)
    print(f"The given quadratic equation {equation} does not have real roots: \n{root1} and {root2}")
elif d > 0:
    root1 = (-b + d**0.5)/(2*a)
    root2 = (-b - d**0.5)/(2*a)
    print(f"The roots of given quadratic equation {equation} are real and distinct: \n{root1} and {root2}")
else:
    root = -b/(2*a)
    print(f"The roots of given quadratic equation {equation} is real: \n{root}")

