# program to find if the given number is zero, negative or positive

x = int(input("Enter a number: "))

if x > 0:
    print(f"Given number {x} is positive")
elif x < 0:
    print(f"Given number {x} is negative")
else:
    print(f"Given number {x} is zero")
