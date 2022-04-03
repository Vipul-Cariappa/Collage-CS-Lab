# program to display first n lines in a text file

n = int(input("Enter number of lines: "))

with open("note.txt") as file:
    while n > 0:
        print(
            file.readline(),
            end=""
        )
        n -= 1
