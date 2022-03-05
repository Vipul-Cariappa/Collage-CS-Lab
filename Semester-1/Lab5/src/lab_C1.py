# program to perform addition and subtraction of two matrices

# logic to get user data to create the matrix
m, n = input("Enter row * cloumn of the matrix: ").split()
m, n = int(m), int(n)

mat1 = []
mat2 = []

print("Enter data for matrix 1:")
for i in range(m):
    row = list(map(int, input("Enter the elements of the row: ").split()))
    mat1.append(row)

print("Enter data for matrix 2:")
for i in range(m):
    row = list(map(int, input("Enter the elements of the row: ").split()))
    mat2.append(row)


# logic to perform the operations
addtion_matrix = []
subtraction_matrix = []

for i in range(m):
    addtion_matrix.append([])
    subtraction_matrix.append([])
    
    for j in range(n):
        addtion_matrix[i].append(mat1[i][j] + mat2[i][j])
        subtraction_matrix[i].append(mat1[i][j] - mat2[i][j])

print("Addtion: ", *addtion_matrix, sep="\n")
print("Subtraction: ", *subtraction_matrix, sep="\n")
