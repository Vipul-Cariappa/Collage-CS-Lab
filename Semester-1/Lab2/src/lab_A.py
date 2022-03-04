# program to swap 2 variable values

x, y = input("Enter Two Numbers: ").split() 
x, y = int(x), int(y)

print(f"Before Swapping: {x = }   {y = }")

# Swapping the values
tmp = x
x = y
y = tmp

print(f"After Swapping: {x = }   {y = }")
