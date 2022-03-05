# program to check if given number is perfect number


# Solution 1:
x = int(input("Enter a Number: "))
factor_sum = 0


for i in range(1, x):
    if x % i == 0:
        factor_sum += i


if x == factor_sum:
    print("Given number is a perfect number")
else:
    print("Given number is not a perfect number")


# Solution 2:
x = int(input("Enter a Number: "))
factor_sum = 0

i = 1
while i < x:
    if x % i == 0:
        factor_sum += i
    i += 1

if x == factor_sum:
    print("Given number is a perfect number")
else:
    print("Given number is not a perfect number")


# Solution 3:
x = int(input("Enter a Number: "))
factor_sum = 1

i = 2
while i < x**0.5:
    if x % i == 0:
        factor_sum += i + (x/i)

    i += 1

if x == factor_sum:
    print("Given number is a perfect number")
else:
    print("Given number is not a perfect number")
