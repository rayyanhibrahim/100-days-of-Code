def set_zeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows = set()
    zero_cols = set()

    # Find rows and columns containing zero
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Set corresponding rows and columns to zero
    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0


# Example
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

set_zeroes(matrix)

print("Matrix after setting zeroes:")
for row in matrix:
    print(row)
#output
Matrix after setting zeroes:
[1, 0, 1]
[0, 0, 0]
[1, 0, 1]
