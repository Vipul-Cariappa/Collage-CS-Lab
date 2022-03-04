# program to find average of 3 numbers

x, y, z = input("Enter 3 numbers to compute the average: ").split()
x, y, z = int(x), int(y), int(z)

average = (x + y + z) / 3

print(f"Average of gien three numbers is {average}")
