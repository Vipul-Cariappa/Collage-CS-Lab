# program to count the numbers of occurrences of characters in the given string and store them in a dictionary

string = input("Enter a string: ")

d = {}

for i in string:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1

print(d)
