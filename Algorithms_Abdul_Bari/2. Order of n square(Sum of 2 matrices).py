# Time complexity in order of n square. 
#Finding sum of two matrices (n*n) = n^2

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

C = []

# Iterate over each row
for i in range(len(A)):
    row = []
    # Iterate over each column
    for j in range(len(A[0])):
        # Sum the corresponding elements from A and B
        row.append(A[i][j] + B[i][j])
    # Add the row to the result matrix C
    C.append(row)

# Print the result matrix C
for row in C:
    print(row)
