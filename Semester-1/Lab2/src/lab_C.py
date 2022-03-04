# program to find area and perimeter of rectangle

x, y = input("Enter Lenght and Width of the rectangle: ").split()
x, y = int(x), int(y) 


area = x * y
perimeter = 2 * (x + y)

print(f"{area = }   {perimeter = }")
