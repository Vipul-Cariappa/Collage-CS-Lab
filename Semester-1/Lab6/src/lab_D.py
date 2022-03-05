# program to print alphabet pattern 'A'

x = int(input("Enter the height: "))

A = "#"
S = " "

print(S*x, A)

j = 1
for i in range(x-1, 0, -1):
    print(S*i, A, end="")

    n = 2 * j - 2

    if j == x // 2:
        print(A*(n+2))
    else:
        print(S*n, A)

    j += 1
