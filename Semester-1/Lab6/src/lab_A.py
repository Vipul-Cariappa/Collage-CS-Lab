# program to check each character in the given string is an alphabet or digit

# Solution 1:
string = input("Enter a string: ")

for i in string:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        print(f"{i} -> Character")
    elif i >= '0' and i <= '9':
        print(f"{i} -> Number")
    else:
        print(f"{i} -> Special Character")


# Solution 2:
string = input("Enter a string: ")

for i in string:
    if i.isalpha():
        print(f"{i} -> Character")
    elif i.isnumeric():
        print(f"{i} -> Number")
    else:
        print(f"{i} -> Special Character")
