# program to find factorial of a number using recursion

def factorial(x):
    if x < 2:
        return 1
    return x * factorial(x - 1)

n = int(input("Enter a number: "))
print(factorial(n))
