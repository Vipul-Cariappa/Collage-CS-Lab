# program to find duplicate characters in the given string and store them in a list

# Solution 1:
string = input("Enter a string: ")

content = []
duplicate = []

for i in string:
    if i in content and i not in duplicate:
        duplicate.append(i)
    else:
        content.append(i)

print(duplicate)


# Solution 2:
string = input("Enter a string: ")

duplicate = []

for i in string:
    if string.count(i) > 1 and i not in duplicate:
        duplicate.append(i)

print(duplicate)


