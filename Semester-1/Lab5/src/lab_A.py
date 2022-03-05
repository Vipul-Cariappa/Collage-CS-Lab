# program to find sum of digits


# Solution 1:
x = int(input("Enter a Number: "))
s = 0

while x:
    s += x % 10
    x //= 10


print(f"Sum of digits: {s}")


# Solution 2:
x = input("Enter a Number: ")

s = 0

for i in x:
    s += int(i)

print("Sum of digits:", s)
