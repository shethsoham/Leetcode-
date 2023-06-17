#Order of n3 
#Matrix multiplication (n*n*n = n^3)

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

result = []

for i in range(3):
    row = []
    for j in range(3):
        element = 0
        for k in range(3):
            element += A[i][k] * B[k][j]
        row.append(element)
    result.append(row)

# Print the result matrix
for row in result:
    print(row)
